from tkinter import *
import random

root=Tk()
root.title("List")
root.geometry("400x400")

random_word_list = Label(root)
random_word = Label(root)

def word():

    random_word = random.sample(range(a,z),5)
    random_word_list["text"] = "random word : " + str(random_word)
    
    
btn=Button(root,text="generate word list ",command=word)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

random_word_list.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()