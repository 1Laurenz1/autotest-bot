"""
Service for interacting with OpenAI API

Сервис для взаимодействия с OpenAI API
"""

import re

from openai import AsyncOpenAI
from typing import Optional, List, Union

from app.core import settings, logger


class AIService:
    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "gpt-4o-mini"
    ) -> None:
        
        if not api_key and not settings.OPENAI_KEY.get_secret_value():
            logger.exception("API key is not configurated in .env")
            raise ValueError("OpenAI key is not configurated")
        
        self.client = AsyncOpenAI(api_key=api_key or settings.OPENAI_KEY.get_secret_value())
        self.model = model
        
        logger.info(f'The AIService initialized with the model: {self.model}')

    
    async def ask(
        self, text: str,
        system_prompt: str = (
            "You are a helpful assistant. "
            "For each question, choose only one of the four options given to you. "
            "If you see answer options - respond with just one letter."
            "But if you don't see the options for answers, you need to come up with a brief response to the question."
            "Do not invent extra information. "
        ),
        **kwargs
        ) -> str:
        """
        Send a text prompt to the AI model and receive a response.
        :param text: User input text or question.
        :param system_prompt: System instruction for the AI. Defaults to a guideline for choosing one option.
        :param kwargs: Additional parameters for the OpenAI API call (like temperature, max_tokens, etc.)
        :return: Response text from the AI, stripped of leading/trailing whitespace.
        """
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": text}
                ],
                stream=False,
                **kwargs
            )
            answer = response.choices[0].message.content.strip()
            
            logger.info("AI response succesfully received")
                
            return answer
            
        except Exception as e:
            logger.exception("AI request failed")
            raise RuntimeError("OpenAI API request failed") from e
        
        
    async def choose_options(
        self,
        text: str,
        options: Union[str, List[str]],
        temperature: float = 0.2
    ) -> str:
        """
        Method for questions with a single choice answer
        :param text: text of question
        :param options: a str with options separated by commas, for example "A, B, C, D, E"
        :param temperature: degree of randomness (lower means a more deterministic response)
        :return: selected option (letter only)
        """
        
        if isinstance(options, list):
            options_str = ", ".join(options)
        else:
            options_str = options
        
        prompt = (
            f"You are a helpful assistant. Choose only one of these options: {options_str}. "
            "Do not invent other options. Respond only with the chosen letter."
        )
        
        answer = await self.ask(text, system_prompt=prompt, temperature=temperature)
        
        allowed_letters = [o.strip().upper() for o in options_str.split(",")]
        answer_clean = next((c for c in answer if c.upper() in allowed_letters), None)
        
        if not answer_clean:
            logger.warning(
                f"GPT returned unexpected answer: {answer} Returning first allowed option:"
            )
            answer_clean = allowed_letters[0]
        return answer_clean
    

ai_model = AIService()