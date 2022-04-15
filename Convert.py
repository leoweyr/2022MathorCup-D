#本程序作用：数据集文件与程序可操作数据集互相转换

import numpy
import csv

def CsvToNumpy(csvFilePath):#将Csv数据集文件转换为Numpy数组数据集
    with open(csvFilePath,encoding="utf-8") as csvFile:
        reader = csv.reader(csvFile)
        csvList = []
        rowID = 0
        for row in reader:
            if(rowID != 0):
                csvList.append(row)
                print("Csv数据集第" + str(rowID) + "行数据已读取")
            rowID += 1
        return numpy.array(row)