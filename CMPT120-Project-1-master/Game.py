# CMPT 120L 113
# Andrew Mallach
# 10 Sep 2018
###


score = 0

 

# show game title
print("\nMarist Mayhem\n"
      "\n========\n"
      )
name=input("Please enter your name     ")
major=input("Please enter your major    ")



# show game introduction
print("\nWell, " + name + ", the day has finally arrived. August 27th, 2018. After one last\n"
      " \ngrueling year at high school, AP exams, and standardized tests,\n"
      " \nYou have finally made it to college. It only gets better from here.\n"
      " \nYou finally feel like your life is in your own hands. You feel\n"
      " \nlike you are finally an adult. As the sun rises, you start to\n"
      " \nfrantically look over your schedule, anxious about the fact that\n"
      " \nyour new chapter in your academic career is about to begin. In\n"
      " \nyour nervousness however, you fail to realize that your only class\n"
      " \ntoday starts at 2 PM. You decide to go back to bed, browsing social\n"
      " \nmedia and still worrying about the coming day. You decide to try\n"
      " \nand take it easy for a bit and take a nap.\n")

# prompt the user
input("\n<Press Enter to continue...>\n")

# show current situation
print("\nOh no! You've really messed up now! \n"
          "\nIt's only the first day of school and \n"
          "\nyou overslept for your first class, \n"
      "\nand it's an afternoon class! Not many \n"
      "\nexcuses you can come up with to get out \n"
      "\nof that. Regardless, you think that \n"
      "\nyou might get some slack because it's\n "
      "\nonly the first day, and you head off to class.\n")

# show the current score

print("Your score is " + str(score))

# prompt the user
input("\n<Press Enter to continue...>\n")

# show the current location
print("\nYou show up about 10 minutes late. The teacher doesn't seem \n"
      "\ntoo pleased. You tell her that you were trying to find the right\n"
      "\nroom for a while, and the teacher buys it. You spend the rest\n"
      "\nof the class time as normal.\n")

# show the current score
score+=5
print("Your score is " + str(score))

# same as above
input("\n<Press Enter to continue...>\n")

# same as above
print("\nYou go back to your dorm feeling guilty about what\n"
      "\nhappened. You were told that you have a quiz in the class\n"
      "\nnext week. You told yourself that you can't mess around\n"
      "\nwith your sleep schedule anymore.\n")

# same as above
score+=5
print("Your score is " + str(score))

# again...
input("\n<Press Enter to continue...>\n")

# again...
print("\nThursday arrives. You have been diligently keeping up \n"
      "\nwith all of your other classes. You start to learn more \n"
      "\nmaterial for this upcoming quiz for Monday, and you feel \n"
      "\nlike you can ace it given time.\n")

# again...
score+=5
print("Your score is " + str(score))

# yet again...
input("\n<Press Enter to continue...>\n")

# yet again...
print("\nMonday arrives. You didn't study for a single minute. You've spent \n"
      "\nall of your time playing video games and going on your phone \n"
      "\nYou try to get your roommate to help you before the quiz, but \n"
      "\nhe doesn't even have the same class. You decide the only possible \n"
      "\nway to do well is to take pictures of the textbook with your phone \n"
      "\nand use it during the exam. That way, the material is readily \n"
      "\navailable to use. You go to class, ready to cheat.\n")

# yet again...
score+=5
print("Your score is " + str(score))

# one last time...
input("\n<Press Enter to continue...>\n")

# show game ending
print("\nYou were caught cheating by your teacher. You didn't even try to hide \n"
      "\nthe fact that you were using your phone under the table. You meet with \n"
      "\nthe college President and are promptly kicked out. Your dreams of \n"
      "\nbecoming a " + major + " major are shattered.\n"
      "\nGame Over!\n")

# show credits
print("\nCopyright (c) 2016-2018 Andrew Mallach, andrew.mallach1@marist")


