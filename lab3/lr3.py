import tkinter as tk
import generator as gen
import pygame

def generate_code():
    num = list(str(cipher_entry.get()))
    if (''.join(num).isdigit() == False) or not(int(''.join(num)) < 1000 and int(''.join(num)) > 99):
        final_code = "Warning: Please enter a three digit number."
    else:
        first_part = gen.generate()
        second_part = gen.shake(first_part, int(num[0]), 0)
        third_part = gen.shake(second_part, int(num[1]), 1)
        fourth_part = gen.shake(third_part, int(num[2]), 2)
        final_code = f'{first_part}-{second_part}-{third_part}-{fourth_part}'
    code_label.configure(text = final_code)
    pass

window = tk.Tk()
window.title("Generator hoi4")
window.geometry("512x512")
bg_img = tk.PhotoImage(file = 'background.png')


pygame.mixer.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play()


label_bg = tk.Label(window, image=bg_img)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

title_label = tk.Label(window, text = 'Generator for hoi4', font = ('Calibri', 24))
title_label.place(x = 512/3, y = 50)

code_label = tk.Label(window, text = 'Your code', font=('Calibri', 18))
code_label.place(relx = .5, rely = .6, anchor='c')

cipher_entry = tk.Entry(window, width=10, font = ('Calibri', 16))
cipher_entry.place(relx = .4, rely = .3, anchor = 'e')

btn_for_gen = tk.Button(window, text = 'Ok', command=generate_code)
btn_for_gen.place(relx = .45, rely = .3, anchor = 'w')

window.mainloop()
