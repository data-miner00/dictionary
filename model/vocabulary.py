
class Vocabulary:

	# constructor
	def __init__(self, lang: str, word: str, meaning: str, example: str = ""):
		self.lang = lang
		self.word = word
		self.meaning = meaning
		self.example = example

		print('vocabulary object ' + self.word + ' initiated.')

	

