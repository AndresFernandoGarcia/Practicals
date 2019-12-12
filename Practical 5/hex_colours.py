COLOR_TO_HEX= {'ALICEBLUE' : '#f0f8ff','ANTIQUEWHITE': '#faebd7', 'ANTIQUEWHITE1':'#ffefdb',
                    'ANTIQUEWHITE2':'#eedfcc','ANTIQUEWHITE3':'#cdc0b0','ANTIQUEWHITE4':'#8b8378',
                    'AQUAMARINE1':'#7fffd4','AQUAMARINE2':'#76eec6','AZURE1':'#f0ffff','AQUAMARINE4':'#458b74'}
def main():
    continues = False
    while (continues != True):
        user_input = input("Color>>> ")
        user_input = user_input.upper()


        if(user_input == ""):
            continues = True
        else:
            output = findColour(user_input)
            if output != "none":
                print(output)
            else:
                print("invalid colour")


def findColour (color):
    for colour, hex_val in COLOR_TO_HEX.items():
        if (color == colour):
            return hex_val

    return("none")


main()