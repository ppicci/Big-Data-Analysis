from pytube import YouTube

url = "https://www.youtube.com/watch?v=jNQXAC9IVRw"
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
print(f"Downloading video: {yt.title}")
stream.download(output_path="video_output")
print(f"Download completed: {yt.title}")
