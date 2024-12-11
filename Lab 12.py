#----------------------------------------------------------
# Name: Aland Adili
# E-mail Address: ava6698@psu.edu
# Class: CMPSC 131 Section
# Lab #12
#----------------------------------------------------------
course_room={
    "SC201":"3004",
    "SC202":"4501",
    "SC301":"6755",
    "SC302":"1244",
    "SC400":"1411",
}
course_instructor={
    "SC201":"Carson",
    "SC202":"Curie",
    "SC301":"Newton",
    "SC302":"Edison",
    "SC400":"Hertz",
}
course_meeting={
    "SC201":"8:00-8:50am",
    "SC202":" 9:00-9:50am",
    "SC301":"10:00-10:50am",
    "SC302":"11:00-11:50am",
    "SC400":" 1:00-1:50pm",
}
print("Course","  Room","  Instructor","  Time")
print("------------------------------------------------------------------------------------------------------------------------------------------------")
for i in course_room:
    print(i,end="    ")
    print(course_room[i],end="    ")
    print(course_instructor[i],end="    " )
    print(course_meeting[i])

find=input("Enter a course number:")
if find in course_room:
    print("The details for course",find,"are:")
    print("Room:",course_room[find])
    print("Instructor:",course_instructor[find])
    print("Time:",course_meeting[find])
else:
    print("The course number is invalid")



