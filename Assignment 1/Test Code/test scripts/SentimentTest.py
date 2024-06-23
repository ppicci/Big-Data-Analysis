from pathlib import Path

from textblob import TextBlob

with open('../output/test_transcribe/Me at the zoo.txt', 'r', encoding='utf-8') as file:
    text = file.read()

blob = TextBlob(text)
print(blob.sentiment)
print(blob.sentiment.polarity)
print(blob.sentiment.subjectivity)

file_path = '../output/test_sentiment/Me at the zoo - Sentiment.txt'
Path(file_path).parent.mkdir(parents=True, exist_ok=True)

with open(file_path, 'w') as file:
     file.write(str(blob.sentiment))
print(f'Text has been written to {file_path}')