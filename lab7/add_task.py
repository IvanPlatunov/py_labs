import requests
import json
import tkinter
from PIL import Image, ImageTk
import random

window = tkinter.Tk()
window.title("Picture generator")
window.geometry("700x500")
btn = tkinter.Button(text="Generate")
def gen_pic():
    global btn
    btn.destroy()
    response = requests.get("https://nekos.best/api/v2/neko")
    img_data = response.json()
    print(img_data["results"][0]["url"])
    pic_resp = requests.get(img_data["results"][0]["url"])
    f = open("image.png", "w+b")
    f.write(pic_resp.content)
    im = Image.open(f)
    bg = ImageTk.PhotoImage(im)
    label1 = tkinter.Label(image=bg)
    label1.image = bg
    label1.place(x=0, y=0, relwidth=1, relheight=1)
    btn = tkinter.Button(text="Generate", command=gen_pic)
    btn.pack(expand=True)
    


btn = tkinter.Button(text="Generate", command=gen_pic)
btn.pack(expand=True)
window.mainloop()




