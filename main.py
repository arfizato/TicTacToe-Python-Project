from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
""" GREAT COLOR PALETTES :https://imgur.com/Jmk6LEH """


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
    global x, numOfButtonsDisabled, stopPlaying, firstChar, secondChar, playerOneWins, playerTwoWins
    x+=1
    atLeastOnePlayerWon=FALSE

    choiceButton["state"]= DISABLED
    choiceButton["bg"]="#404040"
    choiceButton["fg"]="#000000"

    button["state"]= DISABLED
    if (x%2==0):   
        #only changes color if the player chooses the "only color" option before he starts playing
        if (firstChar==""):     
            button["bg"]="#dbf9db"
            #button["relief"]= "sunken"
        

        text.set(firstChar)
        mat[l-1][c]=firstChar 
        if checkForWin(mat,l-1,c,firstChar):
            playerTwoWins+=1
            atLeastOnePlayerWon= TRUE
            box = messagebox.askquestion("Player 2 Won", "\tSCORE:  "+str(playerOneWins)+" - "+str(playerTwoWins)+"\nWould You Like To Keep Playing?",icon = 'question')
            if (box !='yes'):
                stopPlaying=TRUE         
            root.destroy()      
    else:
        #only changes color if the player chooses the "only color" option before he starts playing
        if (firstChar ==""):
            button["bg"]="#c8eed9"
            #button["relief"]= "sunken"

        text.set(secondChar)
        mat[l-1][c]=secondChar
        if checkForWin(mat,l-1,c,secondChar):
            playerOneWins+=1
            atLeastOnePlayerWon= TRUE
            box=messagebox.askquestion("Player 1 Won","\tSCORE:  "+str(playerOneWins)+" - "+str(playerTwoWins)+"\nWould You Like To Keep Playing?",icon = 'question')
            if (box!='yes'):
                stopPlaying=TRUE          
            root.destroy()  

    numOfButtonsDisabled+=1
    if numOfButtonsDisabled==9 and atLeastOnePlayerWon == FALSE:
        box=messagebox.askquestion("It's a TIE ", "\tSCORE:  "+str(playerOneWins)+" - "+str(playerTwoWins)+"\nWould You Like To Keep Playing?",icon = 'question')
        if (box!='yes'):
            stopPlaying=TRUE
        root.destroy()

#picking what to fill the buttons with
def changeText(text,button):
    global firstChar, secondChar, charList, charNumber
    charNumber= charNumber+1 if charNumber<4 else 0
    firstChar=charList[charNumber][0] 
    secondChar=charList[charNumber][1]
    text.set(charList[charNumber][2])   


"""--------------------------Main--------------------------"""    
global stopPlaying, playerOneWins, playerTwoWins
stopPlaying=FALSE
playerTwoWins=0
playerOneWins=0
while (stopPlaying==FALSE):
    
    charNumber=0
    charList=[["O","X","X O"],["+","-","- +"],["B","A","A B"],["Y","X","X Y"],[""," ","Only Color"]]
    mat=[["."]*3,["."]*3,["."]*3]
    numOfButtonsDisabled=0
        
    root = tk.Tk()
    root.title("Tic Tac toe")
    root.iconbitmap(r'images/TicTacToe.ico')
    # define font
    myFontChoice = font.Font(family='Times',weight="bold",slant="italic")
    myFont = font.Font(family='Times',weight="bold")
    #myFont = font.Font(family=)

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
    choiceButton  = Button(root,textvariable=text0,width=38,height=5,fg="#323831",bg="#bbcab7", command= lambda: changeText(text0,choiceButton))
    choiceButton.grid(row=0 ,column=0, columnspan=3)
    choiceButton["font"]= myFontChoice

    button1  = Button(root,textvariable=text1,text="",width=12,height=5,bg="#e1f1dd", command= lambda: buttonClicked(text1,button1,3,0) )
    button1.grid(row=3 ,column=0)
    button1["font"]= myFont
    button2  = Button(root,textvariable=text2,text="",width=12,height=5,bg="#bbcab7", command= lambda: buttonClicked(text2,button2,3,1) )
    button2.grid(row=3 ,column=1)
    button2["font"]= myFont
    button3  = Button(root,textvariable=text3,text="",width=12,height=5,bg="#e1f1dd", command= lambda: buttonClicked(text3,button3,3,2) )
    button3.grid(row=3 ,column=2)
    button3["font"]= myFont

    button4  = Button(root,textvariable=text4,text="",width=12,height=5,bg="#bbcab7", command= lambda: buttonClicked(text4,button4,2,0) )
    button4.grid(row=2 ,column=0)
    button4["font"]= myFont
    button5  = Button(root,textvariable=text5,text="",width=12,height=5,bg="#e1f1dd", command= lambda: buttonClicked(text5,button5,2,1) )
    button5.grid(row=2 ,column=1)
    button5["font"]= myFont
    button6  = Button(root,textvariable=text6,text="",width=12,height=5,bg="#bbcab7", command= lambda: buttonClicked(text6,button6,2,2) )
    button6.grid(row=2 ,column=2)
    button6["font"]= myFont

    button7  = Button(root,textvariable=text7,text="",width=12,height=5,bg="#e1f1dd", command= lambda: buttonClicked(text7,button7,1,0) )
    button7.grid(row=1 ,column=0)
    button7["font"]= myFont
    button8  = Button(root,textvariable=text8,text="",width=12,height=5,bg="#bbcab7", command= lambda: buttonClicked(text8,button8,1,1) )
    button8.grid(row=1 ,column=1)
    button8["font"]= myFont
    button9  = Button(root,textvariable=text9,text="",width=12,height=5,bg="#e1f1dd", command= lambda: buttonClicked(text9,button9,1,2) )
    button9.grid(row=1 ,column=2) 
    button9["font"]= myFont

    root.mainloop()


