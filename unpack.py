import os
import tkinter as tk
from PIL import Image, ImageTk
import copy
import zlib
import io
from tkinter import filedialog
#----------------------------------------

class VideoPlayer:

    def __init__(self, root, directory,images):

        self.root = root
        self.directory = directory

        self.root.title(directory+" Video Player")
        self.root.geometry("800x600")
        self.root.configure(bg="black")

        self.label = tk.Label(self.root,bg="black")
        self.label.pack(fill="both",expand=True)

        # procura todos os ficheiros .bmp
        
        self.images=images
        

        self.counter = 0

        self.play()


    #---------------------------------

    def play(self):
        if len(self.images)==0:
            return

        if self.counter>=len(self.images):
             self.counter=0
        

        try:

          
            image=self.images[self.counter]

            image=image.resize(
                (self.root.winfo_width(),
                 self.root.winfo_height())
                 )

            self.photo=ImageTk.PhotoImage(
                    image)

            self.label.configure(
                    image=self.photo)


        except:
            pass

        self.counter+=1

        # 250 milisegundos
        self.root.after(250,self.play)


#----------------------------------------



print("\033c\033[47;30m\ngive me the .video pack file ? \n")

a=filedialog.askopenfile(title="give me the .video pack file ?",defaultextension="*.video")
a=a.name
f1=open(a,"rb")
f=f1.read()
f1.close()
ff=f.split(b"\x01\x00\x05\x04\x03\x07")


ff1=ff[1].split(b"\x01\x00\x05\x04\x03\x02")
if len(ff1)< 2:
    
    if ff1[1]!="JABA":
        printf("this is not a pack file to 1 file")
        exit(1)
directory=ff1[1].decode()

counter=0
images=[]
for d in ff:
    if  counter>2 and d.strip()!="":
        ff1=d.split(b"\x01\x00\x05\x04\x03\x02")
          
        
        
        bmp=zlib.decompress(ff1[1])
        
        image=Image.open(io.BytesIO(bmp))

        

        images.append(image)
    counter=counter+1

counter=0


# directoria onde ficaram os bitmaps

root=tk.Tk()

app=VideoPlayer(root,directory,images)

root.mainloop()


