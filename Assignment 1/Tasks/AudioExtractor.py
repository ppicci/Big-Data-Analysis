import moviepy.editor as mp
from pathlib import Path
import time

def audio_extractor(file):
    output_folder = Path("Audio")/file.stem
    output_folder.mkdir(parents=True, exist_ok=True)
    video = mp.VideoFileClip(f"{file}")
    video.audio.write_audiofile(f"{output_folder}/{file.stem}.wav")

def serial_runner():
    folder = Path("Videos")
    start = time.perf_counter()
    for file in folder.glob('*.mp4'):
        audio_extractor(file)
    end = time.perf_counter()
    print(f"Finished in {end - start:.2f} seconds")


if __name__ == "__main__":
    serial_runner()


