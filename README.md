Automatic Bank Form Generation using IVRS (Extended Version)
This project is an enhanced and extended version of the original system developed by MJR Varma (Jagannadha Rohit Varma Mandhapati) at Maharaj Vijayaram Gajapathi Raj College of Engineering. The extension builds upon his socially relevant initiative designed to assist illiterate users in filling out banking forms through an intelligent IVRS-based system.

Overview
The system enables users to automatically generate bank forms using voice interaction in Telugu, their native language. By bridging speech recognition, text translation, and automated form generation, it assists individuals who face literacy barriers in performing routine banking operations independently.

Functionality
The system captures the QR code on the user's bank passbook using a camera sensor.

It decodes the QR to extract the account number.

Using the account number, it fetches user details from the database.

Through voice prompts in Telugu, the system asks whether the user wishes to deposit or withdraw money.

The user responds via speech in Telugu, which is recognized, translated, and processed.

The system then asks for the amount, processes it, and generates the official bank form in printable format.

This entire process minimizes manual entry and enables underserved populations to access financial systems more easily.

Technologies and Requirements
Language: Python 3.x

Core Dependencies:

gtts — Text-to-Speech, generates Telugu audio responses

playsound — Plays audio messages for user interaction

cv2 — Captures and processes images (QR recognition via webcam)

numpy — Image data operations

pyzbar — Decodes QR codes

speech_recognition — Converts user's Telugu speech to text

selenium — Automates the form-filling process on bank portals

webdriver_manager — Manages ChromeDriver for Selenium

sqlite3 — Manages the accounts database (local storage)

num2words — Converts numeric amounts to words

word2number — Converts spoken numbers into digits

translators — Translates Telugu speech input into English for internal logic processing

Install dependencies using:

text
pip install gtts playsound opencv-python numpy pyzbar SpeechRecognition selenium webdriver-manager num2words word2number translators
Usage
Ensure all packages are installed.

Connect a working camera for QR scanning and microphone for voice input.

Run the main file from your terminal:

text
python main.py
Follow voice instructions in Telugu to complete the form-filling process automatically.

Extension Description
This extended version incorporates improvements such as:

Better multilingual translation support.

Optimized QR scanning and error handling.

Streamlined interaction flow for smoother user experience.

Modular code restructuring for maintainability.

The original core concept and functionality were first developed by MJR Varma, and this project serves as a refined adaptation extending his socially impactful contribution.

Conclusion
The Automatic Bank Form Generation using IVRS (Extended Version) stands as a step toward inclusive technological accessibility. By allowing users to interact in their own language and automating form generation, it embodies the spirit of socially responsible innovation through technology.

