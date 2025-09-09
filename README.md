# 🌐 Languages: [EN](README.md) | [RU](README_RU.md)

# Autotest Bot

Automation of online test completion for distance learning.
The project is designed for use with Python and allows you to:

- Recognize text on the screen (OCR)

- Send questions to a neural network to choose the correct answer

- Emulate user actions (mouse clicks, keyboard input)

- Easily extend and customize for new platforms

---

## Table of Contents

1. [Installation](#-Installation)
2. [Usage](#-Usage)
3. [Examples](#-examples)
4. [Technologies](#-Technologies)
5. [Important Notes](#-Important)
6. [License](#-License)

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

    OPENAI_API_KEY=your_openai_api_key_here

---

## Usage

Run the main script:

    python -m app.run

---

The bot will:

1. Take screenshots of the test questions.

2. Recognize text using OCR.

3. Ask GPT to provide correct answers.

4. Automatically click/select answers.


## Examples

Example screenshot text:

    Question: Who is the author of "The Tale of Igor's Campaign"?
    A) Ivan Franko
    B) Lesya Ukrainka
    C) Mykhailo Kotsiubynsky
    D) Taras Shevchenko

    AI chooses option:
    D

---


Example without options:

    Question: Summarize the following text: "Ukraine declared independence in 1991..."

    AI response:
    Ukraine became an independent country in 1991.


--- 
## Technologies

- Python 3.11+

- pytesseract (OCR)

- Pillow, OpenCV (image processing)

- pyautogui, pynput (input emulation)

- openai (GPT API)

- SQLAlchemy + SQLite/PostgreSQL (optional)

**See requirements.txt for exact versions.**

---

## ⚠️ Important

- This project is intended only for personal and educational use.
Do not use it to bypass rules of educational platforms.

---

## 📄 License

This project is covered by the MIT license.