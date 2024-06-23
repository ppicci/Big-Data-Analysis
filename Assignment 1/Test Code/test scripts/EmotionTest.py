from pathlib import Path
import spacy, nltk
from nrclex import NRCLex

nlp = spacy.load('en_core_web_sm')
nltk.download('punkt')  # needed if the libraries are not already downloaded

with open('../output/test_transcribe/Me at the zoo.txt', 'r', encoding='utf-8') as file:
    text = file.read()

doc = nlp(text)

full_text = ' '.join([sent.text for sent in doc.sents])

emotion = NRCLex(text)

print("Detected Emotions and Frequencies:")
print(emotion.affect_frequencies)

file_path = '../output/test_emotion/Me at the zoo - emotion.txt'
Path(file_path).parent.mkdir(parents=True, exist_ok=True)

with open(file_path, 'w') as file:
     file.write(str(emotion.affect_frequencies))
print(f'Text has been written to {file_path}')
