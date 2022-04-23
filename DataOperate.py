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

def FilterCoordinate(totalPosition,unincludePosition): #生成按条件过滤不包含规定坐标集的坐标集
    filterCoordinate = [] #不包含规定坐标集的坐标集
    rowID = 0
    for row in totalPosition:
        if row not in unincludePosition:
            filterCoordinate.append(row)
        rowID += 1
        print("正在生成按条件过滤不包含规定坐标集的坐标集：已完成第" + str(rowID) + "组")
    print("数据集 - 按条件过滤不包含规定坐标集的坐标集生成完成！")
    return filterCoordinate

def GetTraffic(coordinate,weakCoverCoordinate): #给坐标集赋予业务量属性
    weakCoverPosition = []  # 弱覆盖点的坐标集
    weakCoverTraffic = []  # 弱覆盖点的业务量集
    for coordinate in weakCoverCoordinate: #将弱覆盖点的坐标集和业务量集分开，但索引是一一对应的
        weakCoverPosition.append((coordinate[0],coordinate[1]))
        weakCoverTraffic.append(coordinate[2])
    trafficCoordinate = []  # 已添加业务量属性的坐标集
    weakCoverPosition_npa = numpy.array(weakCoverPosition)
    rowID = 0
    for position in coordinate:
        # 在坐标集中将弱覆盖点对象赋上对应业务量属性
        if position in weakCoverPosition:
            weakCoverSearch = numpy.where(weakCoverPosition_npa == [position[0], position[1]])
            weakCoverIndex = str(weakCoverSearch)[9:9]
            trafficCoordinate.append([position[0], position[1], float(weakCoverTraffic[int(weakCoverIndex)])])
        else:
            trafficCoordinate.append([position[0], position[1], 0])  # 0并不表示该坐标点业务量为0，而是指不具有业务量属性的非弱覆盖点
        rowID += 1
        print("正在给坐标集添加业务量属性：已完成第" + str(rowID) + "组")
    print("数据集 - 坐标集业务量属性添加完成！")
    return trafficCoordinate

def AbleCoordinate(totalCanPosition,weakCoverCoordinate): #给可以建站的每个坐标对象赋予业务量属性
    ableCoordinate = GetTraffic(totalCanPosition,weakCoverCoordinate) #给可建站坐标点赋予业务量属性
    #以业务量为标准对可建站的坐标集进行降序排序
    ableCoordinate_index = 0
    while(ableCoordinate_index < len(ableCoordinate)):
        ableCoordinate_index += 1
        indexMove = ableCoordinate_index
        while(indexMove > 0):
            if(ableCoordinate[indexMove][2] > ableCoordinate[indexMove - 1][2]):
                index_backUp - 1
            else:
                break
        ableCoordinate_backup = ableCoordinate[ableCoordinate_index]
        ableCoordinate.pop(ableCoordinate_index)
        ableCoordinate.insert(indexMove,ableCoordinate_backup)
    return ableCoordinate

def MeetConditionCoordinate_highCost(ableCoordinate,weakCoverCoordinate,totalTraffic,indexDatum,indexDatumNext): #生成每个基站皆为宏基站的且满足题目条件的坐标集
    meetConditionPosition = [] #每个基站皆为宏基站的且满足题目条件的坐标集
    sumTraffic = 0
    sumCost = 0
    index = indexDatum
    indexLoop = 0
    while(index < len(ableCoordinate)):
        if(indexLoop == 1):
            index = indexDatumNext
        positionX = ableCoordinate[index][0]
        positionY = ableCoordinate[index][1]
        stationTraffic = ableCoordinate[index][2]
        meetConditionPosition.append((positionX,positionY))
        sumCost += 10
        sumTraffic = float(sumTraffic) + float(stationTraffic)
        #获取每个被覆盖点的业务量
        coverCoordinate = ConditionJudge.CoverCoordinate(positionX,positionY,30)
        coverCoordinate = GetTraffic(coverCoordinate,weakCoverCoordinate)
        for coverPosition in coverCoordinate:
            coverTracfic = coverPosition[2]
            sumTraffic = float(sumTraffic) + float(coverTracfic)
        ableCoordinate_new = []
        for ablePosition in ableCoordinate:
            if ablePosition in coverCoordinate:
                ableCoordinate_new.append([ablePosition[0],ablePosition[1],0])
            else:
                ableCoordinate_new.append([ablePosition[0],ablePosition[1],ablePosition[2]])
        ableCoordinate = ableCoordinate_new
        banCoordinate = ConditionJudge.BanCoordinate(positionX,positionY)
        banCoordinate = GetTraffic(banCoordinate, weakCoverCoordinate)
        ableCoordinate = FilterCoordinate(ableCoordinate, banCoordinate)
        if(float(sumTraffic/totalTraffic) >= 0.9): #满足条件停止建站
            break
        else:
            index += 1
            indexLoop += 1
    return [sumCost,meetConditionPosition]

def MeetConditionCoordinate_lowCost(ableCoordinate,weakCoverCoordinate,totalTraffic,indexDatum,indexDatumNext): #生成每个基站皆为微基站的且满足题目条件的坐标集
    meetConditionPosition = [] #每个基站皆为微基站的且满足题目条件的坐标集
    sumTraffic = 0
    sumCost = 0
    index = indexDatum
    indexLoop = 0
    while(index < len(ableCoordinate)):
        if(indexLoop == 1):
            index = indexDatumNext
        positionX = ableCoordinate[index][0]
        positionY = ableCoordinate[index][1]
        stationTraffic = ableCoordinate[index][2]
        meetConditionPosition.append((positionX,positionY))
        sumCost += 1
        sumTraffic = float(sumTraffic) + float(stationTraffic)
        #获取每个被覆盖点的业务量
        coverCoordinate = ConditionJudge.CoverCoordinate(positionX,positionY,10)
        coverCoordinate = GetTraffic(coverCoordinate,weakCoverCoordinate)
        for coverPosition in coverCoordinate:
            coverTracfic = coverPosition[2]
            sumTraffic = float(sumTraffic) + float(coverTracfic)
        ableCoordinate_new = []
        for ablePosition in ableCoordinate:
            if ablePosition in coverCoordinate:
                ableCoordinate_new.append([ablePosition[0],ablePosition[1],0])
            else:
                ableCoordinate_new.append([ablePosition[0],ablePosition[1],ablePosition[2]])
        ableCoordinate = ableCoordinate_new
        banCoordinate = ConditionJudge.BanCoordinate(positionX,positionY)
        banCoordinate = GetTraffic(banCoordinate, weakCoverCoordinate)
        ableCoordinate = FilterCoordinate(ableCoordinate, banCoordinate)
        if(float(sumTraffic/totalTraffic) >= 0.9): #满足条件停止建站
            return [sumCost,meetConditionPosition]
        else:
            index += 1
            indexLoop += 1
    return False

'''
def MeetConditionCoordinate_lowCostInsertHighCost(ableCoordinate,highCostCoordinate):#生成从全部基站为宏基站且满足条件的建站选址坐标集中逐步替换插入微基站的坐标集
    meetConditionPosition = []  # 从原本全部基站为宏基站逐步替换插入微基站且满足题目条件的坐标集
    sumTraffic = 0
    ableCoordinate_index = 0
    highCostCoordinate_index = 0
    highCostCoordinateLen = len(highCostCoordinate)
    sumCost = len(highCostCoordinate)*10
    highCostCoordinate_withIndexID = []
    while(highCostCoordinate < len(highCostCoordinate_index)):
        if([ableCoordinate[ableCoordinate_index][0],ableCoordinate[ableCoordinate_index][1]] == highCostCoordinate[highCostCoordinate_index]):
            highCostCoordinate_withIndexID.append([highCostCoordinate[0],highCostCoordinate[1],ableCoordinate_index])
            highCostCoordinate_index += 1
        ableCoordinate_index += 1
    for IndexID in highCostCoordinate_withIndexID:
        sumTraffic = float(sumTraffic) + float(ableCoordinate_index(IndexID[2])[2])
    highCostCoordinate_index = 0

    positionX = highCostCoordinate[highCostCoordinate_index][0]
    positionY = highCostCoordinate[highCostCoordinate_index][1]
    ConditionJudge.BanCoordinate(positionX,positionY)
'''

def CostSort(DataGatherPath): #排序选出成本最低的建站选址数据集
    def SortByCost(dataName):#ID%id%-COST-%cost%.csv
        dataAttribute = str(dataName).split("-COST-")
        cost = str(dataAttribute[1])[:-4]
        return cost
    meetConditionList = os.listdir(DataGatherPath)
    meetConditionList.sort(key=SortByCost)
    leastCostDataList = [] #成本最低的建站选址坐标数据集合集，可能存在多个方案成本一样
    leastCostDataList.append(meetConditionList[0])
    dataIndex = 1
    while (SortByCost(meetConditionList[0]) == SortByCost(meetConditionList[dataIndex])):
            leastCostDataList.append(meetConditionList[dataIndex])
            dataIndex += 1
    return  leastCostDataList