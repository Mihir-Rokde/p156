from tkinter import*
from  PIL import ImageTk,Image
root=Tk()
root.title("Endless Pokemon Card Game")
root.geometry("600x400")
root.configure(background="lightgreen")

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

randomdice=Label(root,bg="yellow",fg="black")
randomdice.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()