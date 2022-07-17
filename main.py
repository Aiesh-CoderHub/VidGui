from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil


def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_file():
    get_link = link_field.get()
    user_path = path_label.cget("text")
    screen.title('Downloading...')
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    shutil.move(mp4_video, user_path)
    screen.title('Download Complete! Download Another File...')


if __name__ == "__main__":
    screen = Tk()
    icon = screen.wm_iconbitmap("1.ico")
    title = screen.title('VidGUI')
    canvas = Canvas(screen, width=500, height=500)
    canvas.pack()
    logo_img = PhotoImage(file='yt.png')
    logo_img = logo_img.subsample(5, 5)
    canvas.create_image(250, 80, image=logo_img)
    link_field = Entry(screen, width=40, font=('Arial', 15))
    link_label = Label(screen, text="Enter Download Link: ",
                       font=('Arial', 15))
    path_label = Label(
        screen, text="Select Path For Download", font=('Arial', 15))
    select_btn = Button(screen, text="Select Path", bg='red', padx='22',
                        pady='5', font=('Arial', 15), fg='#fff', command=select_path)
    canvas.create_window(250, 280, window=path_label)
    canvas.create_window(250, 330, window=select_btn)
    canvas.create_window(250, 170, window=link_label)
    canvas.create_window(250, 220, window=link_field)
    download_btn = Button(screen, text="Download File", bg='green', padx='22',
                          pady='5', font=('Arial', 15), fg='#fff', command=download_file)
    canvas.create_window(250, 390, window=download_btn)

    screen.mainloop()
