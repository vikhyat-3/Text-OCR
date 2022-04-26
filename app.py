from PIL import Image
from gtts import gTTS
import cv2
import pytesseract as pt
from google.colab.patches import cv2_imshow
def Text_to_speech(text_msg):
    speech = gTTS(text = text_msg)
    print(text_msg)
    speech.save('do.mp3')
img=cv2.imread("/content/hftthw.png")
img
