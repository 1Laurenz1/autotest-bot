"""
Module for solving tests by selecting and clicking answers

Модуль для решения тестов: выбор и клик по ответам
"""

class TestSolver:
    def __init__(self, ocr_model=None, ai=None) -> None:
        from app.core import ocr
        from app.api import ai_model
        
        self.ocr = ocr_model or ocr
        self.ai = ai or ai_model