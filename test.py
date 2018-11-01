import datetime
import webbrowser
import random



th=datetime.datetime.today().hour
tm=datetime.datetime.today().minute
h=input('hour')
m=input('mintue')
lst=['https://www.youtube.com/watch?v=kXYiU_JCYtU','https://www.youtube.com/watch?v=eVTXPUF4Oz4','https://www.youtube.com/watch?v=ScNNfyq3d_w']
if h==th and m==tm :
    url=random.shuffle(lst)
    for i in lst:
            x=webbrowser.open(i)
            
            

