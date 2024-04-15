import mido
import os.path
# from pyautogui import keyDown, keyUp, FAILSAFE
import time
import keyboard
import re

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
FAILSAFE = True

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

class MidiFile():
    def __init__(self) -> None:
        self.midifile = ""
        self.file_path = ""
        return
    
    # We assume that the Midi is going to be stored in the MidiFiles folder
    def read_file(self, file_name) -> bool:
        self.file_path = os.path.join(os.path.dirname(__file__),"MidiFiles",file_name)
        self.midifile = mido.MidiFile(self.file_path,type=0)
        self.player = MidiPlayer(self.midifile)
        self.notes = self.player.get_all_notes()
    
    def scale_notes(self, max_range = 100, min_range = 0) -> None:
        # (maxAllowed - minAllowed) * (unscaledNum - min) / (max - min) + minAllowed
        # Should allow me to scale all our notes down within the instrument range
        # Also should be feeding the instrument range into this so we get correct values!
        
        self.min_note = min([thing[1] for thing in self.notes])
        self.max_note = max([thing[1] for thing in self.notes])
        
        new_notes = []
        for note in self.notes:
            new_note = round((max_range - min_range) * (note[1] - self.min_note) / (self.max_note - self.min_note) + min_range)
            
            # Fix because the lower range was not being scaled for some reason
            if new_note < min_range:
                new_note = min_range
            elif new_note > max_range:
                new_note = max_range
            new_notes.append([note[0],new_note,note[2]])
        
        self.notes = new_notes

    def play(self, instrument, time_mult = 1):
        self.player.set_notes(self.notes)
        self.player.play(instrument, time_mult)


# Honestly why is this a seperate class at this point
# Okay well this has been stripped now
class MidiPlayer():
    def __init__(self, MidiFile) -> None:
        self.MidiFile = MidiFile
        self.ticks_per_beat = MidiFile.ticks_per_beat
        self.tempo = self.get_tempo()
        self.ticks_per_second = mido.tick2second(1, self.ticks_per_beat, self.tempo)
        pass
                
    # note = xx means the note hit, c = 60
    # velocity = xx can be discarded as we don't do that!
    # time = xx is delta time (I think)
    def get_all_notes(self) -> list:
        self.all_notes = []
        for message in self.MidiFile.tracks[1]:
            if str(message)[0:4] == "note":
                note_split = str(message).split(" ")
                note_on_off = note_split[0]
                notes = int(note_split[2].split("=")[1])
                #note_time = note_split [4]
                note_time = message.time
                self.all_notes.append([note_on_off,notes,note_time])
                
        return self.all_notes
    
    def get_tempo(self) -> float:
        found_tempo = False
        for message in self.MidiFile.tracks[0]:
            if message.type == "set_tempo" and not found_tempo:
                found_tempo = True
                
                self.tempo = message.tempo
        return self.tempo
    
    def play(self, instrument, time_mult = 1):
        c_instrument = INSTRUMENTS[instrument]
        PAUSE = True
        for note in self.all_notes:
            while(PAUSE):
                if keyboard.is_pressed("ALT"):
                    print("Unpaused Program")
                    PAUSE = False
                    time.sleep(0.5)
                if keyboard.is_pressed("TAB"):
                    print("Keyboard Interrupt!")
                    break
            if keyboard.is_pressed("TAB"):
                print("Keyboard Interrupt!")
                break
            if keyboard.is_pressed("ALT"):
                print("Paused Program")
                PAUSE = True
                time.sleep(0.5)
            
            # print(note)
            c_key = self.get_key(note[1], instrument)
            if note[0] == "note_on":
                # Turns out that 'D' causes a system mute??
                # I genuinly want to know the spaghetti on that one
                if re.search("[^a-z1-9]",c_key) != None:
                    keyboard.send("shift+"+str(c_key).lower())
                    # print("shift"+c_key)
                else:
                    keyboard.send(c_key)
                    # print(c_key)
            time.sleep(float(note[2]) * float(self.ticks_per_second) * float(time_mult))
                
    def set_notes(self, notes):
        self.all_notes = notes
        
    def get_key(self, note, instrument):
        c_instrument = INSTRUMENTS[instrument]
        bindings = c_instrument["Binding"]
        return bindings[note - c_instrument["MinNote"]]