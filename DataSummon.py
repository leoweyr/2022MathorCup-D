#本程序作用：收录根据特定情况生成所需数据集以及数据集相关操作

import Convert
import ConditionJudge
import threading

def MultithreadingWork(FuntionWork,FunctionResult,conditionMin,conditionMax,threadAmount): #计算机底层多线程规划任务，让数据集生成更快
    if(len(conditionMax) != len(conditionMin)):#检查生成条件极值的对称性
        return False
    else:
        parameterLen = len(conditionMin)
        conditionStep = (conditionMax - conditionMin)/threadAmount #将数据集生成条件依据线程数进行分段，平均每段的生成条件区间长度
        conditionData = [] #将数据集分段出多个子数据集的数据集
        conditionParameter = [] #单位生成条件集
        #数据集生成条件平均分段给不同线程进行同时工作运算生成数据集
        threadIndex = 1 #线程索引
        while(threadIndex <= threadAmount):
            if(threadIndex == 1):
                parameterID = 0
                conditionParameter_ini0 = []
                conditionParameter_ini1 = []
                while (parameterID < parameterLen):
                    conditionParameter_ini0.append(conditionMin[parameterID])
                    conditionParameter_ini1.append(conditionMin[parameterID] + conditionStep)
                    parameterID += 1
                conditionParameter.append(conditionParameter_ini0)
                conditionParameter.append(conditionParameter_ini1)
            elif(threadIndex < threadAmount and threadIndex != 1):
                parameterID = 0
                while(parameterID < parameterLen):
                    conditionParameter[0][parameterID] += conditionStep
                    conditionParameter[1][parameterID] += conditionStep
                    parameterID += 1
            elif(threadIndex == threadAmount):
                parameterID = 0
                while (parameterID < parameterLen):
                    conditionParameter[0][parameterID] += conditionStep
                    conditionParameter[1][parameterID] = conditionMax[parameterID]
                    parameterID += 1
            conditionData[threadIndex] = conditionParameter
            exec("threadWork{} = threading.Thread(target=FuntionWork,args=(conditionData[0],conditionData[1]))".format(threadIndex))
            exec("threadWork{}.start".format(threadIndex))
            print("线程" + threadIndex + "已开始工作")
            threadIndex += 1
        #轮询等待全部线程工作完毕
        threadIndex = 1  # 线程索引
        threadStatus_total = 0 #线程工作状态
        while(threadStatus_total < threadAmount):
            if(threadIndex > threadAmount):
                threadIndex = 1
            exec("threadStatus = threadWork{}.is_alive()".format(threadIndex))
            if(threadStatus == False):
                threadStatus_total += 1
                print("线程" + threadIndex + "已结束工作")
            threadIndex += 1
        #获取线程输出结果并对结果进行处理
        threadIndex = 1
        threadResult_total = [] #线程工作输出结果集
        while(threadIndex <= threadAmount):
            exec("threadResult = threadWork{}.get_result()".format(threadIndex))
            threadResult_total.append(threadResult)
            threadIndex += 1
        FunctionResult(threadResult_total)

def TotalBanCoordinate(): #生成不能建站的坐标集
    existingStationList = Convert.CsvToList("./TopicData/附件2 现网站址坐标(筛选).csv")
    banStationList = [] #不能建站点坐标集
    rowID = 0
    for existingStation in existingStationList:
        banStation = ConditionJudge.BanCoordinate(existingStation[1],existingStation[2])
        banStationList = list(set(banStationList + banStation)) #删除重复的坐标
        rowID += 1
        print("正在生成不能建站的坐标集：已完成第" + str(rowID) + "组")
    print("数据集 - 不能建站的坐标集生成完成！")
    return banStationList
    #Convert.ListToCsv("./Data","不能建站的坐标集.csv",['x','y'],banStationList)

def TotalCoordinate(positionMin=[0,0],positionMax=[2499,2499]): #生成题目环境全部坐标集
    totalPositionList = [] #题目环境全部坐标集
    positionX = positionMin[0]
    positionY = positionMin[1]
    rowID = 0
    while(positionY <= positionMax[1]):
        position = (positionX,positionY)
        totalPositionList.append(position)
        positionX += 1
        if(positionX == positionMax[0]):
            positionY += 1
            positionX = 0
        rowID += 1
        print("正在生成题目环境全部坐标集：已完成第" + str(rowID) + "组")
    print("数据集 - 题目环境全部坐标集生成完成！")
    return totalPositionList
    #Convert.ListToCsv("./Data","题目环境全部坐标集.csv",['x','y'],totalPositionList)