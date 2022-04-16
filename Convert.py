#本程序作用：数据集文件与程序可操作数据集互相转换

import csv
import os

class File: #计算机底层文件操作对象
    def __init__(self, dirPath, fileName):
        self.DirPath = dirPath
        self.FileName = fileName
        if (os.path.exists(dirPath) == False):
            os.makedirs(dirPath)

    def FilePath(self):
        return self.DirPath + "\\" + self.FileName

    def Write(self, content):
        file = open(self.DirPath + "\\" + self.FileName, "w")
        file.write(content)
        file.close()

def CsvToList(csvFilePath): #将Csv数据集文件转换为列表数据集
    with open(csvFilePath,encoding="utf-8") as csvFile:
        reader = csv.reader(csvFile)
        csvList = []
        rowID = 0
        for row in reader:
            if(rowID != 0):
                csvList.append(row)
            rowID += 1
        return csvList

def ListToCsv(filePath,fileName,fieldnames,data): #将列表数据集转换为Csv数据集文件
    csvFile = File(filePath,fileName)
    with open(csvFile.FilePath(), 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            fieldnamesLen = len(fieldnames)
            rowLen = len(row)
            if(fieldnamesLen != rowLen): #检查Csv数据与数据名称对称性
                return False
            else:
                CsvRow = {}
                ListElement = 0
                while(ListElement < fieldnamesLen):
                    CsvRow[fieldnames[ListElement]] = row[ListElement]
                    ListElement += 1
                writer.writerow(CsvRow)
        return True