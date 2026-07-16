import os
import tkinter as tk
from PIL import Image, ImageTk
import copy

#----------------------------------------

class VideoPlayer:

    def __init__(self, root, directory):

        self.root = root
        self.directory = directory

        self.root.title("JABA Video Player")
        self.root.geometry("800x600")
        self.root.configure(bg="black")

        self.label = tk.Label(self.root,bg="black")
        self.label.pack(fill="both",expand=True)

        # procura todos os ficheiros .bmp
        self.files = []

        for f in os.listdir(directory):
            if f.lower().endswith(".bmp"):
                self.files.append(f)

        # ordena 0.bmp,1.bmp,2.bmp,...
        try:
            self.files.sort(
                key=lambda x:int(
                x.replace(".bmp",""))
                )
        except:
            self.files.sort()

        self.counter = 0

        self.play()


    #---------------------------------

    def play(self):

        if len(self.files)==0:
            self.root.after(250,self.play)
            return

        if self.counter>=len(self.files):
            self.counter=0

        filename=os.path.join(
                    self.directory,
                    self.files[self.counter]
                    )

        try:

            image=Image.open(filename)

            # adapta ao tamanho da janela
            image=image.resize(
                (self.root.winfo_width(),
                 self.root.winfo_height())
                 )

            self.photo=ImageTk.PhotoImage(image)

            self.label.configure(
                image=self.photo)

        except:
            pass

        self.counter+=1

        # 250 milisegundos
        self.root.after(250,self.play)


#----------------------------------------




print("\033c\033[47;30m\ngive me the .video pack file ? \n")
a=input().strip()
f1=open(a,"rb")
f=f1.read()
f1.close()
ff=f.split(b"\x01\x00\x05\x04\x03\x07")


ff1=ff[1].split(b"\x01\x00\x05\x04\x03\x02")
if len(ff1)< 2:
    
    if ff1[1]!="JABA":
        printf("this is not a pack file to 1 file")
        exit(1)
names="/tmp/"+ff1[1].decode()

try:
    os.mkdir(names,777)
except:
    pass
os.system("chmod 777 "+names)

counter=0
for d in ff:
    if  counter>1 and d.strip()!="":
        ff1=d.split(b"\x01\x00\x05\x04\x03\x02")
        ff1[0]=ff1[0].decode()  
        f1=open(names+"/"+ff1[0],"bw")
        f1.write(ff1[1])
        f1.close()
    counter=counter+1

counter=0


# directoria onde ficaram os bitmaps
directory=names

root=tk.Tk()

app=VideoPlayer(root,directory)

root.mainloop()


