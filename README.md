# **lightning_dl**
lightning_dl is a youtube video downloader which downloads youtube videoes as mp3/mp4.
This is made for when you want to save some youtube videoes for when you're offline. Weather going on a road trip, a flights, camping or whatever occasion, you can get things ready before going out with no internet.
This program is accelerated by using threads. (You can choose not to use it too if you don't want to use much resource from your computer.)
All you have to do is put your video links in a text file and run this program, and lighting_dl will download your videoes all at once.

## **Preparation:**
In command promt/Terminal, direct in to the folder of your choice, clone the repository, unzip it then direct in to the unzipped folder and run the command as follow;
### Windows:
```console
$ pip install -r requirements.txt
```
### Linux:
```console
$ pip3 install -r requirements.txt
```
## **Usage:**
In the program's folder, run the following command;
### Windows:
```console
$ python project.py <.txt_FILE> <FILE_TYPE(MP3/MP4)> <DESTINATION> <MAX_THREADS>
```
### Linux:
```console
$ python3 project.py <.txt_FILE> <FILE_TYPE(MP3/MP4)> <DESTINATION> <MAX_THREADS>
```
If you don't want to use threads you can put `0` in the <MAX_THREADS> argument.

## **Video:**
https://youtu.be/hxaPTvnoaY4
In this video, I'm explaining about the program, usage and demo of threading speed compared to no threads.
I use a program called "ptime" to measure the program's execution time.
If you have any question about this program, feel free to ask me in the comment.
And if there's any mistake or misunderstanding in the code, I'd be pleased to know that. You can tell me in the comment as well.
I'm new to threading so I still need to know some more things about it.

## **Credit:**
This program uses a library called [pytube](https://pypi.org/project/pytube/) for downloading youtube videoes. You can visit the library site to see the details by clicking on the highlighted word "pytube".

### Thanks for comming by :)
