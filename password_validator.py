# Program 2: Password validator
# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)

# Tip: loop through each character of the input then process it letter by letter

import re

print("𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗦𝗲𝗰𝘂𝗿𝗲 𝗣𝗮𝘀𝘀𝘄𝗼𝗿𝗱 𝗩𝗮𝗹𝗶𝗱𝗮𝘁𝗼𝗿🛡️\n")
print("Make a secure password with these suggestions:")
print("• greater than 15 letters")
print("• at least 1 capital letter")
print("• at least 1 one number")
print("• at least 1 special character\n")

pass_input = input("𝗘𝗻𝘁𝗲𝗿 𝘁𝗵𝗲 𝗽𝗮𝘀𝘀𝘄𝗼𝗿𝗱 𝘆𝗼𝘂 𝘁𝗵𝗮𝘁 𝘆𝗼𝘂 𝗱𝗲𝘀𝗶𝗿𝗲: \n")

while True:  
    if (len(pass_input)<15):
        flag = -1
        break
    elif not re.search("[a-z]", pass_input):
        flag = -1
        break
    elif not re.search("[A-Z]", pass_input):
        flag = -1
        break
    elif not re.search("[0-9]", pass_input):
        flag = -1
        break
    elif not re.search("[~!@#$%^&*();:'.,?\`ñÑ]", pass_input):
        flag = -1
        break
    elif re.search("\s", pass_input):
        flag = -1
        break
    else:
        flag = 0
        print("𝙑𝙖𝙡𝙞𝙙 𝙋𝙖𝙨𝙨𝙬𝙤𝙧𝙙 𝙙𝙚𝙩𝙚𝙘𝙩𝙚𝙙!")
        break
  
if flag ==-1:
    print("𝘚𝘰𝘳𝘳𝘺, 𝘪𝘵'𝘴 𝘯𝘰𝘵 𝘢 𝘝𝘢𝘭𝘪𝘥 𝘗𝘢𝘴𝘴𝘸𝘰𝘳𝘥. 𝘗𝘭𝘦𝘢𝘴𝘦 𝘵𝘳𝘺 𝘰𝘯𝘤𝘦 𝘮𝘰𝘳𝘦.")