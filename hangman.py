# Hangman game with tkinter
# @author: Kaendass
# 16.05.2021


from tkinter import *
from PIL import Image, ImageTk
import random


file = open("words.txt", "r")
word_list = []
for item in file:
	word_list.append(item.strip().upper())

existing_letter = []
counter = 0


class Root:
	
	def __init__(self):

		self.root = Tk()
		self.root.geometry("1920x1080")
		self.root.title("Hangman by Kaendass")
		self.root.config(bg="black")
		
		# =====================================================================================================
		
		self.welcome = Image.open("welcome.png")
		self.welcome = ImageTk.PhotoImage(self.welcome)

		self.play = Image.open("play.png")
		self.play = ImageTk.PhotoImage(self.play)

		self.quit = Image.open("quit.png")
		self.quit = ImageTk.PhotoImage(self.quit)

		self.restart = Image.open("restart.png")
		self.restart = ImageTk.PhotoImage(self.restart)

		self.empty = Image.open("empty.png")
		self.empty = ImageTk.PhotoImage(self.empty)

		self.empty_won = Image.open("empty_won.png")
		self.empty_won = ImageTk.PhotoImage(self.empty_won)

		self.howtoplay = Image.open("howtoplay.png")
		self.howtoplay = ImageTk.PhotoImage(self.howtoplay)

		self.stage1 = Image.open("stage1.png")
		self.stage1 = ImageTk.PhotoImage(self.stage1)

		self.stage2 = Image.open("stage2.png")
		self.stage2 = ImageTk.PhotoImage(self.stage2)

		self.stage3 = Image.open("stage3.png")
		self.stage3 = ImageTk.PhotoImage(self.stage3)

		self.stage4 = Image.open("stage4.png")
		self.stage4 = ImageTk.PhotoImage(self.stage4)

		self.stage5 = Image.open("stage5.png")
		self.stage5 = ImageTk.PhotoImage(self.stage5)

		self.stage6 = Image.open("stage6.png")
		self.stage6 = ImageTk.PhotoImage(self.stage6)

		self.stage1_won = Image.open("stage1_won.png")
		self.stage1_won = ImageTk.PhotoImage(self.stage1_won)

		self.stage2_won = Image.open("stage2_won.png")
		self.stage2_won = ImageTk.PhotoImage(self.stage2_won)

		self.stage3_won = Image.open("stage3_won.png")
		self.stage3_won = ImageTk.PhotoImage(self.stage3_won)

		self.stage4_won = Image.open("stage4_won.png")
		self.stage4_won = ImageTk.PhotoImage(self.stage4_won)

		self.stage5_won = Image.open("stage5_won.png")
		self.stage5_won = ImageTk.PhotoImage(self.stage5_won)

		# =====================================================================================================

		self.left_frame = Frame(self.root, bg="black")
		self.right_frame = Frame(self.root, bg="black")
		self.underscore_frame = Frame(self.root, bg="black")
		self.bottom_frame = Frame(self.root, bg="black")

		# =====================================================================================================

		self.left_label = Label(self.left_frame, bg="black", image=self.welcome)
		self.left_label.pack()

		# =====================================================================================================

		self.play_button = Button(self.right_frame, image=self.play, 
			bd=0, relief=FLAT, command=self.play_game, bg="black", activebackground="black")
		self.play_button.pack(padx=45, pady=(80,20))

		self.quit_button = Button(self.right_frame, image=self.quit, 
			bd=0, relief=FLAT, command=self.root.destroy, bg="black", activebackground="black")
		self.quit_button.pack(padx=45, pady=(0,20))

		self.restart_button = Button(self.right_frame, image=self.restart, state=DISABLED,
			bd=0, relief=FLAT, command=self.restart_game, bg="black", activebackground="black")
		self.restart_button.pack(padx=45)

		# =====================================================================================================

		self.howtoplay_label = Label(self.underscore_frame, image=self.howtoplay, bg="black")
		self.howtoplay_label.grid()

		self.underscore_text = StringVar()

		self.underscores = Label(self.underscore_frame, textvariable=self.underscore_text, font=("Ink Free",100,"bold"),
		 bg="black", fg="white")

		self.letters = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8]

		self.letters[0] = Button(self.bottom_frame, text="A", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("A",0))

		self.letters[1] = Button(self.bottom_frame, text="B", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("B",1))

		self.letters[2] = Button(self.bottom_frame, text="C", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("C",2))

		self.letters[3] = Button(self.bottom_frame, text="D", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("D",3))

		self.letters[4] = Button(self.bottom_frame, text="E", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("E",4))

		self.letters[5] = Button(self.bottom_frame, text="F", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("F",5))

		self.letters[6] = Button(self.bottom_frame, text="G", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("G",6))

		self.letters[7] = Button(self.bottom_frame, text="H", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("H",7))

		self.letters[8] = Button(self.bottom_frame, text="I", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("I",8))

		self.letters[9] = Button(self.bottom_frame, text="J", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("J",9))

		self.letters[10] = Button(self.bottom_frame, text="K", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("K",10))

		self.letters[11] = Button(self.bottom_frame, text="L", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("L",11))

		self.letters[12] = Button(self.bottom_frame, text="M", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("M",12))

		self.letters[13] = Button(self.bottom_frame, text="N", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("N",13))

		self.letters[14] = Button(self.bottom_frame, text="O", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("O",14))

		self.letters[15] = Button(self.bottom_frame, text="P", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("P",15))

		self.letters[16] = Button(self.bottom_frame, text="Q", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("Q",16))

		self.letters[17] = Button(self.bottom_frame, text="R", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("R",17))

		self.letters[18] = Button(self.bottom_frame, text="S", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("S",18))	

		self.letters[19] = Button(self.bottom_frame, text="T", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("T",19))

		self.letters[20] = Button(self.bottom_frame, text="U", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("U",20))

		self.letters[21] = Button(self.bottom_frame, text="V", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("V",21))

		self.letters[22] = Button(self.bottom_frame, text="W", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("W",22))

		self.letters[23] = Button(self.bottom_frame, text="X", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("X",23))

		self.letters[24] = Button(self.bottom_frame, text="Y", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("Y",24))

		self.letters[25] = Button(self.bottom_frame, text="Z", font=("Ink Free",30,"bold"),bg="white", 
			bd=0, relief=FLAT, width=4,activebackground="white", command=lambda:self.get_letter("Z",25))

		self.left_frame.grid(row=0, column=0, sticky="nw")
		self.right_frame.grid(row=0, column=1, sticky="ne")
		self.underscore_frame.grid(row=1, column=0, columnspan=2, sticky="ew")
		self.bottom_frame.grid(row=2, column=0, columnspan=2,padx=315)

		mainloop()

		
	def play_game(self):
		
		global word
		global text
		
		self.underscores.config(fg="white")
		self.restart_button.config(state=ACTIVE)
		
		word = random.choice(word_list)
		text = "_ " * len(word)
		
		self.underscore_text.set(text)
		self.left_label.config(image=self.empty)
		self.play_button.config(state=DISABLED)

		self.letter_list = [i for i in word]
		self.letter_list2 =	[i for i in word]

		self.underscore_text.set(text)
		self.howtoplay_label.grid_forget()
		self.underscores.pack()

		index = 0
		
		for row in range(1,3):
			for column in range(13):
				self.letters[index].grid(row=row, column=column, padx=(0,2), 
					pady=(0,2),sticky="ew")
				index += 1


	def restart_game(self):
		
		global existing_letter
		global counter
		
		index = 0
		for row in range(1,3):
			for column in range(13):
				self.letters[index].config(state=ACTIVE, bg="white")
				index += 1
		existing_letter.clear()
		counter = 0
		word_list.remove(word)
		self.play_game()


	def get_letter(self, letter, button_index):
		
		global word
		global text
		global existing_letter
		global counter
		
		existing_letter.append(letter)
		self.letters[button_index].config(state=DISABLED, bg="light gray")

		if letter in word:
			for index in range(len(self.letter_list2)):
				if not self.letter_list[index] in existing_letter:
					self.letter_list[index] = "_ "

			text = "".join(self.letter_list)
		else:
			counter += 1
			if counter == 1:
				self.left_label.config(image=self.stage1)

			elif counter == 2:
				self.left_label.config(image=self.stage2)

			elif counter == 3:
				self.left_label.config(image=self.stage3)

			elif counter == 4:
				self.left_label.config(image=self.stage4)

			elif counter == 5:
				self.left_label.config(image=self.stage5)

			elif counter == 6:
				self.left_label.config(image=self.stage6)
				self.underscores.config(fg="#ff0000")
				self.disable_buttons()
				
		if text == word:
			if counter == 1:
				self.left_label.config(image=self.stage1_won)
				self.disable_buttons()
				self.underscores.config(fg="#18ff00")

			elif counter == 2:
				self.left_label.config(image=self.stage2_won)
				self.disable_buttons()
				self.underscores.config(fg="#18ff00")

			elif counter == 3:
				self.left_label.config(image=self.stage3_won)
				self.disable_buttons()
				self.underscores.config(fg="#18ff00")

			elif counter == 4:
				self.left_label.config(image=self.stage4_won)
				self.disable_buttons()
				self.underscores.config(fg="#18ff00")

			elif counter == 5:
				self.left_label.config(image=self.stage5_won)
				self.disable_buttons()
				self.underscores.config(fg="#18ff00")
			
			else:
				self.left_label.config(image=self.empty_won)
				self.disable_buttons()
				self.underscores.config(fg="#18ff00")

		self.letter_list = self.letter_list2.copy()
		
		if counter != 6:
			self.underscore_text.set(text)
		else:
			self.underscore_text.set(word)
			counter = 0

	
	def disable_buttons(self):
		index = 0
		for row in range(1,3):
			for column in range(13):
				self.letters[index].config(state=DISABLED)
				index += 1


if __name__ == '__main__':

	root = Root()
	file.close()