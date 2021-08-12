from moviepy.editor import *


clip = (VideoFileClip('NNRC.flv', audio=False)
        .subclip(0, 20))
w,h = clip.size

my_audioclip = AudioFileClip('3023706833.mp3').subclip(0, 20)
videoclip2 = clip.set_audio(my_audioclip)

mountainmask = ImageClip('RC.png', ismask=True)


with open('RC.txt','r',encoding='utf-8') as f:
    text = f.read()


txtclip = TextClip(text, font='JingDianWeiBeiJian-1.ttf', fontsize=50, color='black', transparent=True,align='East',size=clip.size)


final = CompositeVideoClip([videoclip2,
                            txtclip.set_pos(lambda t:('right',h-40-40*t)),
                            clip.set_mask(mountainmask)])


# final.save_frame("frame.png")
# final.save_frame("frame2.png", t=2)
final.subclip(0, 20).write_videofile("New.mp4")

