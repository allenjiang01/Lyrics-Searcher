import requests
from bs4 import BeautifulSoup


class Searcher:
    def __init__(self):
        self.result_list = []
        self.update_var = False

    def search(self, entry):
        query = entry.get()
        url = "https://www.lyrics.com/lyrics/" + query

        browser = requests.get(url)

        soup = BeautifulSoup(browser.text, "html.parser")
        all_search_results = soup.find_all(class_="sec-lyric clearfix")

        prev_artist = ""
        for song in all_search_results:
            title = song.find(class_="lyric-meta-title").getText()
            if song.find(class_="lyric-meta-album-artist"):
                artist = song.find(class_="lyric-meta-album-artist").getText()
            else:
                artist = song.find(class_="lyric-meta-artists").getText()
            if artist == prev_artist:
                continue
            lyric = song.find(class_="lyric-body").getText()
            lyric = lyric.replace("\r", "")
            self.result_list.append(dict(title=title, artist=artist, lyric=lyric))
            prev_artist = artist

        self.update_var = True
        return self.result_list

    def clear(self):
        self.result_list = []