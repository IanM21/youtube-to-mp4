from pytube import YouTube
while True:
    def YT_download():
        url = input("Enter the url of the video: ")
        yt = YouTube(url)
        yt.streams.filter(res='720p').first().download('./Youtube')
        print("Download Successful for {}".format(url))
        print("\n")  
    YT_download()