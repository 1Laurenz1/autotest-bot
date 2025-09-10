import asyncio
from pathlib import Path
from app.core import ocr, TestSolver
from app.api import ai_model

import time

async def TestSolver_first_test():
    answer_counter = 0
    ai_service = ai_model
    solver = TestSolver(ocr_model=ocr, ai=ai_service)
    
    while answer_counter <= 12:
        await asyncio.sleep(5)
        
        screenshot_path = await ocr.save_screenshot("test_screenshot.png")
        text = await ocr.recognize_text(screenshot_path)
        
        answer = await ai_service.ask(
            text=text,
            system_prompt=(
                "You have been given a question and a list of possible answers. "
                "Choose only one correct answer. "
                "Return strictly the text of the answer option, without explanations. "
                "You need to give only 1 letter. "
                "1 - A, 2 - B, 3 - C, 4 - D."
            )
        )
        answer = answer.strip().upper()[0]
        
        await solver.recognize_and_click(answer)
        answer_counter += 1
    
        print(f"OCR text:\n{text}")
        print(f"AI answer:\n{answer}")



if __name__ == '__main__':
    asyncio.run(TestSolver_first_test())