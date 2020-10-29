import json
from model.vocabulary import Vocabulary

class Controller:

	# Constructor
	def __init__(self):
		pass

	# ( Main methods
	# ========================================= #
	# Creating or appending to a file
	def add_word(self, language: str, word: str, meaning: str):
			path = "database/" + language + ".txt"

			with open(path, "a+", encoding="utf-8") as f:
				f.write(word + ":" + meaning + "\n")

			print("Adding done")

	# Load dictionary into list of strings
	def load_dict(self, language: str) -> [str]:
		path = "database/" + language + ".txt"

		try:
			with open(path, "r", encoding="utf-8") as f:
				records = f.readlines()
				print("Successfully loaded " + language + ".txt data")
		except FileNotFoundError:
			print("File not found!")

		return records

	# ( Utility methods
	# ========================================= #
	# Load the language into dictionary
	def load_lang(self) -> dict:
		with open("model/languages.json", "r") as lang_json:
			languages = json.load(lang_json)

		return languages

	# Filter the input for language
	def filter_lang(self, lang_input: str) -> str:
		avail_lang = self.load_lang()
		if lang_input in avail_lang:
			return lang_input
		else:
			return "not found"
