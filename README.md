# Autotest Bot

Automation of online test completion for distance learning.
The project is designed for use with Python and allows you to:

- Recognize text on the screen (OCR)

- Send questions to a neural network to choose the correct answer

- Emulate user actions (mouse clicks, keyboard input)

- Easily extend and customize for new platforms

---

## ⚙️ Installation

### 1. Clone the repository

    git clone https://github.com/1Laurenz1/autotest-bot.git
    cd autotest_bot

### 2. Create a virtual environment
    
    python -m venv .venv

### 3. Activate the virtual environment


    .venv\Scripts\Activate.ps1

### 4. Install dependencies


    pip install -r requirements.txt

### 5. Create a .env file with your API key

    OPENAI_API_KEY=ваш_ключ

---

## Usage

Run the main script:

python -m app.run

---

## Technologies

- Python 3.11+

- pytesseract (OCR)

- Pillow, OpenCV (image processing)

- pyautogui, pynput (input emulation)

- openai (GPT API)

- SQLAlchemy + SQLite/PostgreSQL (optional)

---

## ⚠️ Important

- This project is intended only for personal and educational use.
Do not use it to bypass rules of educational platforms. [EN]

- Проект предназначен только для личного использования и учебных целей.
Не используйте его для обхода правил образовательных платформ. [RU]

---

## 📄 License

MIT License