"""
Module for solving tests by selecting and clicking answers

Модуль для решения тестов: выбор и клик по ответам
"""

import pyautogui
from pathlib import Path

from app.core import logger


class TestSolver:
    def __init__(
        self,
        ocr_model=None,
        ai=None,
        red_button=pyautogui.Point(x=333, y=1048),
        yellow_button=pyautogui.Point(x=964, y=1048),
        blue_button=pyautogui.Point(x=1594, y=1048),
        green_button=pyautogui.Point(x=2235, y=1048)
    ) -> None:
        from app.core import ocr
        from app.api import ai_model

        self.ocr = ocr_model or ocr
        self.ai = ai or ai_model
        self.red_button = red_button
        self.yellow_button = yellow_button
        self.blue_button = blue_button
        self.green_button = green_button
        
    
    async def recognize_and_click(
        self,
        ai_answer: str,
    ) -> bool:

        if ai_answer == "A":
            pyautogui.click(self.red_button)
            logger.info("Clicked RED button (A)")
        elif ai_answer == "B":
            pyautogui.click(self.yellow_button)
            logger.info("Clicked YELLOW button (B)")
        elif ai_answer == "C":
            pyautogui.click(self.blue_button)
            logger.info("Clicked BLUE button (C)")
        elif ai_answer == "D":
            pyautogui.click(self.green_button)
            logger.info("Clicked GREEN button (D)")
        else:
            logger.warning(f"Не удалось сопоставить AI ответ: {ai_answer}")
            return False

        return True
