
#Function: Transfer CSV into list
def readCSV2List(filePath): #F:\project\myDB
    try:
        file = open(filePath,'r',encoding="gbk")# 读取以utf-8
        context = file.read() # 读取成str
        list_result=context.split("\n")#  以回车符\n分割成单独的行
        #每一行的各个元素是以【,】分割的，因此可以
        length=len(list_result)
        for i in range(length):
            list_result[i]=list_result[i].split(",")
        return list_result,length
    except Exception :
        print("文件读取转换失败，请检查文件路径及文件编码是否正确")
    finally:
        file.close();# 操作完成一定要关闭

# Read files into rows & Get length
list_Result,length_list = readCSV2List(E:\Project\TestDataUSC) # Need to add the file path

def FilterByRoomType(strRoom):
    #Traverse
    for i in length_list:
        if list_Result[i][1] == 'strRoom': #Set first column to be Roomtype
            return list_Result[i]


def FilterByMoney(intMoney):
   #Traverse
   for i in length_list:
       if list_Result[i][2] <= intMoney: # Set second to be MoneyRange
           return list_Result[i]

def FilterByDate(intStartDate, intEndDate):
   #Traverse
   for i in length_list:
       if list_Result[i][3] <= intStartDate and list_Result[i][4] >= intEndDate:
           return list_Result[i]

def FilterByLocation(floatLatitude, floatLogitude):
   for i in length_list:
       if abs(list_Result[i][5] - floatLatitude) <= 5 and abs(list_Result[i][6] - floatLogitude) <= 5:
           return listResult[i]




