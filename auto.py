import keyboard
import pyperclip
import translate
import threading
import time
from PIL import Image, ImageDraw, ImageFont
import subprocess
def display(text = "你好,世界!"):
    image = Image.new("RGB", (2000, 1000), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('simhei.ttf', size=36)
    draw.text((1000, 500), text, font=font, anchor="mm", fill=(0, 0, 0))
    image.save('tem.jpg')
    subprocess.call(['start', 'tem.jpg'], shell=True)
class auto:
    def __init__(self):
        self.start = True
        self.detected = False
        self.f_list = []
        self.k_list = []
        self.translator = translate.translate()
        self.update_function()
    def tran(self):
        #pyautogui.hotkey('ctrl','c')
        word =  pyperclip.paste().strip()
        contents = self.translator.tran(word)
        display(contents)
        if contents == 'Error':
            pass
        elif contents == '':
            pass
        else:
            with open('word.txt','r',encoding='utf-8') as f:
                for line in f:
                    if line[:-2] == word:
                        break
                    else:
                        pass
                else:
                    with open('word.txt','a',encoding='utf-8') as f:
                        f.write(word+':\n')
                        f.write(contents)       
                        f.write('-'*10+'\n')
        

    def update_function(self):
        self.k_list.append(['ctrl','c','z'])
        self.f_list.append(self.tran)


        self.function_number = len(self.f_list)

    def key_detected(self,keys_to_detect,f):
        if all(keyboard.is_pressed(key) for key in keys_to_detect):
            if not self.detected:
                t = threading.Thread(target=f())
                t.start()
                self.detected = True
        else:
            self.detected = False
    def run(self):
        while self.start:
            time.sleep(0.5)
            for i in range(self.function_number):
                self.key_detected(self.k_list[i],self.f_list[i])
M = auto()
M.run()