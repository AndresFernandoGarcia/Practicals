from Practical6.programming_language import ProgrammingLanguage

p_languages = []

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
p_languages.append(ruby)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
p_languages.append(python)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
p_languages.append(visual_basic)

print("The dynamically typed languages are: ")
for item in p_languages:
    """ looping through programming languages list"""
    answer = item.is_dynamic()
    if answer:
        print(item.get_name())
