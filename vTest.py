intro = [print("Welcome to Color Quiz!")
print()
print("Here, you will be asked questions that you must answer by choosing between the options provided.")
print("A, B, C or D.")
print()]

press = [print("Press S to start.")
print()]

err1 = "Please press (S) to start!"

if input() == "S":
    qNum(1)
    question()
    
else:
    print(err1)
    print()
    print(press)

qNum = [1, 2, 3, 4, 5] # number of question
sel = ["A", "B", "C", "D"] # alternative (option)
ask # question (words)
opt # options provided
resNum = 0 # Answers score. Determines 'res'.
res #Final result. Quiz result.

ans = input("Your Answer: ") # User answer

err2 = "Please choose one of the options or check your entry."

if ans == "A" or "B" or "C" or "D":
    qNum + 1

else: 
    print(err2)

if qNum == 1:
    ask = "Which do you like more?"
    opt = ["A. Your Bedroom.",
    "B. The Kitchen.",
    "C. The Living Room.",
    "D. The Office."]
    
if qNum == 2:
    ask = ""

input();
    
question:
    print("Question" + qNum)
    print()
    print(ask)
    print()
    print(opt)
    print()

errF = "Something went wrong with the score!"

if resNum == 0:
    print(errF)
else: print(res)
