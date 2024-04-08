import os
from pytube import YouTube
# ---> pip install pytube


def download_video(url, output_path="./video/videos"):
    try:
        # Create output directory if not exists
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Get YouTube video
        video = YouTube(url)

        # Select the highest resolution stream
        stream = video.streams.get_highest_resolution()

        # Download the video
        stream.download(output_path)

        print(f"Video downloaded successfully: {video.title}")

    except Exception as e:
        print(f"Error: {e}")

# Example usage ---> usually working with youtube
video_url = "https://s15.trafficdeposit.com/vidi/j21m7929zh180t5gze6l4sze2g0r8/CPDPE8ixHuLpnHB51aK_Ug/1702131291/57d2f694dd228/5f169f861eaa7.vid"
# video_url = "https://www.youtube.com/watch?v=your_video_id"
download_video(video_url)
