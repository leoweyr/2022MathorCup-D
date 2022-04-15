#本程序作用：收录所以要用到的条件判断操作

def BanCoordinate(positionX,positionY):
#基于门限这一限定条件，输入某坐标，输出不能建站的坐标集
    THRESHOLD = 10#门限值，为常量
    '''
    #坐标集square获取
    positionGather_square = []
    catchX = positionX + THRESHOLD
    catchY = positionY - THRESHOLD
    while (catchY <= positionY + THRESHOLD):
        if(catchX != positionX and catchY != positionY):
            position = [catchX,catchY]
            positionGather_square.append(position)
        catchX -= 1
        if (catchX = positionX - THRESHOLD):
            catchY += 1
            catchX = positionX + THRESHOLD
    '''
    banPositionGather = []
    #圆形在坐标值皆为整数的坐标轴上覆盖的坐标点形成的集合图形即为像素正方形模型
    catchX = positionX
    catchY = positionY - THRESHOLD
    triangleChaseX = 0#像素正方形模型X轴追赶正方形边界增进值
    triangleChaseY = 0#像素正方形模型Y轴追赶正方形边界增进值
    triangleSteeringwheelX = "+"#像素正方形模型X轴追赶方向
    triangleSteeringwheelY = "+"#像素正方形模型Y轴追赶方向
    while True:
       if(catchX != positionX and catchY != positionY):
            position = [catchX,catchY]
            banPositionGather.append(position) 
        if(triangleChaseX == triangleChaseY):
            triangleChaseY += 1
            catchY += 1
        if(triangleSteeringwheelX == "+" and triangleChaseX <= triangleChaseY):
            triangleChaseX += 1
            
        triangleChaseX     
            
    