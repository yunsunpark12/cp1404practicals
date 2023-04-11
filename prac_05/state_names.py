"""
Yunsun Park
CP1404 Practical
State names in a dictionary

Estimate: 30 minutes
Actual:   25 minutes
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT" : "Northern Territory", "WA" : "Western Australia",
            "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
for i in CODE_TO_NAME:
    print("{} is {}".format(i, CODE_TO_NAME[i]))

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")
