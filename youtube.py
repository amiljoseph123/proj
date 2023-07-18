from pytube import YouTube
url = input("Enter a youtube video link :")
to_download = YouTube(url)

title = to_download.title
print( "Video Title - " + title)

videos = to_download.streams #.all()
print(videos)

vid = list(enumerate(videos))
for i in vid:
    print(i)
    print()

stream = int(input("Enter your desired qualty to download : "))
videos[stream].download()

print(title + " Downloaded Successfully")
