from pytube import YouTube
from pytube import Playlist
from art import *
import os
from youtubesearchpython import VideosSearch
from Lang.lang import *
from PyAppDevKit.LibFunc.pyappdevkit import *
from PyAppDevKit.InfoLib.pyappdevkit_info import *

if not os.path.exists(music_file_txt):
    os.mkdir(music_file_txt)
if not os.path.exists(video_file_txt):
    os.mkdir(video_file_txt)
if not os.path.exists(playlist_file_txt):
    os.mkdir(playlist_file_txt)

def video_download():
    x = YouTube(input(videodownload_link_input_txt))
    stream = x.streams.get_highest_resolution()
    stream.download('Video')
    print(process_started_txt)
    print("-"*50)
    print(process_completed_txt)
    print("{0} {1}".format(x.title, video_file_named_downloaded_msg)) 

def playlist_download():
    playlist = input(playlistdownload_link_input_txt) 
    pl = Playlist(playlist)
    if not os.path.exists("{0}/{1}".format(playlist_file_txt,pl.title)):
        os.makedirs("{0}/{1}".format(playlist_file_txt,pl.title), exist_ok=True)
    print("\n{0} {1}".format(pl.title, playlist_downloading_msg))
    for video in pl.videos:
        print("\n{0} {1}".format(video.title, pl_downloading_video_msg))
        st = video.streams.get_highest_resolution()
        st.download('{0}/{1}'.format(playlist_file_txt,pl.title))
        print("{0} {1}".format(video.title, downloaded_video_file_named_txt))


def audio_download():
    x = YouTube(input(audiodownload_link_input_txt))
    mp3 = x.streams.filter(only_audio=True).first()
    mp3.download(music_file_txt)
    print(process_started_txt)
    print("-"*50)
    print(process_completed_txt)
    print("{0} {1}".format(x.title, audio_downloaded_msg)) 

    output = mp3.download(music_file_txt)
    base, ext = os.path.splitext(output)
    to_mp3 = base + ".mp3"
    os.rename(output, to_mp3)


def video_search():
    c = "--- "
    x = str(input(video_search_input_txt))
    search = VideosSearch(x)
    index = 1
    for video in search.result()['result']:
        print(str(index) + ' - ' + video['title'], str(c) + video['link'], str(c) + video['viewCount']['short'])
        index += 1
        print("-"*65)