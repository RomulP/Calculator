# a brilliant creation of a mad mind

from tkinter import *
from tkinter import messagebox

wnd = Tk()
wnd.title('Счеты')
wnd.geometry('500x600')
wnd.resizable(False, False)
wnd.config(bg='black')

# базовая функция
def base(inp):
	global form

	if inp == '=':
		form = str(eval(form))
	elif inp == 'C':
		form = ''
	elif inp == 'Del':
		form = form[0:-1]
	elif inp == '':
		command=click()
	else:		
		form += inp
	txt.config(text=form)

# окно
form = ''
txt = Label(text=form, bg='black', fg='white', font=('arial', 70, 'bold'))
txt.place(x=11, y=20)

# кнопки
buttons = ['7', '8', '9', '-',
		   '4', '5', '6', '+',
		   '1', '2', '3', '*',
		   '.', '0', '=', '/',
		   '', 'C', 'Del', '']
x = 18
y = 170
for bttn in buttons:
	get_lbl = lambda x=bttn: base(x)
	Button(text=bttn, bg='red', fg='white', font=('arial 20'), command=get_lbl).place(x=x, y=y, width=115, height=79)
	x += 117
	if x > 400:
		x = 18
		y += 81

def click():
	messagebox.showinfo('Ну ёпти', 'Ты мне кулькулятер сломал!')


wnd.mainloop()