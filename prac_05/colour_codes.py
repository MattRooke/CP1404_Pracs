COLOUR_HEX_CODES = {"aquamarine": "	#7fffd4", "black": "#000000", "blue": "#0000ff", "firebrick": "#ee2c2c",
                    "forestgreen": "#228b22", "hotpink": "#ff69b4", "magenta": "#ff00ff"}

colour = input("Enter colour name:").lower()
while colour != "":
    if colour in COLOUR_HEX_CODES:
        print("Code is:", COLOUR_HEX_CODES[colour])
    else:
        print("Colour not in list")
    colour = input("Enter colour name:").lower()
