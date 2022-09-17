#lightning_dl

import sys, os
import threading
import pytube
from pytube import YouTube

def main():
    txt, type, destination, threads = check_args()
    print(f"TEXT_FILE: {txt}\nFILE_TYPE: {type}\nDESTINATION: {destination}\nMAX_THREADS: {threads}")
    t_amount(txt, threads)
    assign_task(type, destination)

def check_args():
    global destination
    if sys.platform.startswith("linux"):
        usage = f"Usage: python3 {os.path.basename(__file__)} <.txt_FILE> <FILE_TYPE(MP3/MP4)> <DESTINATION> <MAX_THREADS>"
    elif sys.platform.startswith("freebsd"):
        usage = f"Usage: python3 {os.path.basename(__file__)} <.txt_FILE> <FILE_TYPE(MP3/MP4)> <DESTINATION> <MAX_THREADS>"
    else:
        usage = f"Usage: python {os.path.basename(__file__)} <.txt_FILE> <FILE_TYPE(MP3/MP4)> <DESTINATION> <MAX_THREADS>"
    if len(sys.argv) < 2 or len(sys.argv) > 5:
        sys.exit(usage)
    try:
        txt = sys.argv[1]
    except IndexError:
        print("Please Provide a .txt file")
        sys.exit(usage)
    if not txt.endswith(".txt"):
        print("Please only provide a .txt file")
        sys.exit(usage)
    if not os.path.isfile(txt):
        print("The provided text file does not exist")
        sys.exit(usage)
    try:
        type = str(sys.argv[2]).lower()
    except IndexError:
        print("Please provide your prefered file type(MP3/MP4)")
        sys.exit(usage)
    if not type == str("mp3") and not type == str("mp4"):
        print("The file type can only be \"MP3\" or \"MP4\"")
        sys.exit(usage)
    try:
        destination = str(sys.argv[3])
    except IndexError:
        print("Please provide your prefered destination")
        sys.exit(usage)
    try:
        threads = int(sys.argv[4])
    except IndexError:
        print("Please provide your prefered max-thread amount")
        sys.exit(usage)
    return txt, type, destination, threads

def t_amount(txt, threads):
	global f
	global max_t
	max_t = threads
	with open(txt) as f:
		f = f.read().splitlines()
		while "" in f:
			f.remove("")
		if max_t > len(f):
			max_t = len(f)
		else:
			pass

def assign_task(type, destination):
    if type == "mp3":
        if max_t == 0:
            for link in f:
                mp3_dl(link, destination)
        elif max_t < 0:
            sys.exit("Please enter more than one threads")
        elif len(f) == 0:
            sys.exit("The file is empty.")
        else:
            i = 0
            while threading.active_count() < max_t and i != len(f):
                while i < len(f):
                    globals()['t%s' % i] = threading.Thread(target=mp3_dl, args=(str(f[i]), destination, ))
                    globals()['t%s' % i].start()
                    i += 1
            return True
    elif type == "mp4":
        if max_t == 0:
            for link in f:
                mp4_dl(link, destination)
        elif max_t < 0:
            sys.exit("Please enter more than one threads")
        elif len(f) == 0:
            sys.exit("The file is empty.")
        else:
            i = 0
            while threading.active_count() < max_t and i != len(f):
                while i < len(f):
                    globals()['t%s' % i] = threading.Thread(target=mp4_dl, args=(f[i], destination, ))
                    globals()['t%s' % i].start()
                    i += 1
            return True

def mp4_dl(url, destination):
    try:
        yt = YouTube(url)
    except pytube.exceptions.RegexMatchError:
        print(f"{url} is an invalid youtube link")
        return
    file_name = yt.title.translate({ord(i): None for i in '<>:"/\|?*'})
    f = f"{destination}/{file_name}.mp4"
    if os.path.isfile(f):
        print(f"File: {yt.title}.mp4 is already exist in the folder")
    elif not os.path.isfile(f):
        print(f"Downloading Title: {yt.title} Author: {yt.author} URL: {url}")
        yt = yt.streams.get_highest_resolution()
        file = yt.download(output_path=destination)
        os.rename(file, f)
        return True

def mp3_dl(url, destination):
    try:
        yt = YouTube(url)
    except pytube.exceptions.RegexMatchError:
        print(f"{url} is an invalid youtube link")
        return
    file_name = yt.title.translate({ord(i): None for i in '<>:"/\|?*'})
    f = f"{destination}/{file_name}.mp3"
    if os.path.isfile(f):
        print(f"File: {yt.title}.mp3 is already exist in the folder")
    elif not os.path.isfile(f):
        print(f"Downloading Title: {yt.title} Author: {yt.author} URL: {url} ")
        yt = yt.streams.filter(only_audio=True).first()
        file = yt.download(output_path=destination)
        os.rename(file, f)
        return True

if __name__ == "__main__":
    main()