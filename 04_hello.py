import random

def gamewin(comp,you):
    if comp==you:
        return None
    elif comp=="s":
        if you=="w":
            return False
        elif you=="g":
            return True
    elif comp=="w":
        if you=="g":
            return False
        elif you=="s":
            return True
    elif comp=="g":
        if you=="s":
            return False
        elif you=="w":
            return True
print("comp turn:Snake(s),Water(w) or Gun(g):?")
imp=random.randint(1,3)
if imp==1:
    comp="s"
elif imp==2:
    comp ="w"
elif imp==3:
    comp="g"
you=input("your turn: Snake(s),Water(w) or Gun(g):?")
print(f"comp choice is {comp}")
print(f"your choice is {you}")
a=gamewin(comp,you)
if a==None:
    print("tie the game!")
elif a==True:
    print("you win!")
else :
    print("you lose!")