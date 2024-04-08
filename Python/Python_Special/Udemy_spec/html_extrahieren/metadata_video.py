from moviepy.editor import VideoFileClip

def extract_video_metadata(video_path):
    try:
        # Open the video file
        clip = VideoFileClip(video_path)

        # Get video metadata
        metadata = {
            'duration': clip.duration,
            'resolution': clip.size,
            'fps': clip.fps,
            # Add more metadata attributes as needed
        }

        # Close the video file
        clip.close()

        return metadata

    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
video_path = 'path/to/your/video.mp4'
video_metadata = extract_video_metadata(video_path)

if video_metadata:
    print('Video Metadata:')
    for key, value in video_metadata.items():
        print(f'{key}: {value}')
else:
    print('Failed to extract video metadata.')