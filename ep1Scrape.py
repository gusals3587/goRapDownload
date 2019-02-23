from __future__ import unicode_literals
import youtube_dl
from requests import get
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

def main():
    ids = get_playlist_info("https://tv.naver.com/v/5416674/list/314113")
    ydl_opts = {}
    ids = ids[7:]
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(ids)

def get_playlist_info(link):
    resp = get(link)
    html = BeautifulSoup(resp.content, 'html.parser')
    ids = []
    for li in html.select('li'):
        try:
            if "_rec_playlist" in li.get('class'):
                ids.append("https://tv.naver.com/v/" + li['data-clipno'])
        except:
            pass
    return ids

if __name__ == "__main__":
    main()
    

