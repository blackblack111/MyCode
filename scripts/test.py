from moviepy.editor import *
from moviepy.video.tools.credits import credits1

# Load the mountains clip, cut it, slow it down, make it look darker
clip = (VideoFileClip('NNRC.flv', audio=False)
        .subclip(1, 10))
my_audioclip = AudioFileClip('3023706833.mp3').subclip(0, 9)
videoclip2 = clip.set_audio(my_audioclip)
# Save the first frame to later make a mask with GIMP (only once)
# ~ clip.save_frame('../../credits/mountainMask2.png')

# clip = ImageClip('RC.jpg')

# Load the mountain mask made with GIMP
mountainmask = ImageClip('RC.png', ismask=True)

# Generate the credits from a text file
# credits = credits1('RC.txt', 3 * clip.w / 4,font='simsun.ttc')
# scrolling_credits = credits.set_pos('right',lambda t: ('center', -10 * t))

with open('RC.txt','r',encoding='utf-8') as f:
    text = f.read()

txtclip = TextClip(text, font='JingDianWeiBeiJian-1.ttf', fontsize=40, color='black', transparent=True).set_duration(5).set_fps(clip.fps)

# SCROLL THE TEXT IMAGE BY CROPPING A MOVING AREA

# txt_speed = 27
# fl = lambda t:-10*t
# moving_txt= txtclip.fl(fl, apply_to=['mask'])

# Make the credits scroll. Here, 10 pixels per second
final = CompositeVideoClip([videoclip2,
                            txtclip.set_pos((0.2,0.9),relative=True),
                            clip.set_mask(mountainmask)])

# txtclip = TextClip(text, font='simsun.ttc', fontsize=18, color='blue').set_duration(5).resize((clip.size[0], clip.size[1]))
# final = CompositeVideoClip([clip,
#                             txtclip.set_pos('right'),
#                             clip.set_mask(mountainmask)])

final.save_frame("frame.png")
# final.save_frame("frame2.png", t=2)
# final.subclip(0, 5).write_videofile("New.mp4",fps=24)

