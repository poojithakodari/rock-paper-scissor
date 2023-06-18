# drivers code for project 2
#rock-paper-scissors
from random import randint
choice=["rock","paper","scissor"]
system_score=user_score=0
limit=3
while system_score!=limit and user_score!=limit:
    print(f"choose among the following:",choice)
    my_ch=input("player choice:").lower()
    if my_ch not in choice:
        print("invalid input")
        continue
    sys_ch=choice[int(randint(0,2))]
    print(f" system choice: {sys_ch}")
    if my_ch==sys_ch:
      print("-------match is draw--------")
    elif my_ch=="rock" and sys_ch=="scissor":
        user_score+=1

    elif my_ch=="paper" and sys_ch=="rock":
        user_score+=1
    elif my_ch=="scissor" and sys_ch=="paper":
        user_score+=1
    else:
        system_score+=1
    print(f" your score:{user_score},system score:{system_score}")
        
if user_score > system_score:
    print("you won")
else:
    print("system won")
        
      

