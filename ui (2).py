import speech_recognition as sr
from tkinter import *
from googletrans import Translator
from PyDictionary import PyDictionary
translator=Translator()
r=sr.Recognizer()
s=""
def printr():
    with sr.Microphone() as source:
        txt.delete(1.0,END)
        r.adjust_for_ambient_noise(source,duration=0.5)
        r.energy_threshold=700
        txt.insert(INSERT,"\nListening...")
        audio = r.listen(source)
        txt.insert(INSERT,"\nRecognizing...")
        txt.pack()
        try:
            global s
            s=str(r.recognize_google(audio,language='en-IN'))
            txt.insert(INSERT,"You said : "+s)
            txt.insert(INSERT,"\nHindi Translation: "+((translator.translate(s,dest='hi')).text))
            txt.insert(INSERT,"\nFrench Translation: "+((translator.translate(s,dest='fr')).text))
            txt.insert(INSERT,"\nBengali Translation: "+((translator.translate(s,dest='bn')).text))
            txt.pack()
        except sr.UnknownValueError:
            txt.insert(INSERT,"Could not understand audio")
        except sr.RequestError as e:
            txt.insert(INSERT,"Could not request results; {0}".format(e))
def hindi():
    txt.delete(1.0,END)
    txt.insert(INSERT,"\nबोले : ")
    txt.pack()
    with sr.Microphone() as source:                                                                       
        audio = r.listen(source)
        try:
            global s
            s=str(r.recognize_google(audio,language='hi-HI'))
            txt.insert(INSERT,"\nआपने कहा : "+s)
            txt.pack()
            txt.insert(INSERT,"\nEnglish Translation: "+((translator.translate(s,dest='en')).text))
            txt.pack()
            txt.insert(INSERT,"\nFrench Translation: "+((translator.translate(s,dest='fr')).text))
            txt.pack()
            txt.insert(INSERT,"\nBengali Translation: "+((translator.translate(s,dest='bn')).text))
            txt.pack()
        except sr.UnknownValueError:
            txt.insert(INSERT,"Could not understand audio")
        except sr.RequestError as e:
            txt.insert(INSERT,"Could not request results; {0}".format(e))
def bangla():
    txt.delete(1.0,END)
    txt.insert(INSERT,"\nকথা বলা : ")
    txt.pack()
    with sr.Microphone() as source:                                                                       
        audio = r.listen(source)
        try:
            global s
            s=str(r.recognize_google(audio,language='bn-BN'))
            txt.insert(INSERT,"\nআপনি বললেন : "+s)
            txt.pack()
            txt.insert(INSERT,"\nEnglish Translation: "+((translator.translate(s,dest='en')).text))
            txt.pack()
            txt.insert(INSERT,"\nFrench Translation: "+((translator.translate(s,dest='fr')).text))
            txt.pack()
            txt.insert(INSERT,"\nHindi Translation: "+((translator.translate(s,dest='hi')).text))
            txt.pack()
        except sr.UnknownValueError:
            txt.insert(INSERT,"Could not understand audio")
        except sr.RequestError as e:
            txt.insert(INSERT,"Could not request results; {0}".format(e))
def french():
    txt.delete(1.0,END)
    txt.insert(INSERT,"\nParler(Speak) : ")
    txt.pack()
    with sr.Microphone() as source:                                                                       
        audio = r.listen(source)
        try:
            global s
            s=str(r.recognize_google(audio,language='fr-FN'))
            txt.insert(INSERT,"Tu as dit (You said) : "+s)
            txt.pack()
            txt.insert(INSERT,"\nEnglish Translation: "+((translator.translate(s,dest='en')).text))
            txt.pack()
            txt.insert(INSERT,"\nBengali Translation: "+((translator.translate(s,dest='bn')).text))
            txt.pack()
            txt.insert(INSERT,"\nHindi Translation: "+((translator.translate(s,dest='hi')).text))
            txt.pack()
        except sr.UnknownValueError:
            txt.insert(INSERT,"Could not understand audio")
        except sr.RequestError as e:
            txt.insert(INSERT,"Could not request results; {0}".format(e))
def dicn():
    txt.insert(INSERT,"\nSpeak :")
    with sr.Microphone() as source:                                                                       
        audio = r.listen(source)
        try:
            s=str(r.recognize_google(audio))
            dictionary=PyDictionary(s)
            txt.insert(INSERT,"You said : "+s+"\n")
            txt.insert(INSERT,(dictionary.getMeanings()))
            txt.insert(INSERT,"\nHindi Meaning: "+((translator.translate(s,dest='hi')).text))
            txt.insert(INSERT,"\nFrench Meaning: "+((translator.translate(s,dest='fr')).text))
            txt.insert(INSERT,"\nBengali Meaning: "+((translator.translate(s,dest='bn')).text))
            txt.pack()
        except sr.UnknownValueError:
            txt.insert(INSERT,"Could not understand audio")
        except sr.RequestError as e:
            txt.insert(INSERT,"Could not request results; {0}".format(e))
def savetxt():
    n=Tk()
    n.title('Save File')
    Label(n,text="File Name").grid(row=0,column=0)
    def ret():
        content=e1.get()
        f=open(content,'w',encoding="utf-8") #openning a file in write mode with file name in content variable. Encoding in utf-8 for accepting characters from any language!!
        inp=txt.get("1.0",END)
        f.write(inp)
        f.close()
        n.destroy()
    e1=Entry(n)
    e1.grid(row=0,column=1)
    button=Button(n,text='Save',command=ret).grid()
    n.mainloop()
m=Tk()
txt=Text(m)
m.title('Voice Recognition')
ph = PhotoImage(file=r"micicon.png")
button=Button(m,image=ph,command=printr)
button.pack(side=LEFT)
button1=Button(m,text='Clear Box',width=25,command=lambda: txt.delete(1.0,END),activeforeground='Red')
button1.pack(side=LEFT)
txt.insert(INSERT,"Welcome to Voice Recognition!!\n")
txt.pack()
menu=Menu(m)
mode=Menu(menu,tearoff=0)
file=Menu(menu,tearoff=0)
menu.add_cascade(label='File', menu=file)
file.add_cascade(label='Save',command=savetxt)
menu.add_cascade(label='Mode', menu=mode)
trans=Menu(mode,tearoff=0)
dic=Menu(mode)
mode.add_cascade(label='Translator', menu=trans)
mode.add_command(label='Dictionary',command=dicn)
lang=Menu(trans,tearoff=0)
trans.add_cascade(label='Input Language', menu=lang)
lang.add_command(label='English',command=printr)
lang.add_command(label='Hindi',command=hindi)
lang.add_command(label='Bengali',command=bangla)
lang.add_command(label='French',command=french)
m.config(menu=menu)
m.mainloop()
