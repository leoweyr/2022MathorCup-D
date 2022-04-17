#本程序作用：收录所有要用到的条件判断操作

import math

def BanCoordinate(positionX,positionY): #基于门限这一限定条件，输入某坐标，输出不能建站的坐标集
    THRESHOLD = 10 #门限值，为常量
    positionGather_square = [] #外切于覆盖圆的正方形区域坐标集square
    catchX = int(positionX) - THRESHOLD
    catchY = int(positionY) - THRESHOLD
    while (catchY <= int(positionY) + THRESHOLD):
        if(catchX != int(positionX) and catchY != int(positionY) and catchX >= 0 and catchX <= 2499 and catchY >=0 and catchY <= 2499):
            position = (catchX,catchY)
            positionGather_square.append(position)
        if(catchX == int(positionX) + THRESHOLD):
            catchY += 1
            catchX = int(positionX) - THRESHOLD
        else:
            catchX += 1
    positionGather_ban = [] #根据门限限定条件从坐标集square中筛选出不能建筑的坐标集ban
    for position in positionGather_square:
        distance = math.sqrt((float(position[0]) - float(positionX))**2 + (float(position[1]) - float(positionY))**2)
        if(float(distance) <= float(THRESHOLD)):
            positionGather_ban.append(position)
    return positionGather_ban

def CoverCoordinate(positionX,positionY,coverRadius): #基于覆盖范围限定条件，输入某坐标，输出已覆盖的坐标集
    positionGather_square = []  # 外切于覆盖圆的正方形区域坐标集square
    catchX = int(positionX) - coverRadius
    catchY = int(positionY) - coverRadius
    while (catchY <= int(positionY) + coverRadius):
        if (catchX != int(positionX) and catchY != int(
                positionY) and catchX >= 0 and catchX <= 2499 and catchY >= 0 and catchY <= 2499):
            position = (catchX, catchY)
            positionGather_square.append(position)
        if (catchX == int(positionX) + coverRadius):
            catchY += 1
            catchX = int(positionX) - coverRadius
        else:
            catchX += 1
    positionGather_cover = []  # 根据覆盖范围条件从坐标集square中筛选出不能建筑的坐标集cover
    for position in positionGather_square:
        distance = math.sqrt(
            (float(position[0]) - float(positionX)) ** 2 + (float(position[1]) - float(positionY)) ** 2)
        if (float(distance) <= float(coverRadius)):
            positionGather_cover.append(position)
    return positionGather_cover