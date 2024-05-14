from googletrans import Translator

translator = Translator()
text = "insert text here"  # Replace this with the text you want to translate
out = translator.translate(text, dest='en') #Replace en with the language you want to
print(out.text)