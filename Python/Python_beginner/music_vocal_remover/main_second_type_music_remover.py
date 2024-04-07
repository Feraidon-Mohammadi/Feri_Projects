import os
from pydub import AudioSegment
from spleeter.separator import Separator

# Specify the folder where you saved ffmpeg.exe
ffmpeg_folder = r'D:\\Visual studio\\projects python\\Py_beginner IAD\\Py_beginner\\music_vocal_remover\\ff'

# Set the full path to ffmpeg.exe
ffmpeg_exe_path = os.path.join(ffmpeg_folder, 'ff/ffmpeg.exe')
AudioSegment.converter = ffmpeg_exe_path

def remove_vocals(input_path, output_path):
    # Load the MP3 file using pydub
    audio = AudioSegment.from_file(input_path, format="mp3")

    # Save the audio to a temporary WAV file
    temp_wav_file = os.path.join(output_path, "temp_audio.wav")
    audio.export(temp_wav_file, format="wav")

    # Use spleeter to separate vocals and accompaniment
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(temp_wav_file, output_path)

    # Remove the temporary WAV file
    os.remove(temp_wav_file)

if __name__ == "__main__":
    input_file = r'D:\Visual studio\projects python\Py_beginner IAD\Py_beginner\music_vocal_remover\ff\input_file\input_sound.mp3'
    output_path = r'/music_vocal_remover/ff/output_path'

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    output_file_path = os.path.join(output_path, "instrumental.mp3")

    remove_vocals(input_file, output_file_path)
    print(f"Vocals removed, and instrumental saved to {output_file_path}")