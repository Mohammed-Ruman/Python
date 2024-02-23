# 12. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
# Take following input from user
# Number of classes held
# Number of classes attended.
# And print
# percentage of class attended
# Is student is allowed to sit in exam or not.


classes_held=int(input("Number of Classes Held? "))
classes_attend=int(input("Number of Classes Attended? "))

perc=classes_attend/classes_held *100

if perc > 75:
    print("Eligible")
else:
    print("Not Eligible")