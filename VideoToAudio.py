# Importing necessary packages
import youtube_dl
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog


def CreateWidgets():
    linkLabel = Label(root, text="YOUTUBE LINK  :", bg="cornsilk4")
    linkLabel.grid(row=1, column=0, pady=5, padx=5)

    root.linkText = Entry(root, width=55, textvariable=videoLink)
    root.linkText.grid(row=1, column=1, pady=5, padx=5)

    destinationLabel = Label(root, text="DESTINATION    :", bg="cornsilk4")
    destinationLabel.grid(row=2, column=0, pady=5, padx=5)

    root.destinationText = Entry(root, width=55, textvariable=downloadPath)
    root.destinationText.grid(row=2, column=1, pady=5, padx=5)

    browseButton = Button(root, text="BROWSE", command=Browse, width=15)
    browseButton.grid(row=2, column=2, pady=5, padx=5)

    downloadButton = Button(root, text="DOWNLOAD AUDIO", command=Download, width=15)
    downloadButton.grid(row=3, column=1, pady=5, padx=5)


def Browse():
    downloadDirectory = filedialog.askdirectory(initialdir="/Users/Gaurav/Music")
    downloadPath.set(downloadDirectory)

def Download():
    youtube_link = videoLink.get()
    downloadFolder = downloadPath.get()

    audDWLDopt = {
        # Specifying to download audio in best format
        'format':'bestaudio/best',
        # Destination to save the audio file with the title as the name
        'outtmpl': downloadFolder+"/%(title)s.%(ext)s",
        # Converting video to audio
        'postprocessors':[{
            # Extracting audio from the video
            'key':'FFmpegExtractAudio',
            # Format for saving the audio (mp3, wav)
            'preferredcodec': 'mp3',
            # Quality of the audio (Audio BitRate)
            'preferredquality': '320'
        }],
    }

    with youtube_dl.YoutubeDL(audDWLDopt) as aud_dwld:
        aud_dwld.download([youtube_link])

    # Displaying the message
    messagebox.showinfo("YOUR YOUTUBE VIDEO CONVERTED AND DOWNLOAD AS A AUDIO SUCCESSFULLY")

root = tk.Tk()

root.geometry("655x200")
root.resizable(False, False)
root.title("Youtube_Audio_Downloader")
root.config(background="cornsilk4")

videoLink = StringVar()
downloadPath = StringVar()

CreateWidgets()

root.mainloop()