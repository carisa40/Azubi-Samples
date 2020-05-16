from datetime import datetime
from datetime import timedelta
import datetime
import time
now = datetime.datetime.now()
t = time.localtime()
"""
f= open("hours_worked.csv","a")

text = ' , Start Time, End Time, Total Time (hrs.mins), Wages Earned ($), '
text_f = text.split(",")
f.write(str(text_f))
f.write('\n')
f.close()
"""

start_time = input("Hi Nana, type \'start\' to clock-in \n")
text1 = "New session, You clocked in at : \n"
time1 = now.strficoytime("%Y-%m-%d %H:%M:%S")
print (text1, time1 )
#time3 = int(datetime.timedelta(now))
time3 = now.strftime('%H.%M')



end_time = input ("Hi Nana, type \'end\' to clock out \n")
text2 = "End session, You clocked out at : \n"
#print (text2, time2)
time2 = time.strftime("%Y-%m-%d %H:%M:%S")
time4 = time.strftime('%H.%M')
print(time2)
#time4 = int(datetime.timedelta(t))

total_time = float(time4 )- float(time3)
wages = (total_time) * 5

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