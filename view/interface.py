from controller.controller import Controller

class ConsoleUI:

	def __init__(self):
		self.controller = Controller()
	

	def default_screen(self):
		print("""
		|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|
		|=|             Dictionary            |=|
		|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|
		""")
		print("1. View dictionary")
		print("2. Add Word")
		selection = input(" >> ")

		return selection

	def select_lang(self) -> str:
		lang_dict = self.controller.load_lang()
		
		print("Languages available: ")
		for (key, value) in lang_dict.items():
			print(key + " --- " + value)
		print("Type in the key to continue\n")
		
		lang_input = input("Language: ")
		return lang_input

	def view_dict(self, language: str):
		records = self.controller.load_dict(language)

		for record in records:
			print(record)

	def add_word(self, language: str):
		word = input("Word: ")
		meaning = input("Meaning: ")

		self.controller.add_word(language, word, meaning)

	def entry_point(self):
		while True:
			selection = self.default_screen()
			language = self.select_lang()
			if selection == "1":
				self.view_dict(language)
			elif selection == "2":
				self.add_word(language)
			else:
				print("Sorry, the process is halted")

			