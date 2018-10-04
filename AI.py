import math
import config

def getDestinationPost(myTank, enemy,speed):
    print('automove')
    center = myTank.rect.center
    for index,spr in enumerate(enemy):
        pos = spr.gunpos()
        xx = pos[0] - center[0]
        yy = pos[1] - center[1]
        distance = math.sqrt(xx*xx + yy*yy)
        print(distance)
        x,y = calculateHeadDelta(pos[2],distance)
        print('Center',center)
        print('Similutor',x+pos[0],y+pos[1])
        if(x + pos[0] >= center[0] -50 and x + pos[0] <= center[0] + 50 \
            and y+pos[1] >= center[1] - 50 and y + pos[1] <= center[1] + 50):

            if(myTank.angle >= pos[2] - 2 and myTank.angle <= pos[2] + 2):
                return 'right'
            if(myTank.angle + 18 >= pos[2] - 2 and myTank.angle + 18 <= pos[2] + 2):
                return 'left'
            
            dx,dy = myTank.calculateHeadDelta(speed)
            newX = center[0] + dx
            newY = center[1] + dy

            if(newX >= config.WINDOWS_WIDTH - 50 or newY >= config.WINDOWS_HEIGHT - 50 \
                or newX <= 50 or newY <= 50):
                return 'back'
            
            newX = center[0] - dx
            newY = center[1] - dy 
            if(newX >= config.WINDOWS_WIDTH - 50 or newY >= config.WINDOWS_HEIGHT - 50 \
                or newX <= 50 or newY <= 50):
                return 'head'
            
            if(myTank.lastMove == 'right' or myTank.lastMove == 'left'):
                return 'head'
            return myTank.lastMove
    return 'custom'

def calculateHeadDelta(angle,distance):
    x = 0
    y = 0
    alpha = angle/18*math.pi
    y = -1*distance* math.sin(alpha)
    x = distance*math.cos(alpha)
    return (x,y)  