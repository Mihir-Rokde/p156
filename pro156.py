from tkinter import*
from  PIL import ImageTk,Image
import random
root=Tk()
root.title("Endless Pokemon Card Game")
root.geometry("600x400")
root.configure(background="lightgreen")

img=ImageTk.PhotoImage(Image.open("button.jpg"))

pikachu=ImageTk.PhotoImage(Image.open("pikachu.jpg"))
bulbasour=ImageTk.PhotoImage(Image.open("bulbasour.jpg"))
charmender=ImageTk.PhotoImage(Image.open("charmender.jpg"))
squirtle=ImageTk.PhotoImage(Image.open("squirtle.jpg"))
ratata=ImageTk.PhotoImage(Image.open("ratata.jpg"))
nidoking=ImageTk.PhotoImage(Image.open("nidoking.jpg"))
jigglypuff=ImageTk.PhotoImage(Image.open("jigglypuff.jpg"))
meowth=ImageTk.PhotoImage(Image.open("meowth.jpg"))
persion=ImageTk.PhotoImage(Image.open("persion.jpg"))
abra=ImageTk.PhotoImage(Image.open("abra.jpg"))
kadabra=ImageTk.PhotoImage(Image.open("kadabra.jpg"))
iyvasour=ImageTk.PhotoImage(Image.open("Iyvasour.jpg"))


player1=Label(root,text="PLayer1",bg="red",fg="white")
player1.place(relx=0.1,rely=0.3,anchor=CENTER)

player2=Label(root,text="PLayer2",bg="red",fg="white")
player2.place(relx=0.9,rely=0.3,anchor=CENTER)

player1score=Label(root,bg="orange",fg="white")
player1score.place(relx=0.1,rely=0.4,anchor=CENTER)

player2score=Label(root,bg="orange",fg="white")
player2score.place(relx=0.9,rely=0.4,anchor=CENTER)

pokemon_list=[pikachu,bulbasour,charmender,squirtle,squirtle,nidoking,jigglypuff,meowth,persion,abra,kadabra,iyvasour]
power_list=[200,60,100,50,50,40,70,60,70,30,70]
label=Label(root)
label.place(relx=0.5,rely=0.5,anchor=CENTER)

player1_score=0
player2_score=0

def player1():
    global player1_score
    rn1=random.randint(1,6)
    random_pokemon=pokemon_list[rn1]
    label["image"]=random_pokemon
    
    random_power_list=power_list[rn1]
    
    player1_score=player1_score+random_power_list
    player1score["text"]=str(player1_score)
    
p1btn=Button(root,image=img,command=player1)    
p1btn.place(relx=0.1,rely=0.6,anchor=CENTER)

def player2():
    global player2_score
    rn2=random.randint(1,6)
    random_pokemon1=pokemon_list[rn2]
    label["image"]=random_pokemon1
    
    random_power_list=power_list[rn2]
    
    player2_score=player2_score+random_power_list
    player2score["text"]=str(player2_score)
    
p2btn=Button(root,image=img,command=player2)    
p2btn.place(relx=0.9,rely=0.6,anchor=CENTER)


root.mainloop()