from colorama import Fore,Back,init
init()
import os.path
enc_dec = input("Enter 1 to encrypt\nEnter 2 to decrypt\n")
if enc_dec == "1": 
   image_loc = input("Enter location of image:")
   image_name = input("Enter image name:")
   image = image_loc+"/"+image_name
   text=input("Enter text to be encrypted only 100 character allowed:")
   j=len(text)
   if os.path.exists(image)==True:
      f = open(image,"rb")
      l = f.read()+text.encode()
      f.close()
      f1 = open("enc.png","wb")
      if j==100:
         f1.write(l)
      if j<100:
         rem = 100-j
         sp = rem*" ".encode()
         l=l+sp
         f1.write(l)
      if j>100:
         print(Fore.RED+"Text can be greater than 100 characters")
      f1.close()      
      print(Fore.GREEN+"Image Encoded successfull New image file is enc.png")
   else:
      print(Fore.RED+"NO SUCH IMAGE EXIST")
if enc_dec=="2":
   image_loc = input("Enter location of image:")
   image_name = input("Enter image name:")
   image = image_loc+"/"+image_name
   if os.path.exists(image)==True:
      k=[]
      f1=open(image,"rb")
      l = f1.read()
      f1.close()
      for i in range(1,101):
          try:
             k.append(chr(l[-i]))
          except:
             print(Fore.RED+"Problem in Encrypted image")
             break
             del k
      k.reverse()
      print(Fore.GREEN+''.join(k))
a=input()
