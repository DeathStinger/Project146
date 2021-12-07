from tkinter import *

root =Tk()

root.title("Fibonacci ")
root.geometry("400X400")

label_series=Lable(root,  text="Fibbonacci Series ")

def Fibonacci():
    num=10
    first_no=0
    second_no=1
    sum=0
    counter=1
    while (counter<=0):
label_series["text"] += str(sum) + " "
    counter=counter+1
    first_no=second_no
    second_no=sum+second_no
    sum=first_no+second_no
    
    
btn=Button(root,text="Show Fibbonacci Series",command=Fibbonacci)

btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()

                                                                                                                                                     )
root.mainloop()