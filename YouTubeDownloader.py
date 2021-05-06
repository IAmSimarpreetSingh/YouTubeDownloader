from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube

FileLocation = ''


def SelectFileLocation():
    global FileLocation
    FileLocation = filedialog.askdirectory()

    if len(FileLocation) > 1:
        LocationLabel.config(text=FileLocation, fg='green', font=('Ubuntu', 12, 'bold'), bg='white')

    else:
        messagebox.showerror(title='Location i not selected', message='Try again! select valid location', fg='red')


def VideoDownload():
    TheQuality = YtQualityChoice.get()
    TheUrl = UrlEntry.get()

    if len(TheUrl) > 1:
        Yt = YouTube(TheUrl)

        if TheQuality == QualityChoices[0]:
            Select = Yt.streams.filter(progressive=True, file_extension='mp4').last()

        elif TheQuality == QualityChoices[1]:
            Select = Yt.streams.filter(progressive=True, file_extension='mp4').first()
            

        elif TheQuality == QualityChoices[2]:
            Select = Yt.streams.filter(only_video=True, file_extension='mp4').first()

        elif TheQuality == QualityChoices[3]:
            Select = Yt.streams.filter(only_audio=True).first()

        else:
            messagebox.showerror(title='Download Error', message='There is an error while downloading', fg='red')

    Select.download(FileLocation)
    LocationLabel.config(text='Completed!')


window = Tk()
window.geometry('360x480')
window.title('IAmSimarpreet')
window.resizable(0, 0)

frame_1 = Frame(window, width=1000, height=60, bg='cadet blue', bd=20)
frame_1.pack(fill=X)
frame_2 = Frame(window, width=1000, height=460, bg='white', bd=20)
frame_2.pack(fill=X)
frame_3 = Frame(window, width=1000, height=40, bg='cadet blue', bd=20)
frame_3.pack(fill=X)

TitleLabel = Label(frame_1, text='YouTube Video Downloader', fg='black', font=('Ubuntu', 16, 'bold'))
TitleLabel.pack()

UrlLabel = Label(frame_2, text='Enter video URL below', fg='green', font=('serif', 14, 'bold'), bg='white')
UrlLabel.pack()
UrlEntryVar = StringVar()
UrlEntry = Entry(frame_2, textvariable=UrlEntryVar, width=50)
UrlEntry.pack(pady=20)

LocationLabel = Label(frame_2, text='Your Location', fg='green', font=('Ubuntu', 12, 'bold'), bg='white')
LocationLabel.pack(pady=5)
ChooseLocationButton = Button(frame_2, text='Choose Location', width=20, command=SelectFileLocation)
ChooseLocationButton.pack(pady=5)

QualityLabel = Label(frame_2, text='Choose Video Quality', fg='green', font=('Ubuntu', 12, 'bold'), bg='white')
QualityLabel.pack(pady=20)
QualityChoices = ['Highest Quality', 'Low Quality', 'Video Only', 'Audio Only']
YtQualityChoice = ttk.Combobox(frame_2, values=QualityChoices)
YtQualityChoice.pack()

VideoDownloadButton = Button(frame_2, text='Download Now', width=20, command=VideoDownload)
VideoDownloadButton.pack(pady=30)

window.mainloop()
