__author__ = 'tarunsharma'
import time
import webbrowser

total_breaks = 1
break_count = 0
print "This program started on "+time.ctime()
while break_count < total_breaks:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=yx7MTyVPNow")
    break_count += 1


