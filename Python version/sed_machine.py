#------------------------------------------------------------------------------
# Original author:  Terpal47
# Creation date:    26/05/2016
# Description:      Encrypts and decrypts messages based on a symmetric-key
#                   encryption system. Works via a GUI written using Tkinter.
#------------------------------------------------------------------------------
from tkinter import *
import cryptography_functions as cf

# Defines the class for the window.
class Window(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)

		self.master = master

		self.init_window()

	def init_window(self):
		self.master.title("SED Machine")
		self.pack(fill=BOTH, expand=1)

def generate_key():
	"""Randomly generates a key and inserts it in key_entry. Bound to the
	generate_b button."""
	key = cf.generate_key()
	key_entry.delete(0, 'end')
	key_entry.insert(0, key)

def encrypt():
	"""Uses the existing key in key_entry and the text in message_text and
	replaces it with its encrypted version."""
	message = message_text.get(1.0, 'end-1c')
	message_text.delete('1.0', 'end')
	key = key_entry.get()
	encrypted = cf.encrypt(message, key)
	message_text.insert(1.0, encrypted)

def decrypt():
	"""Uses the existing key in key_entry and the text in message_text and
	replaces it with its decrypted version."""
	message = message_text.get(1.0, 'end-1c')
	message_text.delete('1.0', 'end')
	key = key_entry.get()
	decrypted = cf.decrypt(message, key)
	message_text.insert(1.0, decrypted)

root = Tk()
# Sets window size
root.geometry('600x400')

app = Window(root)

# Places the top, middle, and bottom frames.
# Top frame contains generate key, encrypt, and decrypt buttons.
top_frame = Frame(root, width=600, height=200)
top_frame.place(x=0,y=0)

# Middle frame contains the key_entry field.
mid_frame = Frame(root, width=600, height=200)
mid_frame.place(x=0,y=100)

# Contains the text box for messages.
bottom_frame = Frame(root, width=600, height=200)
bottom_frame.place(x=0,y=150)

# Creates and places the Generate Key button.
generate_b = Button(top_frame, text='Generate Key', command=generate_key)
generate_b.pack(side=LEFT, padx=20, pady=20)

# Creates and places the Encrypt button.
encrypt_b = Button(top_frame, text='Encrypt!', command=encrypt)
encrypt_b.pack(side=LEFT)

# Creates and places the Decrypt button.
decrypt_b = Button(top_frame, text='Decrypt!', command=decrypt)
decrypt_b.pack(side=LEFT)

# Creates and places the field for the key.
key_entry = Entry(mid_frame, width=98)
key_entry.pack(side=BOTTOM)

# Creates and places the text box for storing encrypted and un/decrypted
# messages.
message_text = Text(bottom_frame, width=64, height=12)
message_text.grid(row=0, columnspan=2)

# Loops the window indefinitely.
root.mainloop()