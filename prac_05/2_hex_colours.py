CODE_TO_COLOR = {"#0048ba":"AbsoluteZero", "#b0bf1a": "AcidGreen", "#f0f8ff" : "AliceBlue",
                 "#e32636" : "AlizarinCrimson", "#e52b50": "Amaranth", "#ffbf00": "Amber",
                 "#9966cc": "Amethyst", "#faebd7": "AntiqueWhite", "#ffefdb": "AntiqueWhite1",
                 "#00ffff": "Aqua"}
print(CODE_TO_COLOR)

color_code = input("Enter color code: ").lower()
while color_code != "":
    if color_code in CODE_TO_COLOR:
        print(color_code, "is", CODE_TO_COLOR[color_code])
    else:
        print("Invalid color code")
    color_code = input("Enter color code: ").lower()