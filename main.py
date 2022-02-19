# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import pytesseract
from time import time
from screenCapture import ScreenCapture
import pyfirmata

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# WindowName = "Movies & TV"
'''
def list_window_names():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), win32gui.GetWindowText(hwnd))
    win32gui.EnumWindows(winEnumHandler, None)
list_window_names();
# call it like this:
def Screen_Capture():
    w = 1920  # set this
    h = 1080  # set this
    bmpfilenamename = "out.bmp"  # set this


    hwnd = win32gui.FindWindow(None, "Movies & TV")

    if not hwnd:
        raise Exception('Window not found: {}'.format("windowName"));
    window_rect = win32gui.GetWindowRect(hwnd)
    w = window_rect[2] - window_rect[0];
    h = window_rect[3] - window_rect[1];

    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (0, 0), win32con.SRCCOPY)
    # saves the screenshot

    #dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
    signedIntsArray = dataBitMap.GetBitmapBits(True);
    img = np.fromstring(signedIntsArray, dtype='uint8');
    img.shape = (h,w,4);

    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    img = img[...,:3]
    return img





##print(text);
##cv2.imshow("img", img);
##cv2.waitKey(0);
'''
def Trial_1():
    wincap = ScreenCapture('Real-time Object Detection - OpenCV Object Detection in Games #5 - YouTube - Google Chrome');
    loop_time = time();
    while(True):
        screenshot = wincap.get_screenshot()

        cv2.imshow('Computer Vision', screenshot);
        print('FPS {}'.format(1/(time() - loop_time)));

        loop_time = time();

        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows();
            break;

    print("done");
img = cv2.imread("screenshot.png");

text = pytesseract.image_to_string(img)
ConversionToSomethingReadable = text.split('/');
DeathsInGame = ConversionToSomethingReadable[1];
print(DeathsInGame);