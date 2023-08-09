import PySimpleGUI as sg
import os
import subprocess
import tkinter

def name(name):
    return sg.Text(name + ' - ')


def copy2clip2(text):
    r = tkinter.Tk()
    r.withdraw()
    r.clipboard_clear()
    r.clipboard_append(text)
    r.update() # now it stays on the clipboard after the window is closed
    r.destroy()

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

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

layout = [[sg.Text("The Form Filler")],]

for names in FormNames:
    layout.append([name(names),sg.Button('Copy',key=(names))])

layout.append([sg.HSep()],)
layout.append([sg.Button("Exit",key="-Exit-")],)

#print(layout)

window = sg.Window("Form Menu",layout)

while True:
    event, values = window.read(timeout=10)

    if event in (sg.WIN_CLOSED or 'Exit' or 'Cancel'):
        break
    elif event == "__TIMEOUT__":
        pass
    else:
        print(event)
        copy2clip2(forms[event])
