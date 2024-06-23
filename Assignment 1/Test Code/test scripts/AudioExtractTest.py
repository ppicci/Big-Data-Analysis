import moviepy.editor as mp
from pathlib import Path

output_folder = Path("../output/test_audio")
output_folder.mkdir(parents=True, exist_ok=True)

video = mp.VideoFileClip("../output/test_video/Me at the zoo.mp4")
video.audio.write_audiofile(str(output_folder) + "/Me at the zoo.wav")
