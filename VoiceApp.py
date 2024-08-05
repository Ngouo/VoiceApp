from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os



#Fenetre
root = Tk()
root.title('VoiceApp')
root.resizable(False, False)
root.geometry("900x450+150+150")
root.configure(bg='#305065')

engine = pyttsx3.init()

def SpeakNow():
  text = text_area.get(1.0, END)
  gender = gender_combobox.get()
  speed = speed_combobox.get()
  voices = engine.getProperty('voices')
  
  def setvoice():
    if(gender == 'Anglais'):
      engine.setProperty('voice', voices[0].id)
      engine.say(text)
      engine.runAndWait()
      
    else:
      engine.setProperty('voice', voices[1].id)
      engine.say(text)
      engine.runAndWait()
      
  if(text):  
    if(speed == 'Fast'):
      engine.setProperty("rate", 250)
      setvoice()
    elif(speed == "Normal"):
        engine.setProperty("rate", 150)
        setvoice()
    else:
      engine.setProperty("rate", 60)
      setvoice()
           
      
def Download():
  text = text_area.get(1.0, END)
  gender = gender_combobox.get()
  speed = speed_combobox.get()
  voices = engine.getProperty('voices')
  
  def setvoice():
    if(gender == 'Male'):
      engine.setProperty('voice', voices[0].id)
      path = filedialog.askdirectory()
      os.chdir(path)
      engine.save_to_file(text ,'text.mp3')
      engine.runAndWait()
      
    else:
      engine.setProperty('voice', voices[1].id)
      path = filedialog.askdirectory()
      os.chdir(path)
      engine.save_to_file(text ,'text.mp3')
      engine.runAndWait()
      
  if(text):  
    if(speed == 'Fast'):
      engine.setProperty("rate", 250)
      setvoice()
    elif(speed == "Normal"):
        engine.setProperty("rate", 150)
        setvoice()
    else:
      engine.setProperty("rate", 60)
      setvoice()



#Partie haute
Top_Frame = Frame(root, bg='white', width=900, height=100)
Top_Frame.place(x=0, y=0)

#Logo = PhotoImage(file="speaker logo.png")
Label(Top_Frame, bg='white').place(x=10, y=5)

#Titre de l'Appli
Label(Top_Frame, text='TEXT TO SPEECH', font=("Arial", 20, 'bold'), bg='#fff', fg='#000').place(x=40, y=40)


##########

text_area = Text(root, font='Robote 20', bg='white', relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

Label(root, text='VOICE', font='Arial 15 bold', bg='#305065', fg='white').place(x=560, y=160)
Label(root, text='SPEED', font='Arial 15 bold', bg='#305065', fg='white').place(x=760, y=160)


gender_combobox = Combobox(root, values=["Anglais", 'Francais'], font="Arial 14", state='r', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set("Anglais")

speed_combobox = Combobox(root, values=['Fast', "Normal", "Slow"], font='Arial 14', state='r', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set("Normal")


#Boutons
#image_icon1 = PhotoImage(file="speak.png")
btn = Button(root, text="Speak",width=10,compound=LEFT, font=("Arial", 14, 'bold'), command=SpeakNow)
btn.place(x=550, y=300)

#image_icon2 = PhotoImage(file="download.png")
btn2 = Button(root, text="Save",width=10,compound=LEFT, bg='#39C790', font=("Arial", 14, 'bold'), command=Download)
btn2.place(x=730, y=300)









root.mainloop()
