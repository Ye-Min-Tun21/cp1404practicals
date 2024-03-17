COLOUR_CODES = {"ALICEBLUE": "#F0F8FF",
                "ANTIQUEWHITE": "#FAEBD7",
                "BEIGE": "#F5F5DC",
                "AZURE": "#F0FFFF",
                "AQUA": "#00FFFF",
                "BLANCHEDALMOND": "#FFEBCD",
                "BLUEVIOLET": "#8A2BE2",
                "BLUE": "#0000FF",
                "BISQUE": "#FFE4C4",
                "BLACK": "#000000"
                }

colour_name = input("Enter a colour name: ").strip().upper()
while colour_name != "":
    print(f"The code for {colour_name} is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ")
