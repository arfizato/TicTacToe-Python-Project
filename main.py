from tkinter import *
import tkinter as tk
from tkinter import messagebox
import tkinter.font as font
""" GREAT COLOR PALETTES :https://imgur.com/Jmk6LEH """


# checking if one of the players won 
def checkForWin(mat,l,c,xo):
        
    prevl=l-1 if l>0 else 2
    prevc=c-1 if c>0 else 2
    nextl=l+1 if l<2 else 0
    nextc=c+1 if c<2 else 0

    # checking main diagonal
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
            button["bg"]="#feecaa"
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
            #Color Combinations pink and pastel(bb8082,f6dfeb)  white and gray(ffffff,353535) brown and gray(897853,353535) pastel purple and pink(f6dfeb,dbd0ff) red and black(630000,1b1717)
            button["bg"]="#decc8c"
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

    #in case of numOfButtonsDisabled==9 then we know it's a draw unless someone won with the last button click 
    numOfButtonsDisabled+=1
    if numOfButtonsDisabled==9 and atLeastOnePlayerWon == FALSE:
        box=messagebox.askquestion("It's a TIE ", "\tSCORE:  "+str(playerOneWins)+" - "+str(playerTwoWins)+"\nWould You Like To Keep Playing?",icon = 'question')
        if (box!='yes'):
            stopPlaying=TRUE
        root.destroy()

#picking what to fill the buttons with
def changeText(text,button):
    global firstChar, secondChar, charList, charNumber
    charNumber= charNumber+1 if charNumber<4 else 0 #charNumber is the variables traversing the charList[][] 
    firstChar=charList[charNumber][0] 
    secondChar=charList[charNumber][1]
    text.set(charList[charNumber][2])   

def onClose():
    global stopPlaying
    stopPlaying=TRUE
    root.destroy()

"""--------------------------Main--------------------------"""    
global stopPlaying, playerOneWins, playerTwoWins
stopPlaying=FALSE #boolean deciding when to stop the while loop: only becomes true if the player clicks no on the popup 
playerTwoWins=0 #tracking how many times player 1 won 
playerOneWins=0#tracking how many times player 2 won
while (stopPlaying==FALSE):
    
    charNumber=0#variable selecing the subarrays containing the preferred symbols
    charList=[["O","X","X O"],["+","-","- +"],["B","A","A B"],["Y","X","X Y"],[""," ","Only Color"]] # list of preferred symbols ("X O","A B", etc...) the user has to pick from
    mat=[["."]*3,["."]*3,["."]*3] # matrix keeping count of who marked where 
    numOfButtonsDisabled=0 # tracking if there's a draw or not 
        
    root = tk.Tk()
    root.title("Tic Tac toe")
    root.iconbitmap(r'images/TicTacToe.ico')
    root.configure(bg="#c7dabf")
    root.protocol('WM_DELETE_WINDOW', onClose)
    
    # define font
    myFontChoice = font.Font(family='Times',weight="bold",slant="italic")
    myFont = font.Font(family='Times',weight="bold")


    global x, firstChar, secondChar
    firstChar="O"
    secondChar="X"    
    x=0 

    """------------------------------------Defining each button and putting it on the grid------------------------------------"""
    #choiceButton is the button the user has to click on to pick preferred symbols "X O","A B", etc...
    
    text0  = tk.StringVar()
    text0.set("Click To Pick Variant")
    choiceButton  = Button(root,bd=0,textvariable=text0,width=38,height=5,fg="#323831",bg="#a3b996", command= lambda: changeText(text0,choiceButton))
    choiceButton.grid(padx=1,pady=1,row=0 ,column=0, columnspan=3)
    choiceButton["font"]= myFontChoice

    #Row of [1,2,3]
    text1  = tk.StringVar()
    button1  = Button(root,bd=0,textvariable=text1,text="",width=12,height=5,bg="#bbca95", command= lambda: buttonClicked(text1,button1,3,0) )
    button1.grid(padx=2,pady=1,row=3 ,column=0)
    button1["font"]= myFont

    text2  = tk.StringVar()
    button2  = Button(root,bd=0,textvariable=text2,text="",width=12,height=5,bg="#a3b996", command= lambda: buttonClicked(text2,button2,3,1) )
    button2.grid(padx=1,pady=1,row=3 ,column=1)
    button2["font"]= myFont

    text3  = tk.StringVar()
    button3  = Button(root,bd=0,textvariable=text3,text="",width=12,height=5,bg="#bbca95", command= lambda: buttonClicked(text3,button3,3,2) )
    button3.grid(padx=2,pady=1,row=3 ,column=2)
    button3["font"]= myFont

    #Row of [4,5,6]
    text4  = tk.StringVar()
    button4  = Button(root,bd=0,textvariable=text4,text="",width=12,height=5,bg="#a3b996", command= lambda: buttonClicked(text4,button4,2,0) )
    button4.grid(padx=2,pady=1,row=2 ,column=0)
    button4["font"]= myFont

    text5  = tk.StringVar()
    button5  = Button(root,bd=0,textvariable=text5,text="",width=12,height=5,bg="#bbca95", command= lambda: buttonClicked(text5,button5,2,1) )
    button5.grid(padx=1,pady=1,row=2 ,column=1)
    button5["font"]= myFont

    text6  = tk.StringVar()
    button6  = Button(root,bd=0,textvariable=text6,text="",width=12,height=5,bg="#a3b996", command= lambda: buttonClicked(text6,button6,2,2) )
    button6.grid(padx=2,pady=1,row=2 ,column=2)
    button6["font"]= myFont

    #Row of [7,8,9]
    text7  = tk.StringVar()
    button7  = Button(root,bd=0,textvariable=text7,text="",width=12,height=5,bg="#bbca95", command= lambda: buttonClicked(text7,button7,1,0) )
    button7.grid(padx=2,pady=1,row=1 ,column=0)
    button7["font"]= myFont

    text8  = tk.StringVar()
    button8  = Button(root,bd=0,textvariable=text8,text="",width=12,height=5,bg="#a3b996", command= lambda: buttonClicked(text8,button8,1,1) )
    button8.grid(padx=1,pady=1,row=1 ,column=1)
    button8["font"]= myFont

    text9  = tk.StringVar()
    button9  = Button(root,bd=0,textvariable=text9,text="",width=12,height=5,bg="#bbca95", command= lambda: buttonClicked(text9,button9,1,2) )
    button9.grid(padx=2,pady=1,row=1 ,column=2) 
    button9["font"]= myFont


    root.mainloop()
