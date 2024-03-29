from moviepy.video.io.VideoFileClip import VideoFileClip

# Set the input and output file paths
input_file = 'vvideo.mp4'
output_file = 'vvideoaudio.mp3'

# Open the video file using moviepy
clip = VideoFileClip(input_file)

# Write the audio of the video to an mp3 file
clip.audio.write_audiofile(output_file)


# # This line imports the os library, which allows us to run command-line commands in Python.

# This code sets the input and output file paths. The input file is the video file that you want to convert to an mp3 file. The output file is the location where you want to save the mp3 file.
# You need to replace 'path/to/input_video.mp4' and 'path/to/output_audio.mp3' with the actual path of the input video file and the desired path where you want your output mp3 file to be saved.

# This line is where the magic happens! This line uses the os.system() function to run the ffmpeg command to convert the video file to an mp3 file.
# The command takes the input video file and converts it to an mp3 file and save the output mp3 file in the location specified in the script.
# -i option is used to set the input file,-vn option is used to disable the video output, -ab 128k is used to set the audio bitrate to 128 kbps, -ar 44100 is used to set the audio sample rate to 44100 Hz and -y is used to overwrite the output file if it already exists.

# Please note that you need to have ffmpeg installed on your machine for this to work.
# And this is how you can convert a video to an mp3 file using a simple Python script with ffmpeg command.
# If you have any question, please let me know.