from pathlib import Path
from googletrans import Translator


with open('../output/test_transcribe/Me at the zoo.txt', 'r', encoding='utf-8') as file:
    text = file.read()

translator = Translator()
text_translated = translator.translate(text, src='en', dest='es')
print(text_translated.text)

file_path = '../output/test_translate/Me at the zoo - español.txt'
Path(file_path).parent.mkdir(parents=True, exist_ok=True)

with open(file_path, 'w') as file:
     file.write(text_translated.text)
print(f'Text has been written to {file_path}')