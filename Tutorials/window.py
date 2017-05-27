from tkinter import *
from datetime import datetime

window = Tk()

window.title('Label')
label = Label(window, text = 'Wubba Lubba Dub Dub!')
label.pack(padx=200, pady = 50)


#Button(window, text="Close", command=exit)

#btn_tog = Button(window, text="Switch", command=tog)
#btn_end.pack(padx=150, pady=20)

window.mainloop()
