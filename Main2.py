import numpy as np
import cv2
from PIL import ImageGrab
import pyautogui
import pytesseract
import time
from pyfirmata import Arduino,util
import serial
result = 0;
result2 = result - 1;
x = 500
y = 2000
w = 100
h = 11007
cords = 0
thingy = True;
DeathsInGame = 0;
board = Arduino('COM3');

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def test_Pytesseract():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    screenshot = pyautogui.screenshot();
    screenshot = np.array(screenshot);
    text = pytesseract.image_to_string(screenshot)
    cv2.imshow("img", screenshot)
    print(text);
    cv2.waitKey(0);

def screen_Capture():
    while True:
        screenshot = pyautogui.screenshot();
        screenshot = np.array(screenshot);
        text = pytesseract.image_to_string(screenshot)
        cv2.imshow('Computer Vision', screenshot)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()
    print('Done');

# pyautogui.displayMousePosition()
def deezNuts():
    while(True):
        X = 1683;
        Y = 38;
        image = ImageGrab.grab(bbox=(1683,38,100,100))
        img_np = np.array(image)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

def Trial_2():
    while True:
        img = ImageGrab.grab(bbox=(0, 200, 1920, 1200))  # x, y, w, h #                     #
        img_np = np.array(img)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0Xff == ord('q'):
            break
    cv2.destroyAllWindows()
def Trial_That_Works():
    time.sleep(2);
    print("ooooo");
    while True:
        screenshot = pyautogui.screenshot('screenshot.png', region = (1665,0, 100, 25));
        img_np = np.array(screenshot)
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        img = cv2.imread('screenshot.png');
        text = pytesseract.image_to_string(img)
        #cv2.imshow("frame", frame)
        try:
            ConversionToSomethingReadable = text.split('/');
            DeathsInGame = int(ConversionToSomethingReadable[1]);
            result = DeathsInGame
            result2 = result - 1
            YourAssIsGettingTazed();
        except IndexError:
            continue;
    print('Done');

def YourAssIsGettingTazed():
    #time.sleep(5)
    if (result == result2 + 1):
        # LEDpin = board.get_pin('d:13:p')
        board.digital[12].write(1);

        time.sleep(5)
        board.digital[12].write(0);
        print("Tazed");

def Take_ScreenShot():
    time.sleep(5);
    screenshot = pyautogui.screenshot('Screenshot.jpg', region = (850,1000, 100, 50));
    img_np = np.array(screenshot)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    img = cv2.imread(frame);
    text = pytesseract.image_to_string(img)
    print(text);
'''
Trial_That_Works()
img = cv2.imread('Screenshot.jpg');
#picture = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
text = pytesseract.image_to_string(img)
print(text);
'''
#Trial_That_Works()
#YourAssIsGettingTazed()
#cv2.destroyAllWindows()
#print('done');

# references to helpful code
'''
img = ImageGrab.grab(bbox=None)  # x, y, w, h
img_np = np.array(img) <--- use this for the *mat* error
frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
'''
def Take_ScreenShotV2():
    #board.digital[13].write(1);
    time.sleep(5);
    while True:
        try:
            screenshot = pyautogui.screenshot('Screenshot.jpg', region=(850, 1000, 100, 50));
            img_np = np.array(screenshot)
            img = cv2.imread('Screenshot.jpg');
            text = pytesseract.image_to_string(img)
            SomeBullshit = text.split("/")
            Health = SomeBullshit[0];
            print("done");
            if Health == "0":
                YourAssIsGettingTazed()
        except IndexError:
            continue
#Take_ScreenShotV2();
#board.digital[13].write(0);

#YourAssIsGettingTazed();


'''
while True:
    Take_ScreenShotV2()
    img = cv2.imread('Screenshot.jpg');
    text = pytesseract.image_to_string(img)
    SomeBullshit = text.split("/")
    Health = int(SomeBullshit[0]);
    if Health == 0:
        YourAssIsGettingTazed()  
print(Done);
'''