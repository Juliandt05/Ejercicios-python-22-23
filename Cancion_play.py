from pytube import YouTube
from pytube import Playlist
from tkinter import *
from tkinter import ttk
def descargarCancion(url:str):
    youtube= YouTube(url)
    print(youtube.author)
    print("Descargando", youtube.title)
    cancion= youtube.streams.get_audio_only()
    cancion.download

def descargarlista (url:str):
    playlist= Playlist(url)
    for cancion in  playlist.videos:
        print("Descargando cancion: ",cancion.title)
        cancion.streams.get_audio_only().download("Canciones")
        print("******************\n")
        
ventana = Tk()
ventana.title("Descargar Canción")
ventana.geometry("600x200")
ventana.resizable(width=False,height=False)
ventana.config(background="snow3")


datos_entrada = ttk.Entry(ventana)
datos_entrada.place(x=215,y=100)


boton_descargar=ttk.Button(ventana,text="Descargar cación",command=descargarCancion)
boton_descargar.place(x=235,y=150)

label_titulo=ttk.Label(ventana,text="Introduzca la url de youtube de la canción")
label_titulo.config(background="snow3")
label_titulo.place(x=165,y=50)


ventana.mainloop()