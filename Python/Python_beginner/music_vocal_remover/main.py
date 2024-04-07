import _winapi
import os
from pydub import AudioSegment
from spleeter.separator import Separator
from pydub import AudioSegment
# pip install spleeter
# pip install pydub



# Specify the folder where you saved ffmpeg.exe
ffmpeg_folder = r'D:\Visual studio\projects python\Py_beginner IAD\Py_beginner\music_vocal_remover\ff'


executable = r'D:\Visual studio\projects python\Py_beginner IAD\Py_beginner\music_vocal_remover\ff\ffmpeg.exe'


# Specify command-line arguments
args = 'arguments if any'

# Set up other parameters for CreateProcess
lpProcessAttributes = None
lpThreadAttributes = None
bInheritHandles = False
dwCreationFlags = 0
lpEnvironment = None
lpCurrentDirectory = None
lpStartupInfo = _winapi.STARTUPINFO()
lpProcessInformation = _winapi.PROCESS_INFORMATION()

# Try to create the process
success = _winapi.CreateProcess(
    executable,
    args,
    lpProcessAttributes,
    lpThreadAttributes,
    bInheritHandles,
    dwCreationFlags,
    lpEnvironment,
    lpCurrentDirectory,
    lpStartupInfo,
    lpProcessInformation
)

if success:
    hp, ht, pid, tid = lpProcessInformation
    print(f"Process created with PID: {pid}")
else:
    print(f"Failed to create process. Error code: {_winapi.GetLastError()}")







# Set the full path to ffmpeg.exe
ffmpeg_exe_path = os.path.join(ffmpeg_folder, 'ffmpeg.exe')
AudioSegment.converter = ffmpeg_exe_path

def remove_vocals(input_path, output_path):
    # Load the MP3 file
    audio = AudioSegment.from_mp3(input_path)

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
    output_path = r'D:\Visual studio\projects python\Py_beginner IAD\Py_beginner\music_vocal_remover\ff\output_path'

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    output_file_path = os.path.join(output_path, "instrumental.mp3")

    remove_vocals(input_file, output_file_path)
    print(f"Vocals removed, and instrumental saved to {output_file_path}")