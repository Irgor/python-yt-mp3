from pytube import YouTube 
import os 
  
urls = open("urls.txt", "r")
for url in urls: 
    if len(url) > 0:
        yt = YouTube(str(url)) 
    
        video = yt.streams.filter(only_audio=True).first() 
        
        destination = './output/'
        out_file = video.download(output_path=destination) 
        
        base, ext = os.path.splitext(out_file) 
        new_file = base + '.mp3'
        os.rename(out_file, new_file) 
        
        print(yt.title + " downloaded successfully.")
        
print('all songs downloaded!')