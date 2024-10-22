die1={'1','2','3','4','5','6'}
die2={'1','2','3','4','5','6'}
print("Welcome t my dice game[press enter to toss the dice]")
toss= input()
p1=die1.pop()
die2.pop()
p2=die2.pop()
print(f"you played{p1}and{p2}")
print(f"your score is {int(p1)+int(p2)}")
