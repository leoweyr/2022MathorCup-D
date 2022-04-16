#本程序作用：收录根据特定情况生成所需数据集以及数据集相关操作

import Convert
import ConditionJudge

def TotalBanCoordinate(): #生成不能建站的坐标集
    existingStationList = Convert.CsvToList("./TopicData/附件2 现网站址坐标(筛选).csv")
    banStationList = [] #不能建站点坐标集
    rowID = 0
    for existingStation in existingStationList:
        banStation = ConditionJudge.BanCoordinate(existingStation[1],existingStation[2])
        banStationList = list(set(banStationList + banStation)) #删除重复的坐标
        rowID += 1
        print("正在生成不能建站的坐标集：已完成第" + str(rowID) + "组")
    print("数据集生成完成！")
    Convert.ListToCsv("./Data","不能建站的坐标集.csv",['x','y'],banStationList)