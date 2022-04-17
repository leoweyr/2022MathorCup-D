#本程序作用：数学解题过程的直接操作，同时也是整个题目的程序入口

import DataSummon
import Convert

'''
import threading

class Thread_canReturn(threading.Thread): #继承threading.Thread类增添方法使得能获取多线程工作函数返回的值
    def __init__(self,target,args):
        threading.Thread.__init__(self)
        self.Target = target
        self.Args = args
    def run(self):
        self.result = self.Target(self.Args)
    def get_result(self):
        return self.result

#工作优化操作
def MultithreadingWork(FunctionWork,conditionMin,conditionMax,threadAmount): #计算机底层多线程规划任务，让数据集生成更快
    if(len(conditionMax) != len(conditionMin)):#检查生成条件极值的对称性
        return False
    else:
        parameterLen = len(conditionMin)
        conditionStep = [] #根据线程数将生成条件分段
        parameterID = 0
        while(parameterID < parameterLen):
            conditionStep.append(int((conditionMax[parameterID] - conditionMin[parameterID])/threadAmount)) #将数据集生成条件依据线程数进行分段，平均每段的生成条件区间长度
            parameterID += 1
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
                    conditionParameter_ini1.append(conditionMin[parameterID] + conditionStep[parameterID])
                    parameterID += 1
                conditionParameter.append(conditionParameter_ini0)
                conditionParameter.append(conditionParameter_ini1)
            elif(threadIndex < threadAmount and threadIndex != 1):
                parameterID = 0
                while(parameterID < parameterLen):
                    conditionParameter[0][parameterID] = int(conditionParameter[0][parameterID]) + conditionStep[parameterID]
                    conditionParameter[1][parameterID] = int(conditionParameter[0][parameterID]) + conditionStep[parameterID]
                    parameterID += 1
            elif(threadIndex == threadAmount):
                parameterID = 0
                while (parameterID < parameterLen):
                    conditionParameter[0][parameterID] = int(conditionParameter[0][parameterID]) + conditionStep[parameterID]
                    conditionParameter[1][parameterID] = conditionMax[parameterID]
                    parameterID += 1
            conditionData.append(conditionParameter)
            exec("threadWork{} = Thread_canReturn(target=FunctionWork,args=(conditionData[{}][0],conditionData[{}][1]))".format(threadIndex,threadIndex - 1,threadIndex - 1))
            exec("threadWork{}.start()".format(threadIndex))
            print("线程" + str(threadIndex) + "已开始工作")
            threadIndex += 1
        # 等待全部线程工作完毕
        threadIndex = threadAmount #线程索引
        while(threadIndex > 0):
            exec("threadWork{}.join()".format(threadIndex))
            print("线程" + str(threadIndex) + "已结束工作")
            threadIndex -= 1
        *
        #轮询等待全部线程工作完毕
        threadIndex = 1  # 线程索引
        threadStatus_total = 0 #线程工作状态
        while(threadStatus_total < threadAmount):
            if(threadIndex > threadAmount):
                threadIndex = 1
            exec("threadStatus = threadWork{}.is_alive()".format(threadIndex))
            print("线程" + str(threadIndex) + "工作状态：" + str(threadStatus))
            if(threadStatus == False):
                threadStatus_total += 1
                print("线程" + str(threadIndex) + "已结束工作")
            threadIndex += 1
        *
        #获取线程输出结果并对结果进行处理
        threadIndex = 1
        threadResult_total = [] #线程工作输出结果集
        while(threadIndex <= threadAmount):
            exec("threadResult = threadWork{}.get_result()".format(threadIndex))
            threadResult_total.append(threadResult)
            threadIndex += 1
        threadIndex = 1  # 线程索引
        threadResultTotal = [] #线程工作输出结果合并集
        for threadResultEach in threadResult_total:
            threadResultTotal += threadResultEach
            print("正在合并线程" + str(threadIndex) + "输出结果")
            threadIndex += 1
        print("所有线程输出结果合并完成！")
        return threadResultTotal

'''

#数学解题步骤
def Op_TotalBanCoordinate(): #生成不能建站的坐标集并输出为CSV数据集文件
    existingStationList = Convert.CsvToList("./TopicData/附件2 现网站址坐标(筛选).csv")
    totalBanCoordinate = DataSummon.TotalBanCoordinate(existingStationList)
    Convert.ListToCsv("./Data","不能建站的坐标集.csv",['x','y'],totalBanCoordinate)

def Op_TotalCoordinate(): #生成题目环境全部坐标集并输出为CSV数据集文件
    #MultithreadingWork(DataSummon.TotalCoordinate,(0,0),(20,20),10) 多线程任务规划算庞大数据集更快
    totalCoordinate = DataSummon.TotalCoordinate()
    Convert.ListToCsv("./Data","题目环境全部坐标集.csv",['x','y'],totalCoordinate)

def Op_AbleCoordinate():
    totalPosition = Convert.CsvToList("./Data/题目环境全部坐标集.csv")
    banPosition = Convert.CsvToList("./Data/题目环境全部坐标集.csv")
    filterBanCoordinate = DataSummon.FilterBanCoordinate(totalPosition,banPosition)
    weakCoverCoordinate = Convert.CsvToList("./TopicData/附件1 弱覆盖栅格数据(筛选).csv")
    weakCoverPosition = [] #弱覆盖点的坐标集
    weakCoverTraffic = [] #弱覆盖点的业务量集
    for coordinate in weakCoverCoordinate: #将弱覆盖点的坐标集和业务量集分开，但索引是一一对应的
        weakCoverPosition.append((coordinate[0],coordinate[1]))
        weakCoverTraffic.append(coordinate[2])
    ableCoordinate = DataSummon.AbleCoordinate(filterBanCoordinate,weakCoverPosition,weakCoverTraffic)



if __name__ == '__main__':
    Op_TotalBanCoordinate()
    Op_TotalCoordinate()
    Op_AbleCoordinate()