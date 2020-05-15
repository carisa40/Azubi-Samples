import datetime
now = datetime.datetime.now()

f= open("hours_worked.txt","a")
f.write("\n")
f.write("Start Time,  End Time,  Wages Earned \n")
f.close()
start_time = input("Hi Nana, enter current time to clock-in using 24hr HH.MM format : \n")
text1 = "New session, You clocked in at : \n"
time1 = now.strftime("%Y-%m-%d %H:%M:%S")
print (text1, time1 )
f= open("hours_worked.txt","a")
f.write("\n")
f.write(text1)
f.write(time1)
f.write("\n")
f.close()

end_time = input ("Hi Nana, enter current time to clockout using 24hr HH.MM format : \n")
text2 = "You clocked out at : \n"
time2 = now.strftime("%Y-%m-%d %H:%M:%S")
print (text2, time2)
f= open("hours_worked.txt","a")
f.write("\n")
f.write(text2)
f.write(time2)
f.write("\n")
f.close()

wages = (float(end_time) - float(start_time)) * 5
text3 = (("You have earned : " + "${:.2f}" + " this period.").format(wages))
print(text3)
f= open("hours_worked.txt","a")
f.write("\n")
f.write(str(text3))
f.write("\n")
f.write("*************************************************************** \n")
f.close()