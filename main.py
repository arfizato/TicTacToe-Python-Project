from tkinter import *
import tkinter as tk
from tkinter import messagebox



# checking if one of the players won 
def checkForWin(mat,l,c,xo):
    # checking main diagonal
        
    prevl=l-1 if l>0 else 2
    prevc=c-1 if c>0 else 2
    nextl=l+1 if l<2 else 0
    nextc=c+1 if c<2 else 0

    if (l==c):
        if (mat[prevl][prevc]+mat[nextl][nextc]+mat[l][c]==xo*3):
            return TRUE
    # checking the opposite diagonal 
    elif (l+c==2): 
        if (mat[prevl][nextc]+mat[nextl][prevc]+mat[l][c]==xo*3):
            return TRUE   
    #checking lines and columns 
    if(mat[prevl][c]+mat[nextl][c]+mat[l][c]==xo*3 or mat[l][prevc]+mat[l][nextc]+mat[l][c]==xo*3):
        return TRUE
    else:
        return FALSE
    
    

# Defining the functions for the buttons 
def buttonClicked(text,button,l,c):
    global x, numOfButtonsDisabled, stopPlaying, firstChar, secondChar
    x+=1
    choiceButton["state"]= DISABLED
    choiceButton["bg"]="#404040"
    choiceButton["fg"]="#000000"

    button["state"]= DISABLED
    #button["relief"]= "sunken"
    if (x%2==0):        
        button["bg"]="#dbf9db"

        text.set(firstChar)
        mat[l-1][c]=firstChar 
        #print(checkForWin(mat,l-1,c,"X")) 
        if checkForWin(mat,l-1,c,firstChar):
            box = messagebox.askquestion("Player 2 Won", "Would You Like To Keep Playing?")
            if (box !='yes'):
                #here i want to call RESTART
                #print("stoppppppppppppppppp playing  ",stopPlaying)
                stopPlaying=TRUE
                #print("saha :)")             
            root.destroy()      
    else:
        button["bg"]="#f2ffc2"
        text.set(secondChar)
        mat[l-1][c]=secondChar
        #print(checkForWin(mat,l-1,c,"O"))  
        if checkForWin(mat,l-1,c,secondChar):
            box=messagebox.askquestion("Player 1 Won", "Would You Like To Keep Playing?")
            if (box!='yes'):
                #here i want to call RESTART
                stopPlaying=TRUE
                #print("saha :)")                
            root.destroy()  

    numOfButtonsDisabled+=1
    if numOfButtonsDisabled==9:
        box=messagebox.askquestion("It's a TIE ", "Would You Like To Keep Playing?")
        if (box!='yes'):
            stopPlaying=TRUE
        root.destroy()
    #print(mat)

#picking what to fill the buttons with
def changeText(text,button):
    global firstChar, secondChar, charList, charNumber
    charNumber= charNumber+1 if charNumber<2 else 0
    firstChar=charList[charNumber][0] 
    secondChar=charList[charNumber][1]
    text.set(charList[charNumber][2])   


"""--------------------------Main--------------------------"""    
global stopPlaying
stopPlaying=FALSE
while (stopPlaying==FALSE):
    #print("stop playing  ",stopPlaying)
    
    charNumber=0
    charList=[["X","O","X O"],["-","+","- +"],[""," ","Only Color"]]
    mat=[["."]*3,["."]*3,["."]*3]
    numOfButtonsDisabled=0
        
    root = tk.Tk()
    root.title("Tic Tac toe")
    #root.geometry("1000x1000")

    # defining buttons                   and                      putting them on a grid 

    global x, firstChar, secondChar
    firstChar="X"
    secondChar="O"    
    x=0 
    text0  = tk.StringVar()
    text0.set("Click To Pick Variant")

    text1  = tk.StringVar()
    text2  = tk.StringVar()
    text3  = tk.StringVar()

    text4  = tk.StringVar()
    text5  = tk.StringVar()
    text6  = tk.StringVar()

    text7  = tk.StringVar()
    text8  = tk.StringVar()
    text9  = tk.StringVar()
    #text1.set("")
    choiceButton  = Button(root,textvariable=text0,width=39,height=5,bg="#bbcab7", command= lambda: changeText(text0,choiceButton))
    choiceButton.grid(row=0 ,column=0, columnspan=3)

    button1  = Button(root,textvariable=text1,text="",width=12,height=5,bg="#e1f1dd", command= lambda: buttonClicked(text1,button1,3,0) )
    button1.grid(row=3 ,column=0)
    button2  = Button(root,textvariable=text2,text="",width=12,height=5,bg="#bbcab7", command= lambda: buttonClicked(text2,button2,3,1) )
    button2.grid(row=3 ,column=1)
    button3  = Button(root,textvariable=text3,text="",width=12,height=5,bg="#e1f1dd", command= lambda: buttonClicked(text3,button3,3,2) )
    button3.grid(row=3 ,column=2)

    button4  = Button(root,textvariable=text4,text="",width=12,height=5,bg="#bbcab7", command= lambda: buttonClicked(text4,button4,2,0) )
    button4.grid(row=2 ,column=0)
    button5  = Button(root,textvariable=text5,text="",width=12,height=5,bg="#e1f1dd", command= lambda: buttonClicked(text5,button5,2,1) )
    button5.grid(row=2 ,column=1)
    button6  = Button(root,textvariable=text6,text="",width=12,height=5,bg="#bbcab7", command= lambda: buttonClicked(text6,button6,2,2) )
    button6.grid(row=2 ,column=2)

    button7  = Button(root,textvariable=text7,text="",width=12,height=5,bg="#e1f1dd", command= lambda: buttonClicked(text7,button7,1,0) )
    button7.grid(row=1 ,column=0)
    button8  = Button(root,textvariable=text8,text="",width=12,height=5,bg="#bbcab7", command= lambda: buttonClicked(text8,button8,1,1) )
    button8.grid(row=1 ,column=1)
    button9  = Button(root,textvariable=text9,text="",width=12,height=5,bg="#e1f1dd", command= lambda: buttonClicked(text9,button9,1,2) )
    button9.grid(row=1 ,column=2) 

    root.mainloop()


