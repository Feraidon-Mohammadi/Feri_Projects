room = "fereydoun_mohammadi"
print(room)
# take the itmes in side the room


print(len(room))
# take the all alphabets .how many are they


print(room[2])
# take the needed alphabet with numbers from front


print(room[-2])
# take the alphabet from end


print(room[0:4])
# find the alphabets between 0-4


print(room[:])
# needed alphabets from first to last


print(room[:-5])
# find alphabets from first to alphabets 5 from ende of the string


course = "python \" programming"
print(course)
# add " between two string text


course = 'python \' programming'
print(course)
# add ' between two string text


course = "python \\ programming"
print(course)
# add \ between two string text


course = "python \n programming"
print(course)
# type from first part of the string text up and second part down or next line


course = "python \t programming"
print(course)
# add a tab or 3 space between to string text


first = "coding"
seperator = " "
last = "is cool"
full = first + seperator + last  # full = f"{first} {seperator} {last}"
print(full)
# connect two string test with another string text


first2 = "coding"
seperator2 = " "
last2 = "is cool"
full2 = f"{first2}{seperator2}{last2}"
print(full2)
# its same like last code up 58


first3 = "coding"
seperator3 = " "
last3 = "is cool"
full3 = f"{first3}\n{seperator3}\n{last3}"
print(full3)
# write the string text to in the next line


course = "fereydoun programmer"
course_capital = course.upper()
# write string text to BIG alphabet
print(course)
print(course_capital)


course = "alireza programmer"
course_capital = course.lower()
print(course_capital)
# write string text small alphabet


course = " arash programmer"
print(course.strip())
# write first big alphabet
print(course.upper())
# write small alphabet

course = "feri program writer "
print(course.title())
# write first string text big every part
