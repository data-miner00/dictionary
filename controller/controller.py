import json
from model.vocabulary import Vocabulary

class Controller:

	def __init__(self):
		pass


	def load_lang(self) -> dict:
		with open("model/languages.json", "r") as lang_json:
			languages = json.load(lang_json)

		return languages

	def filter_lang(self, lang_input: str) -> str:
		avail_lang = self.load_lang()
		if lang_input in avail_lang:
			return lang_input
		else:
			return "not found"

	def load_dict(self, language: str) -> [str]:
		path = "database/" + language + ".txt"

		try:
			with open(path, "r", encoding="utf-8") as f:
				records = f.readlines()
				print("Successfully loaded " + language + ".txt data")
		except FileNotFoundError:
			print("File not found!")

		return records

		
	def add_word(self, language: str, word: str, meaning: str):
		path = "database/" + language + ".txt"

		with open(path, "a+", encoding="utf-8") as f:
			f.write(word + ":" + meaning)

		print("Adding done")
	