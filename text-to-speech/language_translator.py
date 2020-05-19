from translate import Translator

user_input = str(input("Enter your text to convert it to German: "))   #Get input from speech to text file.

translator = Translator(to_lang='German')
translation = translator.translate(user_input)
print(translation)