import webbrowser
import time

total_breaks = 1
break_count = 0
print ("Este programa iniciou em "+time.ctime())
while(break_count < total_breaks) :
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/whinderssonnunes")
    break_count = break_count + 1

    
