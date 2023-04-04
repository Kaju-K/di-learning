from translate import Translator

translator = Translator(to_lang="en", from_lang="fr")

french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"] 

translation = {}

for word in french_words:
    translation[word] = translator.translate(word)

print(translation)