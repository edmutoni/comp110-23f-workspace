"""Ord: short for ordinal. Takes intput str and returns the int representation of the character's binary code"""
ord("A")

"""Chr: changing from ascii to character"""
chr(55)

emoji: str = "\U0001F6A2"
#need to add three more 0s between U 
print(emoji)

#other uses of \
# \" double quote 
# \' single quote
# \t tab
# \n new line
# \Uxxxxxxxx New Line
# \\ backlash (\)

#print("The computer said, \"Hello, world.\"")

#f strings; format strings 
course: int = 110
print(f"I am in COMP{course} right now!")
#oh this is so much easier