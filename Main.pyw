import PySimpleGUI as sg
from math import ceil
import os
import subprocess
import tkinter
import logging

# TODO: Re-write this to conform to dunder main
# TODO: Setup a check for imports
# TODO: Setup method of importing from "../modules/*"
# TODO: Dynamic Tab Support

def getValue(value, mult):
    try:
        return ceil(float(value) * float(mult))
    except:
        logging.warning("Error with GetValue, probably invalid input!")
        return 0


def name(name):
    return sg.Text(name + ' - ')


def copy2clip2(text):
    try:
        r = tkinter.Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(text)
        r.update() # now it stays on the clipboard after the window is closed
        r.destroy()
    except:
        logging.error("Error Whilst Copying to Clipboard")


layout_trader = [
    [sg.Input(key="NumInput"),sg.Button("Calculate",key="Calc",bind_return_key=True)],
    [name("Random"),sg.Text(key="RandomL"),sg.VSep(),sg.Text(key="Random")],
    [name("This is my final offer. Can't do better than this.")],
    [sg.HSep()],

    [name("Grag"),sg.Text(key="GragL"),sg.VSep(),sg.Text(key="Grag")],
    [name("FINE. BUT ENOUGH TALK. TRADE NOW OR FORGET IT.")],
    [sg.HSep()],

    [name("Vurdulak"),sg.Text(key="VurdulakL"),sg.VSep(),sg.Text(key="Vurdulak")],
    [name("We will afford you no further leniency. Make the transaction now.")],
    [sg.HSep()],

    [name("Josh"),sg.Text(key="JoshL"),sg.VSep(),sg.Text(key="Josh")],
    [name("That sounds fine enough. You sure you don't want to buy any more broriffic goods?")],
    [sg.HSep()],

    [name("Buford"),sg.Text(key="BufordL"),sg.VSep(),sg.Text(key="Buford")],
    [name("Aight man, but you're really pushing it. Let's make the trade now, yeah?")],
    [sg.HSep()],

    [name("Buford Stoned"),sg.Text(key="BufordSL"),sg.VSep(),sg.Text(key="BufordS")],
    [name("Uh.. shit.. sure! I think? ..fuck. I'm getting a headache.")],
    [sg.HSep()],

    [name("Pianzi"),sg.Text(key="PianziL"),sg.VSep(),sg.Text(key="Pianzi")],
    [name("Well, my good friend. This is my final offer, I'd have to be insane to cut you a better bargain than this!")],
    [sg.HSep()],
]

forms = {
    "Death Certificate" : '''# <center>NanoTrasen Medical Association</center>
_<center>Vivamus moriendum est</center>_
___

**<center>ID No. [____]** _(Official use only)</center>_

<center>A copy of this document is to be made available to the relatives/associates of the deceased as well as for the archives of the on-station medical records.</center>

## <center>Death Certificate</center>
___
*I, [____________________________________], in my capacity as a NanoTrasen-certified medical physician, certify that the individual known as [____________________________________] has been declared legally dead.*

**AGE: [___]**

**SEX: (M)[__] (F)[__] (OTHER)[__]**

**JOB TITLE:**
[____________________________________]

**CAUSE OF DEATH:**
[____________________________________]

**SHIFT TIME OF DEATH:**
[____________________________________]
___
<center>This may be admitted as evidence in a NanoTrasen Court of Space Law. Knowingly entering false details may result in the disqualification of the attending physician from medical practice.</center>

**Shift Time:**
\\
\\
\\
\\
\\
**Physician's Signature:**
[_______________]''',

    "Post Mortem" : '''# <center>NanoTrasen Medical Association</center>
_<center>Vivamus moriendum est</center>_
___

**<center>ID No. [____]** _(Official use only)</center>_

## <center>Autopsy Record</center>
<center>To be used for the recording of the results of medical autopsies. This may be admitted as evidence in a NanoTrasen Court of Space Law. Knowingly entering false details may result in the disqualification of the attending physician from medical practice.</center>

**<center>ALL BODIES THAT ARE TO BE AUTOPSIED MUST BE PRESERVED WITH FORMALDEHYDE/EMBALMING FLUID BEFORE COMMENCEMENT.</center>**
___
## Please enter details below on the lines with a pen.

**Name:**
[____________________________________]

**Health Analysis:**

**(OXY)[___] (TOX)[___] (BUR)[___] (BTE)[___]**

**(BRAIN Y/N)[_]**

**(BLOOD VOLUME)[____]**

**Active Medical Issues:**
[____________________________________]

**Reagents Found:**
[____________________________________]

**Organ Condition:**
[____________________________________]

**Foreign Objects (If Applicable):**
[____________________________________]

**Visible Wounds (If Applicable):**
[____________________________________]

**Shift Time of Death (If Known):** [_____]

**Body Condition**
[____________________________________]

**Cause of Death**
[____________________________________]
___

**Shift Time:**
\\
\\
\\
\\
\\
**Physician's Signature:**
[_______________]''',

    "Organ Extraction" : '''# <center>NanoTrasen Medical Association</center>
_<center>Vivamus moriendum est</center>_
___

**<center>ID No. [____]** _(Official use only)</center>_

## <center>Autopsy Record</center>
<center>To be used for the recording of the results of medical autopsies. This may be admitted as evidence in a NanoTrasen Court of Space Law. Knowingly entering false details may result in the disqualification of the attending physician from medical practice.</center>

**<center>ALL BODIES THAT ARE TO BE AUTOPSIED MUST BE PRESERVED WITH FORMALDEHYDE/EMBALMING FLUID BEFORE COMMENCEMENT.</center>**
___
## Please enter details below on the lines with a pen.

**Name:**
[____________________________________]


**Organs Extracted:**

|  Qty  |                  Organs                |
|:-----:|:--------------------------------------:|
| [___] | [____________________________________] |
| [___] | [____________________________________] |
| [___] | [____________________________________] |
| [___] | [____________________________________] |
| [___] | [____________________________________] |
| [___] | [____________________________________] |
| [___] | [____________________________________] |
| [___] | [____________________________________] |
| [___] | [____________________________________] |
| [___] | [____________________________________] |
| [___] | [____________________________________] |
| [___] | [____________________________________] |
| [___] | [____________________________________] |
| [___] | [____________________________________] |
| [___] | [____________________________________] |
| [___] | [____________________________________] |




**Body Condition**
[____________________________________]


___

**Physician's Signature:**
[_______________]''',

    "Requisition Form" : '''# <center>Cargonia Supply and Logistics Ltd.</center>
_<center>NanoTrasen's premier courier and logistics firm</center>_
___
## <center>Supply Requisition Form</center>
_<center>(Official use only)</center>_
___
## Please fill out the fields below with a pen

**Department:**
[____________________________________]

**Request Due (Shift Time):** [_________]

**Reason:**
[____________________________________]

|  Qty  |                  Item                  | Price ($) |
|:-----:|:--------------------------------------:|:---------:|
| [___] | [____________________________________] |  [______] |
| [___] | [____________________________________] |  [______] |
| [___] | [____________________________________] |  [______] |
| [___] | [____________________________________] |  [______] |
| [___] | [____________________________________] |  [______] |
|       |                       Total Price ($): |  [______] |

_By signing this form, you agree to not hold Cargonia Supply and Logistics Limited liable for any damage, loss, or other misfortune incurred against yourself, your department, your corporation, any other entity which you may constitute or own, or your purchased goods. You also agree to not hold Cargonia Supply and Logistics Limited liable for the delayed or non-delivery of your goods should it not violate the rights and obligations granted to Cargonia Supply and Logistics Limited by NanoTrasen Space Law. You also agree that this purchase is within the best interests for the continued operation of your department or the station as a whole. You also agree that you are legally allowed to purchase these goods and that you are not purchasing them on the behalf of someone who cannot legally purchase these goods._

**Requestor Signature:**
[____________________________________]
___
**For Official Use Only**

**Sensitive/Restricted Goods?:** [__]

**(If goods are restricted) Authorization Stamp from Relevant Authority:**
\\
\\
\\
\\
\\
**Validity Stamp:**
\\
\\
\\
\\
\\
**(If Denial) Reason:**
[____________________________________]

**Shift Time:**
\\
\\
\\
\\
\\
**Overseeing Quartermaster's Signature:**
[__________________]'''
}
FormNames = list(forms.keys())
layout_forms = [[sg.Text("The Form Filler")],]
for names in FormNames:
    layout_forms.append([name(names),sg.Button('Copy',key=(names))])
layout_forms.append([sg.HSep()],)

layout = [[sg.TabGroup([
   [sg.Tab('Forms', layout_forms),
   sg.Tab('Trading', layout_trader)]])],
   [sg.Button("Exit",key="-Exit-")]
]

window = window = sg.Window("SS13 Helper",layout)

while True:
    event, values = window.read(timeout=10)

    if event in (sg.WIN_CLOSED or 'Exit' or 'Cancel'):
        break
    elif event == "__TIMEOUT__":
        pass
    elif event == "Calc":
        value = values["NumInput"]
        print(value)

        window["Random"].update(getValue(value,1.2))
        window["RandomL"].update(getValue(value,0.8))

        window["Grag"].update(getValue(value,1.15))
        window["GragL"].update(getValue(value,0.85))

        window["Vurdulak"].update(getValue(value,1.10))
        window["VurdulakL"].update(getValue(value,0.9))

        window["Josh"].update(getValue(value,1.15))
        window["JoshL"].update(getValue(value,0.85))

        window["Buford"].update(getValue(value,1.3))
        window["BufordL"].update(getValue(value,0.7))

        window["BufordS"].update(getValue(value, 1.95))
        window["BufordSL"].update(getValue(value, 0.05))

        window["Pianzi"].update(getValue(value,1.33))
        window["PianziL"].update(getValue(value,0.67))
    else:
        print(event)
        copy2clip2(forms[event])