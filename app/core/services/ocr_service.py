"""
OCR Service for text recognition from screenshots.

Сервис для распознавания текста с помощью Tesseract OCR.
"""

from pathlib import Path
from typing import Optional, Protocol, List, Tuple

from app.core import logger

import os
import asyncio

from PIL import Image, ImageGrab
import pytesseract


class ScreenshotTool(Protocol):
    def screenshot(self) -> Image.Image: ...
        
class PILScreenshotTool(ScreenshotTool):
    def screenshot(self) -> Image.Image:
        return ImageGrab.grab()


class OCREngine(Protocol):
    def image_to_string(self, image: Image.Image, lang: str) -> str: ...
    
class PytesseractEngine(OCREngine):
    def image_to_string(self, image: Image.Image, lang: str | List[str]) -> str:
        return pytesseract.image_to_string(image, lang)


class OCRService:
    def __init__(
        self,
        folder_path: Path = Path("screenshots"),
        ocr_engine: Optional[OCREngine] = None,
        screenshot_tool: Optional[ScreenshotTool] = None,
        languages: str = "ukr+eng+rus"
    ) -> None:
        self.folder_path = folder_path
        self.ocr_engine = ocr_engine
        self.screenshot_tool = screenshot_tool
        self.languages = languages

        os.makedirs(self.folder_path, exist_ok=True)
        logger.info(f"OCRService initialized, folder: {self.folder_path}")
    
        
    async def save_screenshot(self, filename: str = "screenshot.png") -> Path:
        if self.screenshot_tool is None:
            raise RuntimeError("Screenshot tool is not set")

        base_name = Path(filename).stem
        ext = Path(filename).suffix or ".png"
        screenshot_path = self.folder_path / filename
        counter = 1

        while screenshot_path.exists():
            screenshot_path = self.folder_path / f"{base_name}_{counter}{ext}"
            counter += 1

        def _make_screenshot():
            screenshot = self.screenshot_tool.screenshot()
            
            top_crop = 200
            width, height = screenshot.size
            cropped_screenshot = screenshot.crop((0, top_crop, width, height))
            
            cropped_screenshot.save(screenshot_path)

        await asyncio.to_thread(_make_screenshot)
        logger.info(f"Screenshot saved: {screenshot_path}")
        return screenshot_path


    async def recognize_text(self, image_path: Path) -> str:
        if not image_path.exists():
            logger.error(f"File does not exist: {image_path}")
            raise FileNotFoundError(f"Image not found: {image_path}")

        if self.ocr_engine is None:
            raise RuntimeError("OCR engine is not set")

        def _ocr():
            image = Image.open(image_path)
            return self.ocr_engine.image_to_string(image, lang=self.languages)

        try:
            text = await asyncio.to_thread(_ocr)
            result = text.strip()
            logger.info(f"OCR completed successfully for {image_path}")
            return result
        except Exception as e:
            logger.exception(f"OCR failed for {image_path}")
            raise RuntimeError("OCR failed") from e
        
    
screenshot_tool = PILScreenshotTool()
ocr_engine = PytesseractEngine()

ocr = OCRService(
    folder_path=Path("screenshots"),
    ocr_engine=ocr_engine,
    screenshot_tool=screenshot_tool,
    languages="ukr+eng+rus"
)