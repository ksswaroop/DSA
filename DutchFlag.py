balls= ["G", "B", "G", "G", "R", "B", "R", "G"]

#balls_num=len(balls)*[0]
#print(balls_num)

for i in range(len(balls)):
    if balls[i]=="R":
        balls[i]=1
    elif balls[i]=="G":
        balls[i]=2
    else:
        balls[i]=3
#print(balls_num)
print(balls)
