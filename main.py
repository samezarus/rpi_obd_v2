from tkinter import *  
from tkinter import ttk  
from tkinter import scrolledtext 

import obd

# 
ecu = None
portstr = "/dev/ttyUSB0"
baudrate = 38400


def ecu_connect():
    """ Connect to ECU """

    global ecu
    global portstr
    global baudrate

    try:
        ecu = obd.OBD(portstr=portstr, baudrate=baudrate, fast=True) 
    except:
        ecu = None


def clear_all_erors():
    """ Сбрасываем ошибки """

    global ecu

    if ecu is not None:
        connection = ecu.OBD(portstr="/dev/ttyUSB0", baudrate=38400, fast=False)
        connection.query(ecu.commands.CLEAR_DTC)
    else:
        pass


def set_text(entry_, text):
    if entry_ is not None:
        if type(entry_) == Entry:
            entry_.delete(0,END)
            entry_.insert(0,text)


#
window = Tk()  
window.maxsize(800, 480)
window.geometry('800x480')
window.title("RPI OBD Scaner")

#
s = ttk.Style()
s.configure('TNotebook.Tab', font=('URW Gothic L','18','bold') )

#
tabs = ttk.Notebook(window)

# Main tab
tab_main = ttk.Frame(tabs)  
tabs.add(tab_main, text='Main')

txt_port = Entry(tab_main, width=100)
set_text(txt_port, portstr)
txt_port.pack()

btn_conn = Button(tab_main, text = "Connect to ECU", command=ecu_connect).place(x=5, y=30, width=120, height=50)

btn_clr_err = Button(tab_main, text = "Clear Error's", command=clear_all_erors).place(x=5, y=120, width=100, height=50)
btn_get_err = Button(tab_main, text = "Read Error's", command=clear_all_erors).place(x=105, y=120, width=100, height=50)


# Error's tab
tab_err = ttk.Frame(tabs)  
tabs.add(tab_err, text="Error's")

txt_err = scrolledtext.ScrolledText(tab_err, width=40, height=10)  
txt_err.grid(column=0, row=0)  
txt_err.pack(fill=BOTH, expand=YES)

# Widget's tab
tab_wdg = ttk.Frame(tabs)  
tabs.add(tab_wdg, text="Widget's")  

# Logs's tab
tab_log = ttk.Frame(tabs)  
tabs.add(tab_log, text="Log's")  

txt_log = scrolledtext.ScrolledText(tab_log, width=40, height=10)  
txt_log.grid(column=0, row=0)  
txt_log.pack(fill=BOTH, expand=YES)

#
tabs.pack(expand=1, fill='both')  

#
window.mainloop()