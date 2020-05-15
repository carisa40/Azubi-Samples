from datetime import datetime
import time
now = datetime.now()
t = time.localtime()
"""
f= open("hours_worked.csv","a")

text = ' , Start Time, End Time, Total Time (hrs), Wages Earned ($), '
text_f = text.split(",")
f.write(str(text_f))
f.write('\n')
f.close()
"""

start_time = input("Hi Nana, enter current time to clock-in using 24hr HH.MM format : \n")
text1 = "New session, You clocked in at : \n"
time1 = now.strftime("%Y-%m-%d %H:%M:%S")
print (text1, time1 )


end_time = input ("Hi Nana, enter current time to clockout using 24hr HH.MM format : \n")
text2 = "You clocked out at : \n"
#time2 = now.strftime("%Y-%m-%d %H:%M:%S")
#print (text2, time2)
time2 = time.strftime("%Y-%m-%d %H:%M:%S")
print(time2)

total_time = float(end_time) - float(start_time)
wages = (float(end_time) - float(start_time)) * 5

formatted_time = "{:.2f}".format(total_time)
formatted_wage = "{:.2f}".format(wages)
text3 = (("You have worked " + "{:.2f} hours " + "and earned : " + "${:.2f}" + " this period.").format(total_time,wages))
print(text3)
f= open("hours_worked.csv","a")

text4 = [' ', str(time1), str(time2), str(formatted_time), str(formatted_wage), ' ']
[i.split(',', 1)[0] for i in text4]
f.write(str(text4))
f.write('\n')
f.close()