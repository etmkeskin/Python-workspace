from pytube import YouTube
from pytube.exceptions import VideoUnavailable, RegexMatchError


def download_youtube_video(url, path):
    try:
        print("Creating YouTube object...")
        yt = YouTube(url)
        print(f"Title: {yt.title}")

        print("Getting highest resolution stream...")
        stream = yt.streams.get_highest_resolution()

        print("Downloading video...")
        stream.download(save_path)

        print(f"Video downloaded successfully: {yt.title}")
    except VideoUnavailable:
        print("Error: The video is unavailable.")
    except RegexMatchError:
        print("Error: The video URL is incorrect.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=6gTmyhRM6k0&t=2s"
    save_path = "C:\\Users\\etmke\\Downloads"

    download_youtube_video(video_url, save_path)
