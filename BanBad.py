#本程序作用：获取坏点

import numpy
import csv

class ExistingStation:
    def __int__(self,positionX,positionY):
        self.X = positionX
        self.Y = positionY

#现有基站对象类
#exec("{} = Program(\"{}\")".format(programName, packageList.getCellValue(row, column_program)))
def GetExistingStation:
    with open("./TopicData/附件2 现网站址坐标(筛选).csv",encoding="utf-8") as csv_existingStation:
        reader = csv_existingStation.reader(csv_existingStation)
        for i in reader:
            exec()