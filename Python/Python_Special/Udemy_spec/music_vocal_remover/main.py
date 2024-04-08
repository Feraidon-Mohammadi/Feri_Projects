import os
from pydub import AudioSegment
from spleeter.separator import Separator
# pip install sleeter


def remove_vocals(input_path, output_path):
	# Load the MP3 file
	audio = AudioSegment.from_mp3(input_path)
	
	# Save the audio to a temporary WAV file
	temp_wav_file = "temp_audio.wav"
	audio.export(temp_wav_file, format="wav")
	
	# Use spleeter to separate vocals and accompaniment
	separator = Separator('spleeter:2stems')
	separator.separate_to_file(temp_wav_file, output_path)
	
	# Remove the temporary WAV file
	os.remove(temp_wav_file)


if __name__ == "__main__":
	input_mp3 = "input_song.mp3"
	output_path = "output_path"
	
	if not os.path.exists(output_path):
		os.makedirs(output_path)
	
	output_file_path = os.path.join(output_path, "instrumental.mp3")
	
	remove_vocals(input_mp3, output_file_path)
	print(f"Vocals removed and instrumental saved to {output_file_path}")