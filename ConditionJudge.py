#本程序作用：收录所以要用到的条件判断操作

import math

def BanCoordinate(positionX,positionY): #基于门限这一限定条件，输入某坐标，输出不能建站的坐标集
    THRESHOLD = 10 #门限值，为常量
    positionGather_square = [] #外切于覆盖圆的正方形区域坐标集square
    catchX = positionX - THRESHOLD
    catchY = positionY - THRESHOLD
    while (catchY <= positionY + THRESHOLD):
        if(catchX != positionX and catchY != positionY and catchX >= 0 and catchX <= 2499 and catchY >=0 and catchY <= 2499):
            position = [catchX,catchY]
            positionGather_square.append(position)
        if(catchX == positionY + THRESHOLD):
            catchY += 1
            catchX = positionX - THRESHOLD
        else:
            catchX += 1
    positionGather_ban = [] #根据门限限定条件从坐标集square中筛选出不能建筑的坐标集ban
    for position in positionGather_square:
        distance = math.sqrt((position[0] - positionX)**2 + (position[1] - positionY)**2)
        if(distance <= THRESHOLD):
            positionGather_ban.append(position)
    return positionGather_ban