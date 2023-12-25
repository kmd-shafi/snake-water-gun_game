import random

def gamewin(comp,you):
    if(comp==you):
        return None
    elif(comp=="s"):
        if(you=="w"):
            return False
        elif(you=="g"):
            return True
    elif(comp=="w"):
        if (you=="g"):
            return False
        elif(you=="s"):
            return True
    elif(comp=="g"):
        if(you=="s"):
            return False
        elif(you=="w"):
            return True
    
print("comp turn: Snake(s),Water(w) or Gun(g):?")
ran=random.randint(1,3)
if (ran ==1):
    comp="s"
elif(ran==2):
    comp="w"
elif(ran==3):
    comp="g"
    
   
you=input("your turn : Snake(s),Water(w) or Gun(g):?")
a=gamewin(comp,you)
# print(f"computer choice i {comp}")
# print(f"your choice is {you}")

if a==None:
    print("this game is tie!")
elif a:
    print("you win!")
else:
    print("you lose")

    


        