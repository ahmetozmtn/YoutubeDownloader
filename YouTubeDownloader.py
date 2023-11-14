from pytube import YouTube
from pytube import Playlist
from art import *
import os
from youtubesearchpython import VideosSearch

lang=str(input('Which language (English or Turkish)?: '))

if lang=="EN" or lang=="English":
    if not os.path.exists("Music"):
        os.mkdir("Music")
    if not os.path.exists("Video"):
        os.mkdir("Video")
    if not os.path.exists("Playlist"):
        os.mkdir("Playlist")

    def video_download():
        x = YouTube(input("Please Paste the Video Link you want to download: "))
        stream = x.streams.get_highest_resolution()
        stream.download('Video')
        print("Download Process Started...")
        print("-"*50)
        print("Download Completed.")
        print("{} Video File Named Downloaded".format(x.title)) 

    def playlist_download():
        playlist = input("Enter Playlist Link: ") 
        pl = Playlist(playlist)
        if not os.path.exists("Playlist/{}".format(pl.title)):
            os.makedirs("Playlist/{}".format(pl.title), exist_ok=True)
        print("\n{} Downloading Playlist Named...".format(pl.title))
        for video in pl.videos:
            print("\n{} Downloading Video File Named...".format(video.title))
            st = video.streams.get_highest_resolution()
            st.download('Playlist/{}'.format(pl.title))
            print("{} Downloaded Video File Named.".format(video.title))


    def audio_download():
        x = YouTube(input("Please Paste the Audio Link you want to download: "))
        mp3 = x.streams.filter(only_audio=True).first()
        mp3.download('Music')
        print("Download Process Started...")
        print("-"*50)
        print("Download Completed.")
        print("{} Audio File Named Downloaded".format(x.title)) 

        output = mp3.download('Music')
        base, ext = os.path.splitext(output)
        to_mp3 = base + ".mp3"
        os.rename(output, to_mp3)


    def video_search():
        c = "--- "
        x = str(input("Type the name of the Video you want to search: "))
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
    2-Music
    3-Playlist
    4-Video Search
    0-Exit""")
        choose = input("\nPlease Make Your Choice: ") 

        if choose == "1":
            video_download()

        elif choose == "2":
            audio_download()

        elif choose == "3":
            playlist_download()

        elif choose == "4":
            video_search()

        elif choose == "0":
            exit()

elif lang=="TR" or lang=="Türkçe":
    if not os.path.exists("Müzik"):
        os.mkdir("Müzik")
    if not os.path.exists("Video"):
        os.mkdir("Video")
    if not os.path.exists("Playlist"):
        os.mkdir("Playlist")

    def video_indir():
        x = YouTube(input("Lütfen İndirmek İstediğiniz Video Bağlantısını Yapıştırın: "))
        stream = x.streams.get_highest_resolution()
        stream.download('Video')
        print("İndirme İşlemi Başlatıldı...")
        print("-"*50)
        print("İndirme tamamlandı.")
        print("{} Adlı video indirilmiştir.".format(x.title)) 

    def playlist_indir():
        playlist = input("Playist linki giriniz: ") 
        pl = Playlist(playlist)
        if not os.path.exists("Playlist/{}".format(pl.title)):
            os.makedirs("Playlist/{}".format(pl.title), exist_ok=True)
        print("\n{} Adlı Playist indiriliyor...".format(pl.title))
        for video in pl.videos:
            print("\n{} Adlı video indirilmiştir...".format(video.title))
            st = video.streams.get_highest_resolution()
            st.download('Playlist/{}'.format(pl.title))
            print("{} Adlı video indirilmiştir.".format(video.title))


    def ses_indir():
        x = YouTube(input("Lütfen indirmek istediğiniz Ses Bağlantısını Yapıştırın: "))
        mp3 = x.streams.filter(only_audio=True).first()
        mp3.download('Müzik')
        print("İndirme işlemi başlatılmıştır...")
        print("-"*50)
        print("İndirme tamamlanmıştır.")
        print("{} Adlı ses dosyası indirilmiştir".format(x.title)) 

        output = mp3.download('Müzik')
        base, ext = os.path.splitext(output)
        to_mp3 = base + ".mp3"
        os.rename(output, to_mp3)


    def video_arama():
        c = "--- "
        x = str(input("Aramak istediğiniz Videonun adını yazın: "))
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
        secim = input("\nLütfen seçim yapınız: ") 

        if secim == "1":
            video_indir()

        elif secim == "2":
            ses_indir()

        elif secim == "3":
            playlist_indir()

        elif secim == "4":
            video_indir()

        elif secim == "0":
            exit()
else:
    print("Invalid YoutubeDownloader argument...")