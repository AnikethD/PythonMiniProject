import time
import webbrowser as wb
import random
import datetime as dt



try :
    print('This Clock Runs in 24H Format')
    
    now=dt.datetime.now()
    hour=now.hour
    mini=now.minute
    sec=now.second

    
    h=input('Hour of Alarm :')
    if h>24:
        raise ValueError("It has to be less than 24")
    m=input('Minute of Alarm :')
    if m>60:
        raise ValueError("It has to be less than 60")

    
    while True :
        print(str(hour)+":"+str(mini)+":"+str(sec))
        sec+=1
        time.sleep(1)


        if h==hour and m==mini and sec==10 :
           line=random.choice(open('url.txt','r').readlines())
           x=wb.open(line)
        if sec==60:
            sec=0
            mini+=1
        if mini==60:
                mini=0
                hour+=1
        if hour==24:
            hour=0


            
except Exception as e:
    print(e)
            
   
    
