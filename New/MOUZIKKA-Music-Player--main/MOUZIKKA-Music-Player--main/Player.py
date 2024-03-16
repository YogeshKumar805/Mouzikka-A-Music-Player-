import Model
from pygame import mixer
from tkinter import filedialog
import os #ydi file ka path de denge tho os automaticaly file ka name de dega.
from mutagen.mp3 import MP3
class Player:
    def __init__(self):
        mixer.init()
        self.my_model=Model.Model()

    def get_db_status(self):
        return self.my_model.get_db_status()

    def close_player(self):
        mixer.music.stop()
        self.my_model.close_db_conn()

    def set_volume(self,volume_level):
        mixer.music.set_volume(volume_level)

    def add_song(self):
        song_path=filedialog.askopenfilename(title="select a song...",filetypes=[("mp3 files",".mp3")])
        if song_path=="":
           return
        song_name=os.path.basename(song_path)
        self.my_model.add_song(song_name,song_path)
        return song_name

    def remove_song(self,song_name):
        self.my_model.remove_song(song_name)

    def get_song_length(self,song_name):
        self.song_path=self.my_model.get_song_path(song_name)
        self.audio_tag=MP3(self.song_path)
        self.song_length=self.audio_tag.info.length
        return self.song_length

    def play_song(self):
        mixer.quit()
        mixer.init(frequency=self.audio_tag.info.sample_rate)
        mixer.music.load(self.song_path)
        mixer.music.play()



    def stop_song(self):
        mixer.music.stop()
    def pause_song(self):

        mixer.music.pause()

    def unpause_song(self):
        mixer.music.unpause()

    def add_song_in_favourites(self,song_name):
        song_path=self.my_model.get_song_path(song_name)
        result=self.my_model.add_song_in_favourites(song_name,song_path)
        return result

    def load_songs_from_favourites(self):
        result=self.my_model.load_songs_from_favourites()
        return result,self.my_model.song_dict

    def remove_song_from_favourites(self,song_name):
        result=self.my_model.remove_song_from_favourites(song_name)
        return result
    def get_song_count(self):
        return  self.my_model.get_song_count()









