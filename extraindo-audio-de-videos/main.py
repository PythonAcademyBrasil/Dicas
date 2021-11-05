from moviepy.video.io.VideoFileClip import VideoFileClip

# Carrega um arquivo de vídeo
video = VideoFileClip('Linkin_Park_Numb.mp4')

# Passe como parâmetro qual será o arquivo de saída
video.audio.write_audiofile('Linkin_Park_Numb.mp3')

