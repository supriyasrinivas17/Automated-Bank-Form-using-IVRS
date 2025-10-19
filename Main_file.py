import cv2
import numpy as np
from pyzbar.pyzbar import decode
import re
import sqlite3
import gtts
import pygame
import speech_recognition as sr
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings
import datetime
import time
import os
from num2words import num2words
from word2number import w2n
import translators

warnings.filterwarnings("ignore", category=DeprecationWarning)

# Initialize pygame mixer once
pygame.mixer.init()

def play_audio(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Database setup and fetch all accounts
connection = sqlite3.connect("accounts_db.db")
crsr = connection.cursor()
crsr.execute("SELECT * FROM accounts")
account = crsr.fetchall()

name = ''
acc_num = ''
branch = ''
listener = sr.Recognizer()
listener.pause_threshold = 0.50
listener.energy_threshold = 500
review_command = []
MIC_DEVICE_INDEX = None  # optionally set mic device index here

def fetch_amt():
    count = 0
    while count <= 5:
        try:
            count += 1
            recognizer = sr.Recognizer()
            recognizer.pause_threshold = 0.55
            recognizer.energy_threshold = 1000
            with sr.Microphone(device_index=MIC_DEVICE_INDEX) as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)
                print('Listening for amount...')
                voice = recognizer.listen(source, timeout=5)
                print("Processing voice...")
                command = recognizer.recognize_google(voice, language="te").lower()
                print("YOU SAID: " + command)
                translation = command
            if 'లక్ష' in command:
                translation = '100000'
            if command.isdigit() or translation.isdigit():
                return translation
            translation = translators.google(command, from_language="te", to_language='en')
            translation = translation.replace(' rupees', '').replace(' Rs', '').replace(' Rs.', '')
            if translation == 'One lakh':
                translation = '100000'
            if not translation.isdigit():
                translation = w2n.word_to_num(translation)
            return translation
        except Exception as e:
            print('Try again. Error:', e)
            if count > 5:
                print("Max tries reached. Exiting fetch_amt.")
                return None

def deposit(acc_num):
    global name, branch
    print("Deposit")
    play_audio(r"Audio Files\deposit.mp3")
    amnt = fetch_amt()
    if amnt is None:
        print("Amount not detected. Ending deposit.")
        return
    play_audio(r"Audio Files\wait.mp3")
    print("\nThank You! For Banking with us")

    current_time = datetime.datetime.now()
    abs_path = os.path.abspath(r"Deposit_Form.html")
    file_url = 'file://' + abs_path.replace("\\", "/")
    service = Service(ChromeDriverManager().install())
    web = webdriver.Chrome(service=service)
    web.get(file_url)
    wait = WebDriverWait(web, 10)

    wait.until(EC.presence_of_element_located((By.ID, "17_firstname-6"))).send_keys(name)
    wait.until(EC.presence_of_element_located((By.ID, "17_shorttext-10"))).send_keys(f"{current_time.day}-{current_time.month}-{current_time.year}")
    wait.until(EC.presence_of_element_located((By.ID, "17_shorttext-8"))).send_keys(branch)
    wait.until(EC.presence_of_element_located((By.ID, "17_shorttext-16"))).send_keys(amnt)
    wait.until(EC.presence_of_element_located((By.ID, "17_shorttext-11"))).send_keys(acc_num)

    amnt_word = num2words(amnt).upper()
    if 'HUNDRED THOUSAND' in amnt_word:
        amnt_word = 'ONE LAKH'

    inwords = amnt_word + ' RUPEES ONLY'
    wait.until(EC.presence_of_element_located((By.ID, "17_shorttext-2"))).send_keys(inwords)

    print("Please review and submit the deposit form in the browser window.")
    time.sleep(100)
    exit()

def withdraw(acc_num):
    global name, branch
    print("Withdraw")
    play_audio(r"Audio Files\withdraw.mp3")
    amnt = fetch_amt()
    if amnt is None:
        print("Amount not detected. Ending withdrawal.")
        return
    play_audio(r"Audio Files\wait.mp3")
    print("\nThank You! For Banking with us")

    current_time = datetime.datetime.now()
    abs_path = os.path.abspath(r"Withdraw_Form.html")
    file_url = 'file://' + abs_path.replace("\\", "/")
    service = Service(ChromeDriverManager().install())
    web = webdriver.Chrome(service=service)
    web.get(file_url)
    wait = WebDriverWait(web, 10)

    wait.until(EC.presence_of_element_located((By.ID, "17_firstname-6"))).send_keys(name)
    wait.until(EC.presence_of_element_located((By.ID, "17_shorttext-10"))).send_keys(f"{current_time.day}-{current_time.month}-{current_time.year}")
    wait.until(EC.presence_of_element_located((By.ID, "17_shorttext-8"))).send_keys(branch)
    wait.until(EC.presence_of_element_located((By.ID, "17_shorttext-16"))).send_keys(amnt)
    wait.until(EC.presence_of_element_located((By.ID, "17_shorttext-11"))).send_keys(acc_num)

    amnt_word = num2words(amnt).upper()
    if 'HUNDRED THOUSAND' in amnt_word:
        amnt_word = 'ONE LAKH'

    inwords = amnt_word + ' RUPEES ONLY'
    wait.until(EC.presence_of_element_located((By.ID, "17_shorttext-2"))).send_keys(inwords)

    print("Please review and submit the withdrawal form in the browser window.")
    time.sleep(100)
    exit()

def hello_name(acc_num):
    global name, branch
    count = 0
    inp = ''
    print(f"\nNamaste! {name} Welcome to STREAK BANK")
    tts = gtts.gTTS(name)
    tts.save(r"Audio Files\que.mp3")
    play_audio(r"Audio Files\que.mp3")

    while (('deposit' not in inp) and ('withdraw' not in inp)):
        print("\nWithdraw or deposit")
        play_audio(r"Audio Files\que1.mp3")
        with sr.Microphone(device_index=MIC_DEVICE_INDEX) as source:
            count += 1
            listener.adjust_for_ambient_noise(source, duration=1)
            print('Listening for transaction type...')
            try:
                voice = listener.listen(source, timeout=5)
            except sr.WaitTimeoutError:
                print("Listening timed out. Please try again.")
                continue
            print("Processing voice...")
            try:
                command = listener.recognize_google(voice, language="te").lower()
            except sr.UnknownValueError:
                print("Sorry, I did not understand that. Please try again.")
                continue
            except sr.RequestError as e:
                print(f"Could not request results; {e}")
                break
            print("YOU SAID: " + command)

            if 'ట్రో' in command or 'త్ర' in command:
                command = "withdraw"

        if any(word in command for word in ['deposit', 'ఆపోజిట్', 'డిపో', 'వేయాలి', 'డిపాజిట్', 'పెట్టాలి', 'ఇవ్వాలి']):
            inp = 'deposit'
            deposit(acc_num)
            break
        elif any(word in command for word in ['withdraw', 'తియ్యాలి', 'త్ర', 'విత్ డ్రా', 'విత్డ్రా', 'తీయాలి']):
            inp = 'withdraw'
            withdraw(acc_num)
            break
        else:
            inp = 'others'
            review_command.append(command)
            play_audio(r"Audio Files\others_command.mp3")
            if count == 5:
                play_audio(r"Audio Files\didnt.mp3")
                play_audio(r"Audio Files\thank.mp3")
                break

    print(name)
    print(branch)
    exit()

def fetch_data(acc_no):
    global name, branch, acc_num
    print(f"Received scanned account number: {acc_no}")
    found = False
    for record in account:
        print(f"Checking against DB account: {record[0]}")
        if acc_no == record[0]:
            print(f"Account found: {record}")
            name = record[1]
            acc_num = record[0]
            branch = record[2]
            found = True
            hello_name(acc_num)
            break
    if not found:
        print("No matching account found in database.")

def decoder(image):
    gray_img = cv2.cvtColor(image, 0)
    barcodes = decode(gray_img)
    for obj in barcodes:
        full_text = obj.data.decode("utf-8")
        print("Full QR code data:", full_text)
        search = re.search(r"Account Number[:\s]*([\d\s\-]+)", full_text)
        if search:
            candidate = search.group(1).replace(" ", "").replace("-", "").strip()
            print(f"Extracted candidate repr: {repr(candidate)}")
            if len(candidate) == 11 and candidate.isdigit():
                account_num = candidate
                print(f"Extracted Account Number: {account_num}")
                fetch_data(account_num)
                return True
            else:
                print(f"Extracted candidate is not a valid 11-digit number: {candidate}")
        else:
            print("No 'Account Number' label found in QR data.")
        return False
    return False

def scan():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        found = decoder(frame)
        cv2.imshow('Image', frame)
        if found:
            break
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

play_audio(r"Audio Files\welcome.mp3")
scan()
