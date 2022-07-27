"""
import time
from tkinter import *
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

service = Service(executable_path=ChromeDriverManager().install())
url = "https://www.azlyrics.com/"
browser = webdriver.Chrome(service=service)
browser.get(url)
search_box = browser.find_element(By.ID, "q")
search_box.send_keys("Ye not crazy")
search_box.submit()
time.sleep(10)
#element_locator = browser.find_element(By.CLASS_NAME, "text-left visitedlyr")
lyric_href = browser.find_element(By.TAG_NAME, "a").get_attribute()
print(lyric_href)
# browser.get(str(lyric_href))
#lyric_href.click()

"""
import requests
from bs4 import BeautifulSoup
from tkinter import *


def search():
    query = lyric_entry.get()
    url = "https://www.lyrics.com/lyrics/" + query

    browser = requests.get(url)
    # print(browser.text)

    soup = BeautifulSoup(browser.text, "html.parser")
    # print(soup.prettify())
    # all_search_results = soup.find_all(class_="sec-lyric clearfix")
    all_search_results = soup.find_all(class_="sec-lyric clearfix")
    # print(all_search_results[0])
    l = []

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
        l.append(dict(title=title, artist=artist, lyric=lyric))
        prev_artist = artist

    song1_label.config(text="Title: " + l[0].get("title"))
    artist1_label.config(text="Artist: " + l[0].get("artist"))
    lyric1_label.config(text="Lyric: \n" + l[0].get("lyric"))

    song2_label.config(text="Title: " + l[1].get("title"))
    artist2_label.config(text="Artist: " + l[1].get("artist"))
    lyric2_label.config(text="Lyric: \n" + l[1].get("lyric"))

    song3_label.config(text="Title: " + l[2].get("title"))
    artist3_label.config(text="Artist: " + l[2].get("artist"))
    lyric3_label.config(text="Lyric: \n" + l[2].get("lyric"))

# Begin process
gui = Tk()
gui.title("Lyric Search")
gui.geometry("1000x800")
gui.config(padx=20, pady=20)
frame_1 = LabelFrame(gui, padx=5, pady=5)
frame_2 = LabelFrame(gui, padx=5, pady=5)
frame_3 = LabelFrame(gui, padx=5, pady=5)

# labels
search_label = Label(text="Search for lyrics: ", padx=5, pady=5)
search_label.pack()

# entries
lyric_entry = Entry(width=30)
lyric_entry.pack(pady=10)

# buttons
search_button = Button(text="Search Song", command=search)
search_button.pack(pady=5)

# result 1
frame_1.pack(pady=10)
result1_label = Label(frame_1, text="Result 1", font="Bold")
result1_label.pack()
song1_label = Label(frame_1, text="Title: ")
song1_label.pack()
artist1_label = Label(frame_1, text="Artist: ")
artist1_label.pack()
lyric1_label = Label(frame_1, text="Lyric: ", padx=5, pady=5)
lyric1_label.pack()

# result 2
frame_2.pack(pady=10)
result2_label = Label(frame_2, text="Result 2", font="Bold")
result2_label.pack()
song2_label = Label(frame_2, text="Title: ")
song2_label.pack()
artist2_label = Label(frame_2, text="Artist: ")
artist2_label.pack()
lyric2_label = Label(frame_2, text="Lyric: ", padx=5, pady=5)
lyric2_label.pack()

# result 3
frame_3.pack(pady=10)
result3_label = Label(frame_3, text="Result 3", font="Bold")
result3_label.pack()
song3_label = Label(frame_3, text="Title: ")
song3_label.pack()
artist3_label = Label(frame_3, text="Artist: ")
artist3_label.pack()
lyric3_label = Label(frame_3, text="Lyric: ", padx=5, pady=5)
lyric3_label.pack()

gui.mainloop()
