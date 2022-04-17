#本程序作用：收录根据特定情况生成所需数据集以及数据集相关操作
import numpy
import Convert
import ConditionJudge

def TotalBanCoordinate(existingStationList): #生成不能建站的坐标集
    banStationList = [] #不能建站点坐标集
    rowID = 0
    for existingStation in existingStationList:
        banStation = ConditionJudge.BanCoordinate(existingStation[1],existingStation[2])
        banStationList = list(set(banStationList + banStation)) #删除重复的坐标
        rowID += 1
        print("正在生成不能建站的坐标集：已完成第" + str(rowID) + "组")
    print("数据集 - 不能建站的坐标集生成完成！")
    return banStationList

def TotalCoordinate(positionRange=([0,0],[2499,2499])): #生成题目环境全部坐标集positionMin=[0,0],positionMax=[2499,2499]
    totalPositionList = [] #题目环境全部坐标集
    positionX = positionRange[0][0] #positionXMin
    positionY = positionRange[0][1] #positionYMin
    rowID = 0
    while(positionY <= positionRange[1][1]): #positionYMax
        position = (positionX,positionY)
        totalPositionList.append(position)
        positionX += 1
        if(positionX == positionRange[1][0]): #positionXMax
            positionY += 1
            positionX = 0
        rowID += 1
        print("正在生成题目环境全部坐标集：已完成第" + str(rowID) + "组")
    print("数据集 - 题目环境全部坐标集生成完成！")
    return totalPositionList

def FilterBanCoordinate(totalPosition,banPosition): #生成可以建站的坐标集
    filterBanCoordinate = [] #可以建站的坐标集
    rowID = 0
    for row in totalPosition:
        if row not in banPosition:
            filterBanCoordinate.append(row)
        rowID += 1
        print("正在生成可以建站的坐标集：已完成第" + str(rowID) + "组")
    print("数据集 - 可以建站的坐标集生成完成！")
    return filterBanCoordinate

def AbleCoordinate(totalCanPosition,weakCoverPosition,weakCoverTraffic): #给可以建站的每个坐标对象赋予业务量属性
    ableCoordinate = [] #已添加业务量属性的可建站坐标集
    weakCoverPosition_npa = numpy.array(weakCoverPosition)
    rowID = 0
    for position in totalCanPosition:
        #在可建站的坐标集中将弱覆盖点对象赋上对应业务量属性
        if position in weakCoverPosition:
            weakCoverSearch = numpy.where(weakCoverPosition_npa == [position[0],position[1]])
            weakCoverIndex = str(weakCoverSearch)[9:9]
            ableCoordinate.append([position[0],position[1],float(weakCoverTraffic[int(weakCoverIndex)])])
        else:
            ableCoordinate.append([position[0], position[1], 0]) #0并不表示该坐标点业务量为0，而是指不具有业务量属性的非弱覆盖点
        rowID += 1
        print("正在给可以建站的坐标集添加业务量属性：已完成第" + str(rowID) + "组")
    print("数据集 - 可以建站的坐标集业务量属性添加完成！")