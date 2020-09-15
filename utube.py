from pytube import YouTube	#module for downloading youtube video
from tkinter import *		#module making Graphical User Interface
import tkinter as tk
import tkinter.messagebox
import time


window=tk.Tk()
window.title('YouTube Downloader!!')
frame=Frame(window,width=800,height=600,background='pink')
frame.pack()
pixel=['240p']
flg=0
def start_download():
    link =entry1.get() #take link as input
    if len(link)==0:#check whether link filed is entered or not
        entry1.focus()
        flg=0
        return

    resolution_disp.delete('1.0',END)

    if len(entry2.get())==0:#take directory path to which video needs to be downloaded
        entry2.focus()
        return


    try:
        yt = YouTube(link)#establishing connection with youtube
    except:
        resolution_disp.insert(tk.END,"Connection Error")#if there is network or connection problem of internet


    mp4files = yt.filter('mp4')#filtering only mp4 videos

    i=0
    for _ in mp4files:#display available video qualities
        tmp = str(_)
        resolution_disp.insert(tk.END,str(i)+"\t"+tmp[22:27])
        resolution_disp.insert(tk.END,'\n')
        i+=1
        flg=1
    if len(entry3.get())==0:#enter desired resolution(quality)
        entry3.focus()
        return

    n=int(entry3.get())

    d_video = yt.get(mp4files[n - 1].extension, mp4files[n - 1].resolution)#getting specified quality video
    d_video.download(entry2.get())#downloading to specified directory

    tkinter.messagebox.showinfo('Sucessfully Downloded!!')
	#clear all the entries
    entry1.delete(0,'end')
    entry3.delete(0,'end')
    resolution_disp.delete('1.0',END)

    return

#labels
label1=tk.Label(text='Enter URL',fg='red',font=('verdana italic',12))
label1.place(x=10,y=10)
label2=tk.Label(text='Enter Directory path:',fg='red',font=('verdana italic',12))
label2.place(x=10,y=100)
label3=tk.Label(text='Available Resolutions',fg='red',font=('verdana italic',12))
label3.place(x=10,y=200)
label4=tk.Label(text='Resolution you want',fg='red',font=('verdana',12))
label4.place(x=10,y=450)

#entries for taking user input

entry1=tk.Entry()#for youtube video link input
entry1.place(x=300,y=10,height=25,width=350)

entry2=tk.Entry()#for taking specified directory path to which video needs to be downloaded
entry2.place(x=300,y=100,height=25,width=350)

entry3=tk.Entry()#for taking desired resolution input
entry3.place(x=300,y=450,height=25,width=350)

#Displaying text on the screen
resolution_disp=tk.Text(master=window)
resolution_disp.place(x=300,y=200,height=200,width=350)


#Button to start downloading
button_start_downloding=tk.Button(text='Start Downloading',command=start_download,fg='red',font=('verdana',12))
button_start_downloding.place(x=250,y=530)
#FOR BUUTONS

mainloop()
#for only lower resolution
