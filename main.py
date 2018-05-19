import youtube_dl
import pycurl
import os


def download_audio(path, audio_url, ext, title):
    path = os.path.join(path, ".".join([title, ext]))
    with open(path, 'wb') as audio_file:
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, audio_url)
        curl.setopt(pycurl.WRITEDATA, audio_file)
        curl.perform()
        curl.close()
        audio_file.close()


ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})

path = input("where do you want to save audio: ")
with open('urls', 'r') as urls:
    for line in urls.readlines():
        url, title = line.split(" && ")

        result = ydl.extract_info(
            url,
            download=False
        )

        if 'entries' not in result:
            video = result

            for item in video["formats"]:
                if item["ext"] in ['m4a', 'mp3', 'acc']:
                    audio_url = item['url']
                    ext = item['ext']
                    download_audio(path, audio_url, ext, title)
