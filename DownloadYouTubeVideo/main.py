import pytube

# Input the YouTube URL
link = input("Enter the YouTube URL: ")

# Create a YouTube object
yt = pytube.YouTube(link)

# Choose the stream with the highest resolution (video and audio)
stream = yt.streams.get_highest_resolution()

# Download the video
stream.download()

print("Download completed for", yt.title)



