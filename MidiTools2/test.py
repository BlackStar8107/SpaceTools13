import pywinauto
import psutil
import re
import time
import tkinter
import threading

def get_pid(process_name):
    processes = psutil.process_iter()
    for process in processes:
        if re.search(process.name(), process_name, re.I):
            print(process)
            return process.pid
    processes = psutil.process_iter()
    with open("pid.log", "w") as f:
        for process in processes:
            string = f"pid={process.pid}, name={process.name}, status={process.status}, started={process.create_time}"
            f.write(string+"\n")
       
process_id = get_pid("dreamseeker.exe")
print(process_id)
app = pywinauto.application.Application().connect(process=process_id)
# app.top_window().TypeKeys("H")

def ui():
    root = tkinter.Tk()
    root.attributes('-topmost', True)
    root.update()
    root.mainloop()

UI_Thread = threading.Thread(target=ui, daemon=True)
UI_Thread.start()
Music = app.windows(class_name="#32770")[0]
Music.type_keys("qwe")
time.sleep(5)
# for i in range(1000):
#    app.top_window().type_keys(i)
#    time.sleep(3)