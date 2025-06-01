import json
import requests
import tkinter as tk
from PIL import ImageTk, Image


def click():
    data = requests.get('https://api.nasa.gov/planetary/apod?api_key=4vgoYdKYUUQZYzFe8IhuVQWTeWwTBc6WTAy95fAX')
    nasa_json = data.json()
    f = open('f.json', 'w')
    json.dump(nasa_json, f)
    response = requests.get(nasa_json["hdurl"])
    file_path = 'nasa.png'

    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

    new_img = ImageTk.PhotoImage(Image.open(file_path))
    label_bg.configure(image=new_img)
    label_bg.image = new_img


root = tk.Tk()
root.title('Photo of the today')
root.geometry('800x800')

label_bg = tk.Label(root)
label_bg.place(x=0, y=0, relwidth=1, relheight=1)

btn_key = tk.Button(root, text="Get a photo", command=click)
btn_key.place(x=700, y=700)

root.mainloop()
