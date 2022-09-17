from pytube import YouTube
from pytube import Playlist
from art import *
import os
from youtubesearchpython import VideosSearch


if not os.path.exists("Müzik"):
    os.mkdir("Müzik")
if not os.path.exists("Video"):
    os.mkdir("Video")
if not os.path.exists("Playlist"):
    os.mkdir("Playlist")

def video_indir():
    x = YouTube(input("Lütfen Linkinizi Yapıştırın: "))
    stream = x.streams.get_highest_resolution()
    stream.download('Video')
    print("İndirme İşlemi Başladı...")
    print("-"*50)
    print("İndirme İşlemi Tamamlandı.")
    print("{} Adlı Video Dosyası İndirildi".format(x.title)) 

def playlist_indir():
    playlist = input("Playlist Linkini Girin: ") 
    pl = Playlist(playlist)
    if not os.path.exists("Playlist/{}".format(pl.title)):
        os.makedirs("Playlist/{}".format(pl.title), exist_ok=True)
    print("\n{} Adlı Oynatma Listesi İndiriliyor...".format(pl.title))
    for video in pl.videos:
        print("\n{} Adlı Video Dosyası İndiriyor...".format(video.title))
        st = video.streams.get_highest_resolution()
        st.download('Playlist/{}'.format(pl.title))
        print("{} Adlı Video Dosyası İndiridi.".format(video.title))


def ses_indir():
    x = YouTube(input("Lütfen Linkinizi Yapıştırın: "))
    mp3 = x.streams.filter(only_audio=True).first()
    mp3.download('Müzik')
    print("İndirme İşlemi Başladı...")
    print("-"*50)
    print("İndirme İşlemi Tamamlandı.")
    print("{} Adlı Ses Dosyası İndirildi".format(x.title)) 

    output = mp3.download('Müzik')
    base, ext = os.path.splitext(output)
    to_mp3 = base + ".mp3"
    os.rename(output, to_mp3)


def video_arama():
    c = "--- "
    x = str(input("Aramak İstediğiniz Kelimeyi Yazın: "))
    search = VideosSearch(x)
    index = 1
    for video in search.result()['result']:
        print(str(index) + ' - ' + video['title'], str(c) + video['link'], str(c) + video['viewCount']['short'])
        index += 1
        print("-"*65)

while True:
    #print("-YouTube Video İndirici-","-"*50,"\n\t01-Video\n\t2-Müzik\n\t3-Playlist\n\t4-Video Arama\n\t0-Çıkış")

    tprint("YT-DL")
    print("""
-----------------------------------------------------------------------
    1-Video
    2-Müzik
    3-Playlist
    4-Video Arama
    0-Çıkış""")
    secim_yap = input("\nLütfen Seçim Yapınız: ") 

    if secim_yap == "1":
        video_indir()

    elif secim_yap == "2":
        ses_indir()

    elif secim_yap == "3":
        playlist_indir()

    elif secim_yap == "4":
        video_arama()

    elif secim_yap == "0":
        break

