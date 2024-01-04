from pytube import YouTube 
import os 
  
url = input('Please, type the youtube URL: \n\n')
yt = YouTube(str(url)) 
  
video = yt.streams.filter(only_audio=True).first() 
  
destination = './output/'
out_file = video.download(output_path=destination) 
  
base, ext = os.path.splitext(out_file) 
new_file = base + '.mp3'
os.rename(out_file, new_file) 
  
print(yt.title + " downloaded successfully.")