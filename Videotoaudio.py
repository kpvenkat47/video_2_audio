import moviepy.editor as m
path = input("Enter Path:") #file path on our pc
if ".mp4" in path:
    file = m.VideoFileClip(path)
    file.audio.write_audiofile(r"E:\video\nmv.mp3") #save location
else:
    print("check the path")
