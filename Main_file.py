import gtts
from playsound import playsound
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import speech_recognition as sr
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import chromedriver_binary
import sqlite3
import time
import datetime
from num2words import num2words
from word2number import w2n
import translators
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

name=''
acc_num=''
branch=''
connection = sqlite3.connect("accounts_db.db")
crsr = connection.cursor()
com="select * from accounts"
crsr.execute(com)
account = crsr.fetchall()
listener = sr.Recognizer()
listener.pause_threshold = 0.50
listener.energy_threshold = 500
review_command=[]
command = ""


def fetch_amt():
    count=0
    while(count<=5):
        try:
            count=count+1
            listener = sr.Recognizer()
            listener.pause_threshold = 0.55
            listener.energy_threshold = 1000
            command = ""
            with sr.Microphone() as source:
                print('listening...')
                #voice = listener.listen(source)
                voice = listener.listen(source, timeout = 3)
                print("processing voice...")
                command = listener.recognize_google(voice, language= "te")
                command = command.lower()
                print("YOU SAID: " + command)
                translation=command
            if(('లక్ష రూపాయలు' in command) or ('లక్ష' in command)):
                translation=='100000'
            if (command.isdigit() or translation.isdigit()):
                    return translation
    
            translation= translators.google(command,from_language="te",to_language='en')
            
            print (translation,' ...............')
            
            if ('rupees' in translation):
                translation=translation.replace(' rupees','')
            if (' Rs' in translation):
                translation=translation.replace(' Rs','')
            if (' Rs.' in translation):
                translation=translation.replace(' Rs.','')
    
            print (translation)
    
    
            if (translation=='One lakh'):
                translation='100000'
        
            if (translation.isdigit()==False):
                translation=w2n.word_to_num(translation)
            print(translation)
            return translation
        except:
            
            print('Try again')
            x=fetch_amt()
            return x
    
def closee():
    while(True):
        pass

def deposit(acc_num):
    print("Deposit")
    playsound("D:\Projects\Automatic Bank Form\Automatic Form Generation System IVRS\Audio Files\deposit.mp3")
    amnt=fetch_amt()


    playsound("D:\Projects\Automatic Bank Form\Automatic Form Generation System IVRS\Audio Files\wait.mp3")
    
    print("\nThank You! For Banking with us")    
    
    current_time = datetime.datetime.now()

    web = webdriver.Chrome(ChromeDriverManager().install())
    web.get("D:\Projects\Automatic Bank Form Generation using IVRS\Deposit_Form.html")
    
 
    nm= web.find_element(By.XPATH, '//*[@id="17_firstname-6"]')
    nm.send_keys(name)
    
    date=str(current_time.day)+'-'+str(current_time.month)+'-'+str(current_time.year)



    dt= web.find_element(By.XPATH, '//*[@id="17_shorttext-10"]')
    dt.send_keys(date)

    br= web.find_element(By.XPATH, '//*[@id="17_shorttext-8"]')
    br.send_keys(branch)

    rs= web.find_element(By.XPATH, '//*[@id="17_shorttext-16"]')
    rs.send_keys(amnt)

    an= web.find_element(By.XPATH, '//*[@id="17_shorttext-11"]')
    an.send_keys(acc_num)

    amnt_word=num2words(amnt).upper()
    if('HUNDRED THOUSAND' in amnt_word):
        amnt_word='ONE LAKH'

    amt= web.find_element(By.XPATH, '//*[@id="17_shorttext-2"]')
    inwords = amnt_word + ' RUPEES ONLY'
    amt.send_keys(inwords)
    
    time.sleep(100)
    
    exit()


    while(True):
        pass



def withdraw(acc_num):
    print("Withdraw")
    playsound("D:\Projects\Automatic Bank Form\Automatic Form Generation System IVRS\Audio Files\withdraw.mp3")
    amnt=fetch_amt()

    playsound("D:\Projects\Automatic Bank Form\Automatic Form Generation System IVRS\Audio Files\wait.mp3")
    
    print("\nThank You! For Banking with us")

    current_time = datetime.datetime.now()

    web = webdriver.Chrome(ChromeDriverManager().install())
    web.get("D:\Projects\Automatic Bank Form Generation using IVRS\Withdraw_Form.html")

    nm= web.find_element(By.XPATH, '//*[@id="17_firstname-6"]')
    nm.send_keys(name)
    date=str(current_time.day)+'-'+str(current_time.month)+'-'+str(current_time.year)

    dt= web.find_element(By.XPATH, '//*[@id="17_shorttext-10"]')
    dt.send_keys(date)

    br= web.find_element(By.XPATH, '//*[@id="17_shorttext-8"]')
    br.send_keys(branch)

    rs= web.find_element(By.XPATH, '//*[@id="17_shorttext-16"]')
    rs.send_keys(amnt)

    an= web.find_element(By.XPATH, '//*[@id="17_shorttext-11"]')
    an.send_keys(acc_num)
    amnt_word=num2words(amnt).upper()
    if('HUNDRED THOUSAND' in amnt_word):
        amnt_word='ONE LAKH'

    amt= web.find_element(By.XPATH, '//*[@id="17_shorttext-2"]')
    inwords = amnt_word + ' RUPEES ONLY'
    amt.send_keys(inwords)
   
    time.sleep(100)
    
    exit()
    
    while(True):
        pass

    

def hello_name(acc_num):
    
    count=0
    inp=''
    
    print("\nNamaste! "+ name +" Welcome to STREAK BANK")
    tts = gtts.gTTS(name)
    tts.save("D:\Projects\Automatic Bank Form\Automatic Form Generation System IVRS\Audio Files\que.mp3")

    playsound("D:\Projects\Automatic Bank Form\Automatic Form Generation System IVRS\Audio Files\que.mp3")
    
    while (('deposit' not in inp) or ('withdraw' not in inp)):
            print("\nWithdraw or deposit")
            playsound("D:\Projects\Automatic Bank Form\Automatic Form Generation System IVRS\Audio Files\que1.mp3")

            with sr.Microphone() as source:
                count=count+1
                print('listening...')
                voice = listener.listen(source, timeout = 5)
                print("processing voice...")
                command = listener.recognize_google(voice, language= "te")
                command = command.lower()
                print("YOU SAID: " + command)
                if(('ట్రో' in command)or ('త్ర' in command)):
                    command="withdraw" 
    
            if(('deposit' in command) or ('ఆపోజిట్' in command) or('డిపో' in command) or ('వేయాలి' in command) or ('డిపాజిట్ చేయాలి' in command) or('డబ్బులు ఉండాలి' in command) or ('డబ్బులు ఉంచాడు' in command) or('పెట్టాలనుకుంటున్నాను' in command) or('ఇవ్వాలని అనుకుంటున్నా' in command) or('ఇవ్వాలనుకుంటున్న' in command) or('ఇవ్వాలని అనుకుంటున్నాను' in command) or('ఇవ్వాలనుకుంటున్నాను' in command) or('డబ్బులు వెయ్యాలా అనుకుంటున్నాను' in command) or('వెయ్యాలని అనుకుంటున్నాను' in command) or('వేయాలి అనుకుంటున్నా' in command) or('డబ్బులు ఇవ్వాలని అనుకుంటున్నా' in command) or('నేపాల్ అనుకుంటున్నా' in command) or('డబ్బులు వేయాలి' in command) or ('డబ్బులు వేయాలి అనుకుంటున్నా' in command) or ('డబ్బులు ఎలా అనుకుంటున్నారు'in command) or ('వెయ్యాలి' in command) or ('డిపోసిట్'  in command) or ('పెట్టాలి' in command) or ('ఉంచాలి' in command) or ('ఇవ్వాలి' in command) or ('డిపాజిట్' in command) or ('ఉంచేయాలి' in command) or ('ఇది పోస్ట్ చెయ్యాలి అని అనుకుంటున్నాను' in command) or ('ఏం చేయాలి' in command) or ('ఆపోజిట్ చేయాలనుకుంటున్నాను' in command) or('డిపోలు చేయాలనుకుంటున్నా' in command)):
                inp='deposit'
                deposit(acc_num)
                break
            elif(('ట్రో' in command)or ('తియ్యాలి' in command) or ('త్ర' in command) or('వివో చెయ్యాలి' in command) or ('ట్రా' in command) or ('డ్రా'in command) or ('విత్ డ్రా' in command) or ('విత్డ్రా' in command) or ('పెట్రా' in command) or ('బిడ్డ' in command) or ('itra' in command) or ('రా' in command) or ('తీసుకోవాలి' in command) or ('తీయాలి' in command) or ('తీసుకోవాలనుకుంటున్నాను' in command) or ('తీసుకొని అనుకుంటున్నా' in command)or('డబ్బులు తియ్యాలి అనుకుంటున్నా'  in command) or ('డబ్బులు తీయాలనుకుంటున్నాను' in command) or ('తీయాలనుకుంటున్నాను' in command)or ('డబ్బులు తీసుకోవాలని అనుకుంటున్నాను' in command) or('డబ్బులు తీసుకోండి అని అనుకుంటున్నాను' in command) or ('డబ్బులు తీసుకొని అని అనుకుంటున్నాను' in command) or('డబుల్ తీయాలనుకున్నాను' in command) or('డబ్బులు ఇయ్యాలి' in command) or ('డబ్బులు తియ్యాలి' in command) or('చెయ్యాలి అని అనుకుంటున్నా' in command) or('ఇయ్యాల అనుకుంటున్నా' in command) or ('ఇయాల అనుకుంటున్నా' in command) or ('విడ్మెట్ చేయాలి' in command)or ('widrow చేయాలనుకుంటున్నాను' in command) or ('విడుదల చేయాలనుకుంటున్నారు' in command) or ('widrow' in command) or ('విడో చేయాలనుకుంటున్నాను' in command) or ('విండో చేయాలి' in command) or ('విడుదల చేయాలి' in command)):
                inp='withdraw'
                withdraw(acc_num)
                break
            else:
                inp='others'
                review_command.append(command)
                playsound("D:\Projects\Automatic Bank Form\Automatic Form Generation System IVRS\Audio Files\others_command.mp3")
                if(count==5):
                    playsound("D:\Projects\Automatic Bank Form\Automatic Form Generation System IVRS\Audio Files\didnt.mp3")
                    playsound("D:\Projects\Automatic Bank Form\Automatic Form Generation System IVRS\Audio Files\thank.mp3")
                    break

    print(name)
    print(branch)
    exit()


def fetch_data(acc_no):
    global name
    global branch
    global acc_num
    for i in account:
        if acc_no in i:
            print(i)
            name=i[1]
            acc_num=i[0]
            branch=i[2]
            hello_name(acc_num)
        


def scan():
    
    def decoder(image):
        gray_img = cv2.cvtColor(image,0)
        barcode = decode(gray_img)
        for obj in barcode:
            points = obj.polygon
            (x,y,w,h) = obj.rect
            pts = np.array(points, np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(image, [pts], True, (0, 255, 0), 3)
            
            
            barcodeData = obj.data.decode("utf-8")
            barcodeType = obj.type
            string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)
            
            cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
             
            print("Barcode: "+barcodeData +" | Type: "+barcodeType)
            #print(len(barcodeData))
            
            if len(barcodeData)==11:
                print("Scanned\n")
                fetch_data(barcodeData)
            return barcodeData
    
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        x = decoder(frame)

        cv2.imshow('Image', frame)
        code = cv2.waitKey(10)
        if code == ord('q'):
            break


playsound("D:\Projects\Automatic Bank Form\Automatic Form Generation System IVRS\Audio Files\welcome.mp3")

scan()
