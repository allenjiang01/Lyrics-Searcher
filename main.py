from tkinter import *
import _tkinter
import searcher

# VARIABLES
foreground_color = (10, 128, 102)
background_color = (222, 211, 205)


def config_labels(result_list):
    song1_label.config(text="Title: " + result_list[0].get("title"))
    artist1_label.config(text="Artist: " + result_list[0].get("artist"))
    lyric1_label.config(text="Lyric: \n" + result_list[0].get("lyric"))

    song2_label.config(text="Title: " + result_list[1].get("title"))
    artist2_label.config(text="Artist: " + result_list[1].get("artist"))
    lyric2_label.config(text="Lyric: \n" + result_list[1].get("lyric"))

    song3_label.config(text="Title: " + result_list[2].get("title"))
    artist3_label.config(text="Artist: " + result_list[2].get("artist"))
    lyric3_label.config(text="Lyric: \n" + result_list[2].get("lyric"))


def close_program():
    exit()


def make_label(frame, text):
    return Label(frame, text=text, bg=_from_rgb((222, 211, 205)), fg=_from_rgb(foreground_color))


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


# Begin process
gui = Tk()
gui.title("Lyrics Searcher")
gui.geometry("1000x800")
gui.config(padx=20, pady=20, bg=_from_rgb(background_color))
frame_1 = LabelFrame(gui, padx=5, pady=5)
frame_1.config(bg=_from_rgb(background_color))
frame_2 = LabelFrame(gui, padx=5, pady=5)
frame_2.config(bg=_from_rgb(background_color))
frame_3 = LabelFrame(gui, padx=5, pady=5)
frame_3.config(bg=_from_rgb(background_color))

searcher = searcher.Searcher()
# update_var will be used to check if new search is queued
update_var = searcher.update_var

# labels
search_label = Label(text="Search for lyrics: ", font="bold", padx=5, pady=5, bg=_from_rgb(background_color),
                     fg=_from_rgb(foreground_color))
search_label.pack()

# entries
lyric_entry = Entry(width=30)
lyric_entry.pack(pady=10)

# buttons
search_button = Button(text="Search Song", bg=_from_rgb(foreground_color), fg=_from_rgb(background_color),
                       command=lambda: searcher.search(lyric_entry))
search_button.pack(pady=5)

# result 1
frame_1.pack(pady=10)
result1_label = make_label(frame_1, "Result 1")
result1_label.pack()
song1_label = make_label(frame_1, "Title: ")
song1_label.pack()
artist1_label = make_label(frame_1, "Artist: ")
artist1_label.pack()
lyric1_label = Label(frame_1, text="Lyric: ", padx=5, pady=5, bg=_from_rgb(background_color),
                     fg=_from_rgb(foreground_color))
lyric1_label.pack()

# result 2
frame_2.pack(pady=10)
result2_label = make_label(frame_2, "Result 2")
result2_label.pack()
song2_label = make_label(frame_2, "Title: ")
song2_label.pack()
artist2_label = make_label(frame_2, "Artist: ")
artist2_label.pack()
lyric2_label = Label(frame_2, text="Lyric: ", padx=5, pady=5, bg=_from_rgb(background_color),
                     fg=_from_rgb(foreground_color))
lyric2_label.pack()

# result 3
frame_3.pack(pady=10)
result3_label = make_label(frame_3, "Result 3")
result3_label.pack()
song3_label = make_label(frame_3, "Title: ")
song3_label.pack()
artist3_label = make_label(frame_3, "Artist: ")
artist3_label.pack()
lyric3_label = Label(frame_3, text="Lyric: ", padx=5, pady=5, bg=_from_rgb(background_color),
                     fg=_from_rgb(foreground_color))
lyric3_label.pack()

# update results
try:
    while True:
        if searcher.update_var:
            search_results = searcher.result_list
            if len(search_results) >= 3:
                config_labels(search_results)
            searcher.clear()
            searcher.update_var = False
        gui.update_idletasks()
        gui.update()
        gui.protocol('wm_delete_window', close_program)
except _tkinter.TclError:
    print("program closed")



