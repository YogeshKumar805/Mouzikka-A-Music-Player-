import random
import sys
import threading
import time
from tkinter import filedialog,messagebox
from cx_Oracle import DatabaseError
from pygame import mixer
import tkinter as tk
import tkinter.ttk as ttk
import Player
from MyExceptions import *
import musicplayer_support
import traceback

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global root
    root = tk.Tk()
    top=View(root)
    musicplayer_support.init(root, top)
    root.resizable(False, False)
    root.mainloop()

class View:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family {Avenir Next Cyr Medium} -size 23 -weight "  \
            "normal -slant roman -underline 0 -overstrike 0"
        font12 = "-family {Avenir Next Cyr} -size 9 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font13 = "-family {Vivaldi} -size 22 -weight " \
                 "bold -slant roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("687x526+558+155")
        top.title("New Toplevel")
        top.configure(background="#fff")
        self.top=top
        self.songName = tk.Label(top)
        self.songName.place(relx=0.437, rely=0.038, height=44, width=281)
        self.songName.configure(background="#fff")
        self.songName.configure(disabledforeground="#a3a3a3")
        self.songName.configure(font=font13)
        self.songName.configure(foreground="#000000")
        self.songName.configure(text='''Let's Enjoy''')

        self.songProgress = ttk.Progressbar(top)
        self.songProgress.place(relx=0.393, rely=0.209, relwidth=0.495
                , relheight=0.0, height=7)


        self.songTotalDuration = ttk.Label(top)
        self.songTotalDuration.place(relx=0.844, rely=0.171, height=19, width=29)

        self.songTotalDuration.configure(background="#fff")
        self.songTotalDuration.configure(foreground="#3399ff")
        self.songTotalDuration.configure(font=font12)
        self.songTotalDuration.configure(relief='flat')


        self.songTimePassed = ttk.Label(top)
        self.songTimePassed.place(relx=0.393, rely=0.171, height=19, width=29)
        self.songTimePassed.configure(background="#ffffff")
        self.songTimePassed.configure(foreground="#000000")
        self.songTimePassed.configure(font=font12)
        self.songTimePassed.configure(relief='flat')


        self.pauseButton = tk.Button(top)
        self.pauseButton.place(relx=0.568, rely=0.266, height=34, width=34)
        self.pauseButton.configure(activebackground="#ececec")
        self.pauseButton.configure(activeforeground="#000000")
        self.pauseButton.configure(background="#fff")
        self.pauseButton.configure(borderwidth="0")
        self.pauseButton.configure(disabledforeground="#a3a3a3")
        self.pauseButton.configure(foreground="#000000")
        self.pauseButton.configure(highlightbackground="#d9d9d9")
        self.pauseButton.configure(highlightcolor="black")
        self._img1 = tk.PhotoImage(file="./icons/pause.png")
        self.pauseButton.configure(image=self._img1)
        self.pauseButton.configure(pady="0")
        self.pauseButton.configure(text='''Button''')

        self.playButton = tk.Button(top)
        self.playButton.place(relx=0.64, rely=0.266, height=34, width=34)
        self.playButton.configure(activebackground="#ececec")
        self.playButton.configure(activeforeground="#000000")
        self.playButton.configure(background="#fff")
        self.playButton.configure(borderwidth="0")
        self.playButton.configure(disabledforeground="#a3a3a3")
        self.playButton.configure(foreground="#000000")
        self.playButton.configure(highlightbackground="#d9d9d9")
        self.playButton.configure(highlightcolor="black")
        self._img2 = tk.PhotoImage(file="./icons/play.png")
        self.playButton.configure(image=self._img2)
        self.playButton.configure(pady="0")
        self.playButton.configure(text='''Button''')

        self.stopButton = tk.Button(top)
        self.stopButton.place(relx=0.713, rely=0.266, height=34, width=34)
        self.stopButton.configure(activebackground="#ececec")
        self.stopButton.configure(activeforeground="#000000")
        self.stopButton.configure(background="#fff")
        self.stopButton.configure(borderwidth="0")
        self.stopButton.configure(disabledforeground="#a3a3a3")
        self.stopButton.configure(foreground="#000000")
        self.stopButton.configure(highlightbackground="#d9d9d9")
        self.stopButton.configure(highlightcolor="black")
        self._img3 = tk.PhotoImage(file="./icons/stop.png")
        self.stopButton.configure(image=self._img3)
        self.stopButton.configure(pady="0")
        self.stopButton.configure(text='''Button''')

        self.vinylRecordImage = tk.Label(top)
        self.vinylRecordImage.place(relx=0.0, rely=0.0, height=204, width=204)
        self.vinylRecordImage.configure(background="#d9d9d9")
        self.vinylRecordImage.configure(disabledforeground="#a3a3a3")
        self.vinylRecordImage.configure(foreground="#000000")
        self._img4 = tk.PhotoImage(file="./icons/vinylrecord.png")
        self.vinylRecordImage.configure(image=self._img4)
        self.vinylRecordImage.configure(text='''Label''')

        self.playList = ScrolledListBox(top)
        self.playList.place(relx=0.0, rely=0.38, relheight=0.532, relwidth=0.999)

        self.playList.configure(background="white")
        self.playList.configure(disabledforeground="#a3a3a3")
        self.playList.configure(font="TkFixedFont")
        self.playList.configure(foreground="black")
        self.playList.configure(highlightbackground="#d9d9d9")
        self.playList.configure(highlightcolor="#d9d9d9")
        self.playList.configure(selectbackground="#c4c4c4")
        self.playList.configure(selectforeground="black")
        self.playList.configure(width=10)

        self.previousButton = tk.Button(top)
        self.previousButton.place(relx=0.509, rely=0.285, height=16, width=16)
        self.previousButton.configure(background="#fff")
        self.previousButton.configure(borderwidth="0")
        self.previousButton.configure(disabledforeground="#a3a3a3")
        self.previousButton.configure(foreground="#000000")
        self._img5 = tk.PhotoImage(file="./icons/previous.png")
        self.previousButton.configure(image=self._img5)
        self.previousButton.configure(text='''Label''')

        self.bottomBar = ttk.Label(top)
        self.bottomBar.place(relx=0.0, rely=0.913, height=49, width=686)
        self.bottomBar.configure(background="#d9d9d9")
        self.bottomBar.configure(foreground="#000000")
        self.bottomBar.configure(font="TkDefaultFont")
        self.bottomBar.configure(relief='flat')
        self.bottomBar.configure(width=686)
        self.bottomBar.configure(state='disabled')

        self.vol_scale = ttk.Scale(top)
        self.vol_scale.place(relx=0.015, rely=0.932, relwidth=0.146, relheight=0.0
                , height=26, bordermode='ignore')
        self.vol_scale.configure(takefocus="")

        self.addSongsToPlayListButton = tk.Button(top)
        self.addSongsToPlayListButton.place(relx=0.961, rely=0.323, height=17
                , width=17)
        self.addSongsToPlayListButton.configure(activebackground="#ececec")
        self.addSongsToPlayListButton.configure(activeforeground="#d9d9d9")
        self.addSongsToPlayListButton.configure(background="#fff")
        self.addSongsToPlayListButton.configure(borderwidth="0")
        self.addSongsToPlayListButton.configure(disabledforeground="#a3a3a3")
        self.addSongsToPlayListButton.configure(foreground="#000000")
        self.addSongsToPlayListButton.configure(highlightbackground="#d9d9d9")
        self.addSongsToPlayListButton.configure(highlightcolor="black")
        self._img6 = tk.PhotoImage(file="./icons/add.png")
        self.addSongsToPlayListButton.configure(image=self._img6)
        self.addSongsToPlayListButton.configure(pady="0")
        self.addSongsToPlayListButton.configure(text='''Button''')

        self.deleteSongsFromPlaylistButton = tk.Button(top)
        self.deleteSongsFromPlaylistButton.place(relx=0.917, rely=0.323
                , height=18, width=18)
        self.deleteSongsFromPlaylistButton.configure(activebackground="#ececec")
        self.deleteSongsFromPlaylistButton.configure(activeforeground="#000000")
        self.deleteSongsFromPlaylistButton.configure(background="#fff")
        self.deleteSongsFromPlaylistButton.configure(borderwidth="0")
        self.deleteSongsFromPlaylistButton.configure(disabledforeground="#a3a3a3")
        self.deleteSongsFromPlaylistButton.configure(foreground="#000000")
        self.deleteSongsFromPlaylistButton.configure(highlightbackground="#d9d9d9")
        self.deleteSongsFromPlaylistButton.configure(highlightcolor="black")
        self._img7 = tk.PhotoImage(file="./icons/delete.png")
        self.deleteSongsFromPlaylistButton.configure(image=self._img7)
        self.deleteSongsFromPlaylistButton.configure(pady="0")
        self.deleteSongsFromPlaylistButton.configure(text='''Button''')

        self.addFavorite = tk.Button(top)
        self.addFavorite.place(relx=0.932, rely=0.913, height=42, width=42)
        self.addFavorite.configure(activebackground="#ececec")
        self.addFavorite.configure(activeforeground="#000000")
        self.addFavorite.configure(background="#d9d9d9")
        self.addFavorite.configure(borderwidth="0")
        self.addFavorite.configure(disabledforeground="#a3a3a3")
        self.addFavorite.configure(foreground="#000000")
        self.addFavorite.configure(highlightbackground="#d9d9d9")
        self.addFavorite.configure(highlightcolor="black")
        self._img8 = tk.PhotoImage(file="./icons/like.png")
        self.addFavorite.configure(image=self._img8)
        self.addFavorite.configure(pady="0")
        self.addFavorite.configure(text='''Button''')
        self.addFavorite.configure(width=42)

        self.removeFavorite = tk.Button(top)
        self.removeFavorite.place(relx=0.873, rely=0.913, height=42, width=42)
        self.removeFavorite.configure(activebackground="#ececec")
        self.removeFavorite.configure(activeforeground="#000000")
        self.removeFavorite.configure(background="#d9d9d9")
        self.removeFavorite.configure(borderwidth="0")
        self.removeFavorite.configure(disabledforeground="#a3a3a3")
        self.removeFavorite.configure(foreground="#000000")
        self.removeFavorite.configure(highlightbackground="#d9d9d9")
        self.removeFavorite.configure(highlightcolor="black")
        self._img9 = tk.PhotoImage(file="./icons/broken-heart.png")
        self.removeFavorite.configure(image=self._img9)
        self.removeFavorite.configure(pady="0")
        self.removeFavorite.configure(text='''Button''')
        self.removeFavorite.configure(width=48)

        self.loadFavorite = tk.Button(top)
        self.loadFavorite.place(relx=0.83, rely=0.932, height=26, width=26)
        self.loadFavorite.configure(activebackground="#ececec")
        self.loadFavorite.configure(activeforeground="#000000")
        self.loadFavorite.configure(background="#d9d9d9")
        self.loadFavorite.configure(borderwidth="0")
        self.loadFavorite.configure(disabledforeground="#a3a3a3")
        self.loadFavorite.configure(foreground="#000000")
        self.loadFavorite.configure(highlightbackground="#d9d9d9")
        self.loadFavorite.configure(highlightcolor="black")
        self._img10 = tk.PhotoImage(file="./icons/refresh.png")
        self.loadFavorite.configure(image=self._img10)
        self.loadFavorite.configure(pady="0")
        self.loadFavorite.configure(text='''Button''')
        #messagebox.showinfo("Success!", "Connected successfully to the DB!!!")
        #self.vol_scale.configure(from_=0, to=100, command=self.change_volume)
        #self.change_volume()
        self.setup_player()
    def setup_player(self):
        try:
           self.player=Player.Player()
           if self.player.get_db_status():
              messagebox.showinfo("Success","connected sucessfully to the DB")
              self.addFavorite.config(command=self.add_song_to_favourites)
              self.removeFavorite.config(command=self.remove_song_from_favourites)
              self.loadFavorite.config(command=self.load_songs_from_favourites)
           else:
               raise Exception("Sorry you can not save songs to favourite")
        except Exception as ex:
            messagebox.showinfo("Error",ex)

            self.addFavorite.config(state="disabled")
            self.removeFavorite.config(state="disabled")
            self.loadFavorite.config(state="disabled")
        self.vol_scale.config(from_=0,to=100,command=self.change_volume)
        self.vol_scale.set(50)
        self.addSongsToPlayListButton.config(command=self.add_song)
        self.deleteSongsFromPlaylistButton.config(command=self.remove_song)
        self.playButton.config(command=self.play_song)
        self.stopButton.config(command=self.stop_song)
        self.pauseButton.config(command=self.pause_song)
        self.previousButton.config(command=self.load_previous_song)
        self.playList.config(font="Vivaldi 12")
        self.playList.bind("<Double-1>",self.list_double_click)
        self.top.title("MOUZIKKA -Dance To The Rhythm Of Your Heart")
        img=tk.PhotoImage(file="./icons/icon-music1.png")
        self.top.iconphoto(self.top,img)
        self.top.protocol("WM_DELETE_WINDOW",self.close_window)
        self.isPlaying=False
        self.isPaused=False
        self.my_thread=None
        self.isThreadRunning=False


    def close_window(self):
        print("Window closed")
        #user confirmation
        sys.exit(0)
    def change_volume(self,val):
        volume_level=float(val)/100
        self.player.set_volume(volume_level)

    def add_song(self):
        song_name=self.player.add_song()
        if song_name is None:
            return
        self.playList.insert(tk.END,song_name)
        rcolor=lambda :random.randint(0,255)
        red=hex(rcolor())
        green=hex(rcolor())
        blue=hex(rcolor())
        red=red[2:]
        green=green[2:]
        blue=blue[2:]
        if len(red)==1:
            red="0"+red
        if len(green)==1:
            green="0"+green
        if len(blue)==1:
            blue="0"+blue
        mycolor="#"+red+green+blue
        self.playList.config(fg=mycolor)
    def show_song_detials(self):
        self.song_length=int(self.player.get_song_length(self.song_name))
        min,sec=divmod(self.song_length,60)
        min=round(min)
        sec=round(sec)
        self.songTotalDuration.config(text=str(min)+":"+str(sec))
        self.songTimePassed.config(text="0:0")
        dot_index=self.song_name.rfind(".")
        song_name_str=self.song_name[0:dot_index]
        if len(song_name_str)>14:
            song_name_str=song_name_str[0:14]+". . ."
        self.songName.configure(text=song_name_str)


    def play_song(self):
        print("play song called")
        self.sel_song_index_tuple=self.playList.curselection()
        try:
            if len(self.sel_song_index_tuple)==0:
                delattr(self,"select_song_index_tuple")
                raise NoSongSelectedError("Please select a song first")
            self.song_name=self.playList.get(self.sel_song_index_tuple[0])
            self.show_song_detials()
            if(self.isThreadRunning==False):
                self.isThreadRunning=True
            else:
                self.stop_song()
                time.sleep(1)
            self.songProgress.config(length=self.song_length,maximum=self.song_length)
            self.setup_thread()
            self.player.play_song()
            self.isPlaying=True
        except (NoSongSelectedError) as ex:
            messagebox.showerror("error",ex)

    def setup_thread(self):
        self.my_thread=threading.Thread(target=self.show_timer,args=(self.song_length,))
        self.my_thread.start()







    def show_timer(self,total_sec):
        curr_sec=0
        self.songProgress.stop()
        while curr_sec<=total_sec and mixer.music.get_busy():
            if self.isPaused:
                continue
            min,sec=divmod(curr_sec,60)
            min=round(min)
            sec=round(sec)
            self.songTimePassed.config(text=str(min)+":"+str(sec))

            curr_sec+=1
            self.songProgress.step()
            time.sleep(1)
        print("Thread Finished")
        if curr_sec>total_sec:
            self.load_next_song()






    def pause_song(self):
        if self.isPlaying==True:
            if self.isPaused==False:
                self.player.pause_song()
                self.isPaused=True
            else:
                self.player.unpause_song()
                self.isPaused=False

    def close_window(self):
        result=messagebox.askyesno("App Closing!!","Do you want to quit?")
        if result:
            self.player.close_player()
            messagebox.showinfo("Have a nice day","Thank you" )
            self.top.destroy()

    def remove_song(self):
        self.sel_song_index_tuple=self.playList.curselection()
        try:
            if len(self.sel_song_index_tuple)==0:
                raise NoSongSelectedError("Please select a song to remove")
            song_name=self.playList.get(self.sel_song_index_tuple[0])
            self.playList.delete(self.sel_song_index_tuple[0])
            self.player.remove_song(song_name)
        except (NoSongSelectedError) as ex:
            messagebox.showinfo("Error",ex)


    def stop_song(self):
        self.player.stop_song()
        self.isPlaying=False
    def load_previous_song(self):
        try:
            if hasattr(self,"sel_song_index_tuple")==False:
                raise NoSongSelectedError("Please play a song first")
            self.prev_song_index=self.sel_song_index_tuple[0]-1
            if self.prev_song_index==-1:
               self.prev_song_index=self.playList.count()-1
            self.playList.select_clear(0,tk.END)
            self.playList.select_set(self.prev_song_index)
            self.play_song()
        except (NoSongSelectedError) as ex:
            messagebox.showinfo("Error",ex)
    def load_next_song(self):
        try:
            if hasattr(self,"sel_song_index_tuple")==False:
                raise NoSongSelectedError("please play a song first")
            self.next_song_index = self.sel_song_index_tuple[0]+1
            if self.next_song_index == self.player.get_song_count():
               self.next_song_index=0
            self.playList.select_clear(0,tk.END)
            self.playList.selection_set(self.next_song_index)
            print("Next song index:",self.next_song_index)
            self.play_song()
        except (NoSongSelectedError) as ex:
            messagebox.showinfo("Error",ex)


    def add_song_to_favourites(self):
        fav_song_index_tuple=self.playList.curselection()
        try:
            if(len(fav_song_index_tuple)==0):
                raise NoSongSelectedError("Please Select a song for adding to favourites")
            song_name=self.playList.get(fav_song_index_tuple[0])
            result=self.player.add_song_in_favourites(song_name)
            messagebox.showinfo("Sucess",result)
        except (NoSongSelectedError) as ex:
            messagebox.showinfo("Error",ex)
        except (DatabaseError) as ex:
            messagebox.showinfo("DB Error",ex)


    def remove_song_from_favourites(self):
        fav_song_index_tuple=self.playList.curselection()
        try:
            if(len(fav_song_index_tuple)==0):
                raise  NoSongSelectedError("please select a song for removing a  favourites")
            song_name=self.playList.get(fav_song_index_tuple[0])
            result=self.player.remove_song_from_favourites(song_name)
            if(result.find("deleted")!=-1):
                self.playList.delete(fav_song_index_tuple[0])
            if(fav_song_index_tuple[0]==self.sel_song_index_tuple[0]):
                    self.stop_song()
                    messagebox.showinfo("Sucess",result)
        except (NoSongSelectedError) as ex:
            messagebox.showinfo("error",ex)
        except (DatabaseError) as ex:
            messagebox.showinfo("DB ERROR",ex)








    def load_songs_from_favourites(self):
        try:
            load_result=self.player.load_songs_from_favourites()
            result_str=load_result[0]
            if result_str.find("No songs")!=-1:
                messagebox.showinfo("Favourites Empty!!",result_str)
                return
            song_dict=load_result[1]
            self.playList.delete(0,tk.END)
            for song_name in song_dict:
                self.playList.insert(tk.END,song_name)
            rcolor=lambda :random.randint(0,255)
            red=hex(rcolor())
            green=hex(rcolor())
            blue=hex(rcolor())
            red=red[2:]
            green=green[2:]
            blue=blue[2:]

            if len(red)==1:
                red="0"+red
            if len(green)==1:
                green="0"+green
            if len(blue)==1:
                blue="0"+blue
                mycolor="#"+red+green+blue
                self.playList.config(fg=mycolor)
                messagebox.showinfo("Songs Added!!",result_str)
        except(DatabaseError) as ex:
            messagebox.showinfo("DB Error",ex)









    def list_double_click(self,e):
        self.play_song()


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
    def count(self):
        return tk.Listbox.size(self)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





