import tkinter as tk
from captcha import verify_input, equation_captcha
import tkinter.messagebox as box

HEIGHT = 290
WIDTH = 300

CAPTCHA = equation_captcha()


def convert():
    try:
        int(entry.get())
    except ValueError:
        box.showerror(title="error", message='This input is not valid.' + '\n'
                                             ' Please, try again!')
        refresh_onclick()
    else:
        verify_onclick(int(entry.get()))


def verify_onclick(user_input: int):
    if verify_input(user_input, CAPTCHA) is True:
        verified = tk.Label(window, text="Verified as human!")
        verified.pack()
        entry.delete(0, "end")
    elif verify_input(user_input, CAPTCHA) is False:
        not_verified = tk.Label(window, text="Please, try again!")
        not_verified.pack()
        refresh_onclick()


def refresh_onclick():
    global label
    global CAPTCHA
    NEW_CAPTCHA = equation_captcha()
    CAPTCHA = NEW_CAPTCHA
    label.config(text=NEW_CAPTCHA)


window = tk.Tk()
window.title("TriSolving - Math Captcha")
window.resizable(0, 0)
frame = tk.Canvas(window, height=HEIGHT, width=WIDTH)
frame.pack()

entry = tk.Entry(window)
entry.pack()

label = tk.Label(window, text=CAPTCHA, bg='#70818f', fg='#c6ccd2')
label.config(height=2)
label.config(width=15)
label.config(font=('Ariel', 25))
label.pack()

btn = tk.Button(window, text="Verify", bg='white', fg='#5a6772',
                command=convert)
btn.pack()

refresh_btn = tk.Button(window, text="Refresh", bg='white', fg='#5a6772',
                        command=refresh_onclick)
refresh_btn.pack()

label.place(x=30, y=70)
entry.place(x=55, y=170)
btn.place(x=85, y=230)
refresh_btn.place(x=155, y=230)

window.mainloop()
