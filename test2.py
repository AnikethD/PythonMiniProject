import time
import webbrowser
import random



sec=0
hour=input('Enter your current Hour :')
mini=input('Enter your current Minute :')
h=input('Hour of Alarm :')
m=input('Minute of Alarm :')
lst=['https://www.youtube.com/watch?v=papuvlVeZg8','https://www.youtube.com/watch?v=k2qgadSvNyU','https://www.youtube.com/watch?v=wFhs7WVvuXk&list=PL9LUD5Kp855IUocbAjUd6Du9UmvZrbKk7','https://www.youtube.com/watch?v=KIW_Ca8OWTo','https://www.youtube.com/watch?v=eVTXPUF4Oz4','https://www.youtube.com/watch?v=kXYiU_JCYtU']
while True :
    print(str(hour)+":"+str(mini)+":"+str(sec))
    sec+=1
    time.sleep(1)
    if h==hour and m==mini and sec==10 :
        random.shuffle(lst)
        for i in lst:
            x=webbrowser.open(i)
            break
    if sec==60:
        sec=0
        mini+=1
    if mini==60:
            mini=0
            hour+=1
    if hour==24:
        hour=0
   
    
