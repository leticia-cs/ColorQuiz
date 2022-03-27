# Color Quiz.py

# TO-DO:
# !!!!!! Run the code. !!!!!!!
# sum for total not working
# [SOLVED] is there some other way to do it other than if/else/elif...? tired of those.
# change-able value for input() in answer.
# [SOLVED] range for result score
# test if values are corresponding
# [SOLVED] Optimize dict
# [SOLVED] Fix writing errors

# Base values for each variable.
valA = 0
valB = 0
valC = 0
valD = 0
total = int(valA) + int(valB) + int(valC) + int(valD)
result = 0


result_text = "Nothing here!"
answer = input("My answer: ")

# Base text for each variable.
qNum = 0
qTxt = "No text for question"
aTxt = "No text for A"
bTxt = "No text for B"
cTxt = "No text for C"
dTxt = "No text for D"

# Errors
err1 = "ERROR 1: S was not pressed."
err2 = "ERROR 2: Invalid option selected."
err3 = "ERROR 3: Something went wrong with the total sum."
err4 = "ERROR 4: Something went wrong with the result."
err5 = "ERROR 5: Option value is empty."
err6 = "ERROR 6: Something went wrong with the value"

# Text introdutionc with instructions
intro = """Welcome to Color Quiz.

Here, you will be asked questions with various options of answer.
Just choose the one which applies to you the most.
"""
def start():
    global qNum
    qNum = 1
    return ques
    return answer

print(intro)

press = input("Please press S to start.")

if press == "S" or press == "s":
    start()
else:
    print(err1)

# Base format for the questions.
ques = """
    {}. {}
    a) {}
    b) {}
    c) {}
    d) {}
    """.format(qNum, qTxt, aTxt, bTxt, cTxt, dTxt)


# assign value to answer in each question

# question one (1):
if qNum == 1:
    txt1 = {
        qTxt : "Which place?",
        aTxt : "bedroom",
        bTxt : "kitchen",
        cTxt : "living room",
        dTxt : "bathroom"
    }
    # answer
    if answer == "A" or answer == "a":
        valA = int(valA) + 3
    elif answer == "B" or answer == "b":
        valB = int(valB) + 2
    elif answer == "C" or answer == "c":
       valC = int(valC) + 1
    elif answer == "D" or answer == "d":
       valD = int(valD) + 4
    else:
        print(err6)

# question two (2)
if qNum == 2:
    txt2 = {
        qTxt : "Which vacation?",
        aTxt : "beach",
        bTxt : "art museum",
        cTxt : "home",
        dTxt : "PARTY"
    }
    # answer
    if answer == "A" or answer == "a":
        valA = int(valA) + 2
    elif answer == "B" or answer == "b":
        valB = int(valB) + 3
    elif answer == "C" or answer == "c":
       valC = int(valC) + 4
    elif answer == "D" or answer == "d":
       valD = int(valD) + 1
    else:
        print(err6)

# question three (3)
if qNum == 3:
    txt3 = {
        qTxt : "Which hangout?",
        aTxt : "friends",
        bTxt : "family",
        cTxt : "yourself",
        dTxt : "strangers"
    }
    # answer
    if answer == "A" or answer == "a":
        valA = int(valA) + 3
    elif answer == "B" or answer == "b":
        valB = int(valB) + 2
    elif answer == "C" or answer == "c":
       valC = int(valC) + 4
    elif answer == "D" or answer == "d":
       valD = int(valD) + 1
    else:
        print(err6)

# question four (4)
if qNum == 4:
    txt4 = {
        qTxt : "What role?",
        aTxt : "research",
        bTxt : "write",
        cTxt : "present",
        dTxt : "organize"
    }
    # answer
    if answer == "A" or answer == "a":
        valA = int(valA) + 3
    elif answer == "B" or answer == "b":
        valB = int(valB) + 4
    elif answer == "C" or answer == "c":
       valC = int(valC) + 1
    elif answer == "D" or answer == "d":
       valD = int(valD) + 2
    else:
        print(err6)

# question five (5)
if qNum == 5:
    txt5 = {
        qTxt : "What animal?",
        aTxt : "amphibian/fish",
        bTxt : "mammal",
        cTxt : "bird",
        dTxt : "reptile"
    }
    # answer
    if answer == "A" or answer == "a":
        valA = int(valA) + 3
    elif answer == "B" or answer == "b":
        valB = int(valB) + 1
    elif answer == "C" or answer == "c":
       valC = int(valC) + 2
    elif answer == "D" or answer == "d":
       valD = int(valD) + 4
    else:
        print(err6)

def nextquestion():
    global qNum
    qNum += 1
    if qNum > 5:
        endquiz()
    print(ques)
    print(answer)

def invalip_total():
    raise Exception (err4)

def set_total():
    result={
        "color_yellow" : "Yellow. Lively, imaginative.",
        "color_red" : "Red. Fierce, self-assured",
        "color_orange" : "Orange. Hungry, curious",
        "color_green" : "Green. Peaceful, achiever.",
        "color_blue" : "Blue. Creative, introspective",
        "color_purple" : "Purple. Interior knowledge, wisdom"
    }

if total >= 4 and total <= 6:
    result_text == result.get("color_yellow")
elif total >= 7 and total <= 9:
    result_text == result.get("color_yellow")
elif total >= 10 and total <= 13:
    result_text == result.get("color_yellow")
elif total >= 14 and total <= 16:
    result_text == result.get("color_yellow")
elif total >= 17 and total <= 19:
    result_text == result.get("color_yellow")
elif total == 20:
    result_text == result.get("color_yellow")
else:
    print(err4)

def endquiz():
    if qNum > 5:
        print("""
        Here are your results.
        
        Your color plus a brief description:
        {}.
        
        Your total: {}.""".format(result_text, total))

# DEBUG
# print(total)
