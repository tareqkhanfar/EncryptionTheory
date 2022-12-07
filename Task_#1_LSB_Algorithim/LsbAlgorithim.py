import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

class LSB :
    @staticmethod
    def messageToBinary (message):
      if (type(message)==str):
        return "".join([format(ord(i) , "08b") for i in message])
      elif (type(message)==bytes or type(message)==np.ndarray):
          return [format (i , "08b") for i in message]
      elif (type(message)==int or type (message) == np.uint8):
        return format (message , "08b")
      else :
        raise TypeError ("Error Message !! ")
#################################################################


    def hideData (image , secret_message) :
       n_bytes = image.shape[0] * image.shape[1] * 3 //8
       print ("Maximum Bytes To Encode : " , n_bytes)

       if (len(secret_message) > n_bytes):
          raise ValueError ("The SIZE of Secret Message is larger than Image size!!")
    

       secret_message += "#####"

       data_index = 0
       binary_Secret_message = LSB.messageToBinary(secret_message)
       data_len = len (binary_Secret_message)

       for values in image :
         for pixel in values :
            r , g , b = LSB.messageToBinary (pixel)
            if (data_index < data_len ) :
                pixel[0]= int(r[:-1]+binary_Secret_message[data_index] , 2)
                data_index+=1
            if (data_index < data_len ) :
                pixel[1]= int(g[:-1]+binary_Secret_message[data_index] , 2)
                data_index+=1
            if (data_index < data_len ) :
                pixel[2]= int(b[:-1]+binary_Secret_message[data_index] , 2)
                data_index+=1
            if (data_index >= data_len):
                break 
    
       return image 

#################################################################################
    def showData (image):
        binary_data = ""
        for values in image :
           for pixel in values :
             r , g, b =  LSB.messageToBinary (pixel)
             binary_data += r[-1]
             binary_data += g[-1]
             binary_data += b[-1]


        all_bytes = [binary_data[i:i+8] for i in range (0 , len (binary_data ) , 8)]
        decoded_data = ""
        for byte in all_bytes :
         decoded_data += chr (int (byte , 2))
         if (decoded_data[-5:] == "#####"):
                break
    
        print (decoded_data)
        return decoded_data[:-5]

################################################################

    @staticmethod
    def encodeText (image , data ) :
        print(data)
        print ("The Shape of Image is : ", image.shape)


        if (len (data) ==0) :
            raise ValueError ("Please Enter Data !")

        encodedImage = LSB.hideData(image , data)
        return encodedImage





##################################################################################
    @staticmethod
    def CreateSigniture (text) :
        NumberOfOnes =0 
        NumberOfZeros =0
        PlainTextInBinary = LSB.messageToBinary(text)
        print(PlainTextInBinary)
        for i in PlainTextInBinary :
            if (i == "1"):
                NumberOfOnes +=1
            else :
                NumberOfZeros+=1
        
        return NumberOfOnes * NumberOfZeros



########################################################################################


    @staticmethod
    def VertifySegn(oldSegn , newSegn) :
        
        return oldSegn == newSegn
    
   
