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
        
#Generar la ventana
ventana = Tk()
ventana.title("Descargar Cancion")
ventana.geometry("300x700")
ventana.resizable(width=False,height=False)
ventana.config(background="Light Blue")
#Generar el lienzo para pintar componentes
frm = ttk.Frame(ventana, padding=10).pack()
#Componentes Label y button
textoLabel=StringVar()
textoLabel.set("Introduzaca la url")
labelTexto = ttk.Label(frm, textvariable=textoLabel) 
labelTexto.config(background="blue",border=5,font=("Arial",15))
labelTexto.pack()
ttk.Button(frm, text="Salir", command=ventana.destroy).pack()

# Componente
campoTexto=ttk.Entry(frm)
campoTexto.pack()




ttk.Button(frm, text="Salir",command=ventana.destroy).pack()


#
ventana.mainloop()
url="https://www.youtube.com/watch?v=HKNz0DWQXZw&list=PLVwXkzK42QWrWyeunQ_hi4OM8iUrBWUlq"
descargarlista(url)

