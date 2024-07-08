import os
import pywhatkit as kit
import pyautogui
from dotenv import load_dotenv
import time

load_dotenv()

phone_number = os.getenv('PHONE_NUMBER')

kit.sendwhatmsg(phone_number, "tagoot kia ha bhai", 22, 40)
time.sleep(20)
pyautogui.press("enter")



