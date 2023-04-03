import os
import youtube_dl

while True:
    link = input("Enter YouTube video link (or 'q' to quit): ")
    if link == 'q':
        print("Thanks for using my script. Goodbye!")
        break
    
    ydl_opts = {
        'outtmpl': 'yt-downloads/%(title)s.%(ext)s',
        'format': 'best'
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        try:
            info_dict = ydl.extract_info(link, download=True)
            video_title = info_dict.get('title', None)
            print(f"Successfully downloaded {video_title}")
        except youtube_dl.utils.DownloadError as e:
            print(f"Unable to download video: {str(e)}")
