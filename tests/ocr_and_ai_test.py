import asyncio
from pathlib import Path
from app.core import ocr
from app.api import ai_model

async def test_ocr_ai_pipeline():
    ai_service = ai_model
    
    screenshot_path = await ocr.save_screenshot("test_screenshot.png")
    text = await ocr.recognize_text(screenshot_path)
    answer = await ai_service.ask(
        text=text,
        system_prompt="You are a helpfull assistant."
    )
    
    print(f"OCR text:\n{text}")
    print(f"AI answer:\n{answer}")

if __name__ == '__main__':
    asyncio.run(test_ocr_ai_pipeline())