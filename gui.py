import tkinter as tk
import random
window = tk.Tk()
window.title("Friendship game")
window.geometry("400x400")

# FUNCTIONS

def phrase_generator():
    phrases = ["hello ", "merhaba ", "akwaaba " , "chiao ", "Alohab "]

    names = str(entry1.get())

    return phrases[random.randint(0, 4)] + names

def phrase_display():
    gretting = phrase_generator()

    gretting_display = tk.Text(master=window,height=10, width=30)
    gretting_display.grid(column=0, row=6)
    gretting_display.insert(tk.END, gretting)


# LABEL
label1 = tk .Label(text="Hello, welcome to the newly improved Friendship App")
label1.grid(column=0, row=0,)

label2 = tk.Label(text="What's your name? ")
label2.grid(column=0, row=1)

label3 = tk.Label(text="Your friends name")
label3.grid(column=0, row=2)
# ENTRIES

entry1 = tk.Entry( )
entry1.grid(column=1, row=1)

entry2 = tk.Entry( )
entry2.grid(column=1, row=2)

# BUTTON

button1 = tk.Button(text="click here for results!", command=phrase_display)
button1.grid(column=0, row=3)





window.mainloop()


