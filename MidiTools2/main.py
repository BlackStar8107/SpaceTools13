import glob
import tkinter as tk
import tkinter.filedialog as tkf
from tkinter import ttk
import os
import time
import mido
import pywinauto
import threading
import psutil
import re
    
def make_ui():
    window = tk.Tk()
    window.title("Midi Player 2")

    for i in range(4):
        window.grid_columnconfigure(i, weight=1)
    
    for i in range(5):
        window.grid_rowconfigure(i, weight=1)

    display_frame = ttk.Frame(window, borderwidth=5, relief="ridge", width=250, height=100)
    now_playing = ttk.Label(display_frame, text="Now Playing: None")
    len_playing = ttk.Label(display_frame, text="Song Length: None")

    global progress
    progress = tk.IntVar()
    playbar = ttk.Progressbar(window, orient="horizontal",length=150, variable=progress)

    

    play_button = ttk.Button(window, text="Play", command=ui_play)
    pause_button = ttk.Button(window, text="Pause", command=ui_pause)
    stop_button = ttk.Button(window, text="Stop", command=ui_stop)
    select_button = ttk.Button(window, text="Select", command=ask_for_file)

    instrument_buttons = []

    global selected_instrument
    global paused

    paused = False
    selected_instrument = tk.StringVar()

    counter = 0
    for i in INSTRUMENTS:
        instrument_buttons.append( ttk.Radiobutton(window, text=i, variable=selected_instrument, value=i).grid(column=0, row = 5 + counter, sticky="nsew", padx=5, pady=5) )
        counter += 1

    selected_instrument.set("Guitar")

    display_frame.grid(column=0,row=0,columnspan=4,rowspan=2, sticky="nsew", padx=5, pady=5)
    now_playing.grid(column=0,row=0, sticky="nsew", padx=5, pady=5)
    len_playing.grid(column=0,row=1, sticky="nsew", padx=5, pady=5)
    playbar.grid(column=0,row=3,columnspan=4, sticky="nsew", padx=5, pady=5)
    play_button.grid(column=0,row=4, sticky="nsew", padx=5, pady=5)
    pause_button.grid(column=1,row=4, sticky="nsew", padx=5, pady=5)
    stop_button.grid(column=2,row=4, sticky="nsew", padx=5, pady=5)
    select_button.grid(column=3,row=4, sticky="nsew", padx=5, pady=5)

    window.mainloop()

def ask_for_file():
      global SELECTED_FILE
      global progress
      progress.set(0)
      SELECTED_FILE = tkf.askopenfilename(initialdir=os.path.dirname(__file__), filetypes=[("Midi File",".mid .midi"), ("All Files", "*")])
      read_file(SELECTED_FILE)

def get_pid(process_name):
   processes = psutil.process_iter()
   for process in processes:
       if re.search(process.name(), process_name, re.I):
          print(process)
          return process.pid

def get_note(note, number):
    match note.upper():
        case "C":
            return 12 * number
        case "CS":
            return (12 * number) + 1
        case "D":
            return (12 * number) + 2
        case "DS":
            return (12 * number) + 3
        case "E":
            return (12 * number) + 4
        case "F":
            return (12 * number) + 5
        case "FS":
            return (12 * number) + 6
        case "G":
            return (12 * number) + 7
        case "GS":
            return (12 * number) + 8
        case "A":
            return (12 * number) + 9
        case "AS":
            return (12 * number) + 10
        case "B":
            return (12 * number) + 11
        
MIDDLE_C_NOTE = 60 # Coincidentally, c4, the 5th MIDI C value... fuck only knows

INSTRUMENTS = {
    "Guitar" : {
            "Binding" : "2@34$5%6^78*9(0qQwWeErtTyYuiIoOpPasSdDfgGhHjJkl",
            "MaxNote" : get_note("c",7),
            "MinNote" : get_note("d",3),
        },
    "Banjo" : {
            "Binding" : "0qQwWeErtTyYuiIoOpPasSdDfgGhHjJkl",
            "MaxNote" : get_note("c",7),
            "MinNote" : get_note("e",4),
        },
    "Saxophone" : {
            "Binding" : "wWeErtTyYuiIoOpPasSdDfgGhHjJkl",
            "MaxNote" : get_note("c",7),
            "MinNote" : get_note("g",4),
        },
    "Fiddle" : {
            "Binding" : "eErtTyYuiIoOpPasSdDfgGhHjJklLzZxcCv",
            "MaxNote" : get_note("g",7),
            "MinNote" : get_note("a",4),
        },
    "Trumpet" : {
            "Binding" : "0qQwWeErtTyYuiIoOpPasSdDfgGhHjJkl",
            "MaxNote" : get_note("c",7),
            "MinNote" : get_note("e",4),
        },
    "Bass" : {
            "Binding" : "2@34$5%6^78*9(0qQwWeErtTyYuiIoOpPasSd",
            "MaxNote" : get_note("d",6),
            "MinNote" : get_note("d",3),
        },
    "Electric Guitar" : {
            "Binding" : "34$5%6^78*9(0qQwWeErtTyYuiIoOpPasSdDfgGhHjJkl",
            "MaxNote" : get_note("c",7),
            "MinNote" : get_note("e",3),
        },
    "Piano" : {
            "Binding" : "1!2@34$5%6^78*9(0qQwWeErtTyYuiIoOpPasSdDfgGhHjJklLzZxcCvVbBnm",
            "MaxNote" : get_note("c",8),
            "MinNote" : get_note("c",3),
    }
}

def read_file(file_name):
    global notes
    global midifile
    file_path = os.path.join(os.path.dirname(__file__),"MidiFiles",file_name)
    midifile = mido.MidiFile(file_path,type=0)
    # notes = player.get_all_notes()
    all_notes = []
    for message in midifile.tracks[1]:
            if str(message)[0:4] == "note":
                note_split = str(message).split(" ")
                note_on_off = note_split[0]
                notes = int(note_split[2].split("=")[1])
                #note_time = note_split [4]
                note_time = message.time
                all_notes.append([note_on_off,notes,note_time])
    # Global
    notes = all_notes

def scale_notes():
    global INSTRUMENTS
    global selected_instrument
    global notes
    # (maxAllowed - minAllowed) * (unscaledNum - min) / (max - min) + minAllowed
    # Should allow me to scale all our notes down within the instrument range
    # Also should be feeding the instrument range into this so we get correct values!

    c_instrument_dict = INSTRUMENTS[selected_instrument.get()]
    max_range = c_instrument_dict["MaxNote"]
    min_range = c_instrument_dict["MinNote"]
    min_note = min([thing[1] for thing in notes])
    max_note = max([thing[1] for thing in notes])
    
    new_notes = []
    for note in notes:
        new_note = round((max_range - min_range) * (note[1] - min_note) / (max_note - min_note) + min_range)
        
        # Fix because the lower range was not being scaled for some reason
        if new_note < min_range:
            new_note = min_range
        elif new_note > max_range:
            new_note = max_range
        new_notes.append([note[0],new_note,note[2]])
    
    notes = new_notes

    # mid = mido.MidiFile()
    # mid.ticks_per_beat = 1024
    # track = mido.MidiTrack()
    # mid.tracks.append(track)
    # for note in new_notes:
    #     track.append(mido.Message(note[0],note=note[1], time=note[2]))
    # mid.save("test_song.mid")
    # pass

def ui_pause():
    global paused
    paused = True

def ui_stop():
    global stop
    stop = True

def ui_play():
    global play_thread
    global paused
    global notes
    global midifile
    global selected_instrument
    global stop

    scale_notes()

    try:
        if play_thread.is_alive():
            if paused == True:
                paused = False
            else:
                return
        else:
            paused = False
            stop = False
            # play_thread = threading.Thread(target=play,args=(notes,paused,selected_instrument,midifile,progress, stop), daemon=True)
            play_thread = threading.Thread(target=play, daemon=True)
            play_thread.start()
    except:
        paused = False
        stop = False
        # play_thread = threading.Thread(target=play,args=(notes,paused,selected_instrument,midifile,progress, stop), daemon=True)
        play_thread = threading.Thread(target=play, daemon=True)
        play_thread.start()

# Will be a thread so must include everything!
# def play(notes, paused, selected_instrument, midifile, progress, stop):
def play():
    global play_thread
    global paused
    global notes
    global midifile
    global selected_instrument
    global stop
    c_instrument = INSTRUMENTS[selected_instrument.get()]
    bindings = c_instrument["Binding"]

    ticks_per_beat = midifile.ticks_per_beat

    found_tempo = False
    for message in midifile.tracks[0]:
        if message.type == "set_tempo" and not found_tempo:
            found_tempo = True
            
            tempo = message.tempo

    ticks_per_second = mido.tick2second(1, ticks_per_beat, tempo)

    process_id = get_pid("dreamseeker.exe")
    app = pywinauto.application.Application().connect(process=process_id)
    Music = app.windows(class_name="#32770")[0]

    i = 0
    while not stop and i < len(notes):
        # print(f"DEBUG > stop={stop}, pause={paused}")
        while not paused and i < len(notes) and not stop:
            # print(f"DEBUG > i={i}, stop={stop}, pause={paused}")
            progress.set( i / len(notes) * 100 )
            # print(i / len(notes) * 100)
            note = notes[i]
            c_key = bindings[note[1] - c_instrument["MinNote"]]
            if note[0] == "note_on":
                Music.type_keys("{"+c_key+"}")

            time.sleep(float(note[2]) * float(ticks_per_second))
            i += 1


if __name__ == "__main__":
        make_ui()
