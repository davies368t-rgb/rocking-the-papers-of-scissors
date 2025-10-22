import random

r=random.randint(0,2)
if r==0:
    r1="✂️"
elif r==1:
    r1="🪨"
else:
    r1="📃"

inp=int(input("enter a number(0-✂️  ,1-🪨  ,2-📃  ): "))
if inp==0:
    inp1="✂️"
elif inp==1:
    inp1="🪨"
else:
    inp1="📃"

print("computer input:",r1)
print("your input:",inp1)
if inp==r:
    print("it's a tie")
elif inp==0 and r==1:
    print("you lose")
elif inp==1 and r==0:
    print("you win")
elif inp==0 and r==2:
    print("you win")
elif inp==2 and r==1:
    print("you win")
elif inp==1 and r==2:
    print("you lose")
elif inp==2 and r==0:
    print("you lose")
else:
    print("stuff")