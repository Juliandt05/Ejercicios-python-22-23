from pytube import YouTube
from pytube import Playlist
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
        

url="https://www.youtube.com/watch?v=HKNz0DWQXZw&list=PLVwXkzK42QWrWyeunQ_hi4OM8iUrBWUlq"
descargarlista(url)

