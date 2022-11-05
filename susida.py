import pyautogui as pa
import time
from PIL import Image
import sys
import pyocr
import pyocr.builders
from gtts import gTTS

def moji(a):
    tools = pyocr.get_availadle_tools()
    tool = tools[0]

    langs = tool.get_available_languags()
    lang =langs[0]
    # txtに変換した文字列を代入する
    txt = tool.image_to_string(
        Image.open(a + '.png'),
        lang="eng",
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    )
    Text = list(txt)  # 文字列を配列に変換
    count =len(Text)
    i = 0
    while True:  # 寿司打の場合小文字アルファベットか'-'しか出て来ないのでそれ以外の文字が出てきていたら削除する
        if i >= count:
            break
        if Text[i] < 'a' or Text[i] > 'z':
            if Text[i] != '-':
                del Text[i]
                count -= 1
            else:
                i += 1
        else:
            i += 1
    
    txt = str(''.join(Text))  # 文字列に戻す


def main():
    start = time.time()
    pa.mouseDown(x=765, y=588, button='left')
    pa.mouseUp()
    pa.typewrite(" ", interval=0.0)
    nowtime = time.time()
    while True:
        if time.time() - nowtime > 1.5:
            break
    i = 0
    while True:
        if time.time() - nowtime > 300:
            break
        print(i)
        img = pa.screenshot(
            imageFilename="screenshot" + str(i) + ".pug",  # 保存先ファイル名
            region=(797, 588, 275, 30)  # 撮影範囲(x,y,width,height)
        )
        string = moji.moji("screenshot" + str(i))
        pa.typewrite(string, interval=0.0)
        print(string)
        nowtime1 = time.time()
        while True:
            if time.time() - nowtime1 > 0.25:
                break
        i += 1

myText = "string"
language = 'ja'
output = gTTS(text=myText, lang=language, slow=False)
output.save(output.mp3)

if __name__ == "__main__":
    main()
