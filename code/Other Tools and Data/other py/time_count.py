#coding=utf-8
import time

def alocCount():
    with open('base64.asm') as f:
        text=f.readlines()
        lineCount =0
        for eachline in text:
            if eachline.strip() != "": #remove space and tabIndent line
                if eachline.find(';') == 0: #remove comment
                    pass
                else:
                    lineCount += 1

        print(lineCount)


totalTime = 0
for i in range(0,10):
    start = time.clock()
    ###process
    alocCount()
    ###prosess
    end = time.clock()

    totalTime = totalTime + (end - start)
    print (str(i+1)+'th time:',end - start)
    
averageTime = totalTime/10
print('average time:',averageTime)



"""
方法1
import datetime
starttime = datetime.datetime.now()
#long running
endtime = datetime.datetime.now()
print (endtime - starttime).seconds
方法 2
start = time.time()
run_fun()
end = time.time()
print end-start
方法3
start = time.clock()
run_fun()
end = time.clock()
print end-start
方法1和方法2都包含了其他程序使用CPU的时间，是程序开始到程序结束的运行时间。
方法3算只计算了程序运行的CPU时间
"""
