from bs4 import BeautifulSoup
import requests


class WebScrape:
    def __init__(self, date):
        self.response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}")
        self.webpage_code = self.response.text
        self.soup = BeautifulSoup(self.webpage_code, "html.parser")
        self.top_100 = [title.getText() for title in self.soup.find_all(name="h3",
                                                                        class_="c-title a-no-trucate "
                                                                               "a-font-primary-bold-s "
                                                                               "u-letter-spacing-0021 "
                                                                               "lrv-u-font-size-18@tablet "
                                                                               "lrv-u-font-size-16 u-line-height-125 "
                                                                               "u-line-height-normal@mobile-max "
                                                                               "a-truncate-ellipsis u-max-width-330 "
                                                                               "u-max-width-230@tablet-only")]
        self.top_100 = [title.replace("\n", "") for title in self.top_100]
        self.top_100 = [title.replace("\t", "") for title in self.top_100]
        self.top_song = self.soup.find(name="a", class_="c-title__link lrv-a-unstyle-link")
        self.top_song = self.top_song.getText().replace("\n", "")
        self.top_song = self.top_song.replace("\t", "")
        self.top_100.insert(0, self.top_song)
        self.artist = [artist.getText() for artist in self.soup.find_all(name="span", class_="a-no-trucate")]
        self.artist = [artist.replace("\n", "") for artist in self.artist]
        self.artist = [artist.replace("\t", "") for artist in self.artist]


