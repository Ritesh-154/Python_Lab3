import math
def ball_collide(x1,y1,r1,x2,y2,r2):
    x=math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))
    if x<=r1+r2:
        return True
    else:
        return False
x1=int(input("X coordinate of first ball : "))
y1=int(input("Y coordinate of first ball : "))
r1=int(input("radius of first ball : "))
x2=int(input("X coordinate of second ball : "))
y2=int(input("Y coordinate of second ball : "))
r2=int(input("radius of second ball : "))
a=ball_collide(x1,y1,r1,x2,y2,r2)
if a==True:
    print("They will collide")
else:
    print("They will not collide")
