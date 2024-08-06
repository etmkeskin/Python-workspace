from pytube import YouTube


def download_youtube_video(url, save_path):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream available
        stream = yt.streams.get_highest_resolution()

        # Download the video to the specified path
        stream.download(save_path)

        print(f"Video downloaded successfully: {yt.title}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # URL of the YouTube video to download
    video_url = "https://www.youtube.com/watch?v=9PN_cHPwaGY&pp=ygURZmVuZXJiYWjDp2UgbGlsbGU%3D"

    # Path to save the downloaded video
    save_path = "C:\\Users\\etmke\\Downloads"

    # Download the video
    download_youtube_video(video_url, save_path)
