from controller.controller import Controller

class ConsoleUI:

	# Constructor
	def __init__(self):
		self.controller = Controller()
	
	# ( Display + get inputs
	# ========================================= #
	# Display screen with get selection
	def default_screen(self) -> None:
		print("""
		|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|
		|=|             Dictionary            |=|
		|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|
		""")
		print("1. View dictionary")
		print("2. Add Word")
		selection = input(" >> ")

		return selection

	# Display screen with get language
	def select_lang(self) -> str:
		lang_dict = self.controller.load_lang()
		
		print("Languages available: ")
		for (key, value) in lang_dict.items():
			print(key + " --- " + value)
		print("Type in the key to continue\n")
		
		lang_input = input("Language: ")
		return lang_input

	# ( Main methods
	# ========================================= #
	# Display the selected dictionary
	def view_dict(self, language: str) -> None:
		records = self.controller.load_dict(language)

		for index, record in enumerate(records, start=0):
			self.pretty_print(index, record)

	# Adding a vocabulary into file
	def add_word(self, language: str) -> None:
		word = input("Word: ")
		meaning = input("Meaning: ")

		self.controller.add_word(language, word, meaning)

	# ( Initiate methods
	# ========================================= #
	def entry_point(self) -> None:
		while True:
			selection = self.default_screen()
			language = self.select_lang()
			if selection == "1":
				self.view_dict(language)
			elif selection == "2":
				self.add_word(language)
			else:
				print("Sorry, the process is halted")

			