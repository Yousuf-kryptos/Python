# import tkinter as tk

# # These two are important in creating tkinter application
# root = tk.Tk() # Tk() class creates main application window

# root.mainloop() # mainloop() method starts the event loop by keep opening the window, wait for users 
#                 # actions (like mouse clicks , key presses) and processes until window is closed.

import tkinter as tk

root = tk.Tk()
# Label 

# label = tk.Label(root,text="Yousuf")  # Label() is used to display the text or images in the window
# label.pack()                          # pack() is used to place the label inside the window

# Button

# button = tk.Button(root,text="Click Here",width=25,command=root.destroy) # Button is an action element
# button.pack()                                                           # root.destroy will close the window

# Entry - is used to accept single line text from the user

# tk.Label(root,text="First Name").grid(row=0,column=0)
# tk.Label(root,text="Last Name").grid(row=1,column=0)

# entry1 = tk.Entry(root)
# entry2 = tk.Entry(root)

# entry1.grid(row=0,column=1)
# entry2.grid(row=1,column=1)

# tk.Button(root,text="Submit",command=root.destroy).grid(row=2,column=0)

root.mainloop()