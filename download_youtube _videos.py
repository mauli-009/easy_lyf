from pytube import YouTube
url=input("enter your url:")
yt=YouTube(url)
play=yt.streams.get_lowest_resolution()
play.download()