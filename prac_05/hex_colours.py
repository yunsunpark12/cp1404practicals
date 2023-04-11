"""
Yunsun Park
CP1404 Practical
hex colours

Estimate: 20 minutes
Actual:   30 minutes

NAME_TO_CODE = {"amber": "#ffbf00", "aqua": "#00ffff", "beige" : "#f5f5dc", "black" : "#000000",
            "blond": "#faf0be", "brass": "#b5a642", "bronze": "#cd7f32", "brown": "#a52a2a",
            "camel": "#c19a6b", "charcoal": "#36454f"}

for i in NAME_TO_CODE:
    print("{} is {}".format(i, NAME_TO_CODE[i]))

get color_name

while color_name != ""
    if color_name in NAME_TO_CODE
        print(color_name, "is", NAME_TO_CODE[color_name])
    else
        print("Invalid color")
    get color_name
"""

NAME_TO_CODE = {"amber": "#ffbf00", "aqua": "#00ffff", "beige" : "#f5f5dc", "black" : "#000000",
            "blond": "#faf0be", "brass": "#b5a642", "bronze": "#cd7f32", "brown": "#a52a2a",
                "camel": "#c19a6b", "charcoal": "#36454f"}
for i in NAME_TO_CODE:
    print("{} is {}".format(i, NAME_TO_CODE[i]))

color_name = input("Enter name of color: ").lower()
while color_name != "":
    if color_name in NAME_TO_CODE:
        print(color_name, "is", NAME_TO_CODE[color_name])
    else:
        print("Invalid color")
    color_name = input("Enter name of color: ").lower()
