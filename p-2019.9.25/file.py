# -*- coding:utf-8 -*-
# 导入模块
import xlrd
import xlwt


def readexcel():
    workbook=xlrd.open_workbook(r'C:\Users\peipei\Desktop\git\mmsi.xlsx')#打开表格
    sheet=workbook.sheet_by_name('MMSI') #通过excel表格名称获取工作表
    dat=[]
    for a in range(sheet.nrows):
                cells=sheet.row_values(a)
                data=int(cells[0])#因为表内可能存在多列数据，0代表第一列数据，1代表第二列，以此类推
                dat.append(data) #把每次循环读取的数据插入到list
    return dat
a = excel() #返回整个函数的值
print(a)

def test(a):   #a变量传入
    for b in a:  #循环读取a变量list
        print(b)
test(a)


