import MidiHandler
import PySimpleGUI as sg
import os

##########
## TODO ##
##########
## 1. Be able to read Midi files
## 2. Be able to squash the Midi files into a specified note range
## 3. Map out all instrument bindings
## 4. Be able to play squashed Midi fiels by emulating key inputs
## 5. Make sure there is a failsafe key that will stop the playback!
## 6. Make some form of UI or way to select instrument!
## 7. Make some form of thing to select the Midi file to use!
# 8. Maybe eventually work out a way to feeback if paused or playing

def load_files():
    FILE_PATH = os.path.join(os.path.dirname(__file__),"MidiFiles")
    FILE_LIST = []
    for _, _, files in os.walk(FILE_PATH):
        FILE_LIST = files
    return FILE_LIST
    
if __name__ == "__main__":
    
    ## Start with Keybind for new people!
    KEYBIND_TEXT = "The Current Keybinds are:\n\nTAB - Use this to STOP the current playback.\nALT - Use this to PAUSE the current playback."
    LAYOUT_KEYBIND_POPUP = [[sg.Text("Keybind Help",font=(None,24))],[sg.Text(KEYBIND_TEXT,font=(None,18))],[sg.Text("By Default the Program starts paused. Due to how the way I wrote this, the interface will freeze whilst the song is playing. Cancelling it will make it work again.")],[sg.Button("Ok")]]
    WINDOW_KEYBIND = sg.Window("Help",LAYOUT_KEYBIND_POPUP)
    
    while True:
        event, values = WINDOW_KEYBIND.read()
        if event == sg.WIN_CLOSED or event == 'Ok':
            WINDOW_KEYBIND.close()
            break
        
    FILES = []
    FILES = load_files()
    STATUS_MESSAGE = "Now Playing: None"
    LAYOUT_SELECTION = [[sg.Text("Please select an instrument and song to play!")],[sg.Listbox(["Guitar","Banjo","Saxophone","Fiddle","Trumpet","Bass","Electric Guitar","Piano"],size=(35,15),select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, k="-InstrumentSelect-"),sg.VerticalSeparator(),sg.Listbox(values=FILES,size=(35,15),select_mode=sg.LISTBOX_SELECT_MODE_SINGLE, k="-MusicSelect-")], [sg.Text("How long the delays between notes are:"),sg.Spin(values=[1.0],k="-SpeedControl-",size=(5,1))],[sg.Button("Exit"),sg.Button("Play"),sg.Button("Refresh"),[sg.StatusBar(text=STATUS_MESSAGE,k="-StatusBar-")]]]
    WINDOW_LAYOUT = sg.Window("MidiTools",LAYOUT_SELECTION)
    
    
    while True:
        
        event, values = WINDOW_LAYOUT.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == "Play":
            try:
                instrument = WINDOW_LAYOUT["-InstrumentSelect-"].get()[0]
                instrument_dict = MidiHandler.INSTRUMENTS[instrument]
                play_file = WINDOW_LAYOUT["-MusicSelect-"].get()[0]
                play_speed = WINDOW_LAYOUT["-SpeedControl-"].get()
                print(instrument)
                print(play_file)
                MidiFile = MidiHandler.MidiFile()
                MidiFile.read_file(play_file)
                MidiFile.scale_notes(instrument_dict["MaxNote"],instrument_dict["MinNote"])
                STATUS_MESSAGE = f"Now Playing: {play_file}"
                WINDOW_LAYOUT["-StatusBar-"].update(STATUS_MESSAGE)
                WINDOW_LAYOUT.refresh()
                MidiFile.play(instrument,play_speed)
                STATUS_MESSAGE = "Now Playing: None"
                WINDOW_LAYOUT["-StatusBar-"].update(STATUS_MESSAGE)
                WINDOW_LAYOUT.refresh()
            except:
                pass
        elif event == "Refresh":
            FILES = load_files()
            WINDOW_LAYOUT["-MusicSelect-"].update(values=FILES)
            WINDOW_LAYOUT.refresh()