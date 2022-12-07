from tkinter import *
from tkinter import filedialog
import os
import cv2
from LsbAlgorithim import *
from tkinter import messagebox


####################################################################################################3
def openFile () :
  global Data
  Data=""
  global fileName

  try:
    fileName = filedialog.askopenfilename(initialdir=os.getcwd() , title="Select Text File" )
    
    file=open(fileName , "r")
   
    for line in file :
        Data += line
  except FileNotFoundError :
    messagebox.showerror("Error" , "File Not Exist")



####################################################################################################3



def openCover () :
    global img
    
    try:
        fileName = filedialog.askopenfilename( title="Select Text File" , filetype=(("PNG File" , "*.png") , ("JPG File" , "*.jpg")))
        img = cv2.imread(fileName)
    except FileNotFoundError :
        messagebox.showerror("Error" , "File Not Exist")

    
####################################################################################################3




def GenerateSign () :
    output = filedialog.asksaveasfile(title="Write File Name"  , defaultextension=".txt")
    print(Data)
    output.write(str(LSB.CreateSigniture(Data)))
    output.close()



####################################################################################################3



def VertifySign () :
    Input = filedialog.askopenfile (title="Select File " , defaultextension=".txt" )
    segnValue=str(Input.readline()).strip()
    print("SEGNVALUE" ,type(segnValue))
    global flag 
    flag=LSB.VertifySegn(int (segnValue) ,int ( LSB.CreateSigniture(LSB.showData(StegnoImage))))
    print ("EQUALITY" ,LSB.CreateSigniture(LSB.showData(StegnoImage)) ==segnValue)



####################################################################################################3



def OpenStegno() :
     global StegnoImage
     flag = False
     fileName = filedialog.askopenfilename( title="Select Text File" , filetype=(("PNG File" , "*.png") , ("JPG File" , "*.jpg")))
     StegnoImage = cv2.imread(fileName)
    


####################################################################################################3



def ExtractFile () :
  try :
    if (flag) :
        print("Shape : " , StegnoImage.shape)
        Data = LSB.showData(StegnoImage)
        output = filedialog.asksaveasfile (title="Select ouput location" , defaultextension=".txt")
        output.write(Data)
        output.close()
    else :
            messagebox.showerror("Error !!! " , "Signuture Not Valid !!!")
  except :
            messagebox.showerror("Error !!! " , "Please Vertify the Signiture !!")


####################################################################################################3


def SaveSteg () :
    EncryptImage = LSB.encodeText(img , Data)
    output = filedialog.asksaveasfile (title="Select ouput location")
    cv2.imwrite(str(output.name), EncryptImage)


####################################################################################################3

root = Tk()
root.geometry ("850x500")
root.title("Task One ")
root.configure(bg="#3B8B9F")
Label (root , text="LSB ALGORITHIM" , font="arial 25 bold" , ).place(x=290 , y=10)
Label (root , text="Powered by : Tareq Khanfar" , font="arial 25 bold" , fg="white" , bg="#1B0A4C"  ).place(x=210 , y=150)
Label (root , text="ID :1200265" , font="Rockwell 25 bold" ,bg="red" , fg="white" ).place(x=300 , y=230)


f1= Frame (root , bd=4 , bg="#D361BA" , width=130, height=400 , relief=GROOVE )
f1.place(x=10 , y=70)

f2= Frame (root , bd=4 , bg="#D361BA" , width=130, height=400 , relief=GROOVE )
f2.place(x=700 , y=70)




Button(f2 , text="Open File" , width=12 , height=2 , font= "arial 10 bold" ,command= openFile).place(x=3 , y=6)
Button(f2 , text="Open Cover" , width=12 , height=2 , font= "arial 10 bold", command=openCover ).place(x=3 , y=60)
Button(f2 , text="Save Steg." , width=12 , height=2 , font= "arial 10 bold" , command =SaveSteg ).place(x=3 , y=110)
Button(f1 , text="Open Stegno" , width=12 , height=2 , font= "arial 10 bold", command=OpenStegno ).place(x=3 , y=10)
Button(f1 , text="Extract File" , width=12 , height=2 , font= "arial 10 bold" , command=ExtractFile).place(x=3 , y=80)


Button(f2 , text="Generate Segnuture" , width=15 , height=3 , bg="#020339" , fg="white" , font="arial 10 bold" , command=GenerateSign).place(x=2 , y=180)
Button(f1 , text="Vertify Segnuture" , width=15 , height=3 , bg="red" , fg="white" , font="arial 10 bold" , command=VertifySign).place(x=2 , y=160)

root.mainloop()


####################################################################################################3

    
