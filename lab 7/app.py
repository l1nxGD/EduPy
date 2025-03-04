import requests
from PIL import ImageTk
import tkinter as tk
from random import randint


def get_image():
    date = randint(1, 124)
    req = requests.get(f'https://randomfox.ca/images/{date}.jpg')
    img = ImageTk.PhotoImage(data=req.content)
    return img

def update_image():
    img = get_image()
    label_image.configure(image=img)
    label_image.image = img


window = tk.Tk()
window.title('Cute Fox')
window.geometry("1024x1024")

start_image = get_image()
label_image = tk.Label(window, image = start_image)
label_image.place(x=0, y=0, relwidth=1, relheight=1)

btn_rnd = tk.Button(window, text = 'Random Fox', font = ('Calibri', 12), command = update_image)
btn_rnd.place(relx = .5, rely = .9, anchor = 'c')

window.mainloop()




