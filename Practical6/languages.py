from Practical6.programming_language import ProgrammingLanguage

planguages = []

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
planguages.append(ruby)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
planguages.append(python)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
planguages.append(visual_basic)

print("The dynamically typed languages are: ")
for item in planguages:  # looping through programming languages list
    answer = item.is_Dynamic()
    if answer:
        print(item.get_Name())
