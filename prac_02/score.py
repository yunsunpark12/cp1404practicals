"""
CP1404/CP5632 - Practical
Broken program to determine score status

get score
if score < 0
    print "Invalid score"
else
     if score > 100
        print "Invalid score"
    else if score >= 90
        print "Excellent"
    else if score >= 50
        print "Passable"
    else
        print "bad"
"""

score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("bad")