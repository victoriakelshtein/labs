from tkinter import *

import requests

root = Tk()


def get_fact():
	title = cityField.get()
 
	url = 'https://animechan.vercel.app/api/random/anime?title={}'.format(title)

	print(url)

	result = requests.get(url)
	anime = result.json()
	print(anime)

	info["text"] = f'{anime["anime"]}: {anime["character"], anime["quote"]}'


root['bg'] = '#fafafa'
root.title('Интересные факты об аниме')
root.geometry('1300x500')
root.resizable(width=False, height=False)

frame_top = Frame(root, bg='#fff700', bd=5)
frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)

frame_bottom = Frame(root, bg='#fff700', bd=5)
frame_bottom.place(relx=0.05, rely=0.55, relwidth=0.9, relheight=0.3)

cityField = Entry(frame_top, bg='white', font=30)
cityField.pack()

btn = Button(frame_top, text='Узнать факт об аниме', command=get_fact)
btn.pack()

info = Label(frame_bottom, text='Факты об аниме', bg='#fff700', font=40)
info.pack()

root.mainloop()
