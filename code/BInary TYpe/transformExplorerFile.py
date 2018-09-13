import re
import os
import shutil

"""
#删除转换完成后目录下的文件
afpath = 'SaveData/tempCode/after_transform'
try:
    if os.path.exists(afpath):
        shutil.rmtree(afpath)
        #print("deleted finished")
    if not os.path.exists(afpath):
        os.makedirs(afpath)
        #print('makedir finished')
except:
    pass
"""

flag=0#1代表IDA格式，2代表godblot格式
path = 'SaveData/tempCode/predict/tempCode/tempCode.txt'
try:
    with open(path) as file:
        for i in range(0,10):
            thisline=file.readline()
            if 'proc near' in thisline:
                #print('IDA format')
                flag = 1
                break
            elif 'PROC' in thisline:
                #print('godblot format')
                flag=2
                break


except IOError as err:
    print('File error:' + str(err))

#transform prosess
if flag==1:
    print('IDA format')
elif flag==2:
    newfileContext=[]
    with open(path,'r') as file:
        fileContext=file.readlines()
        ContextLen=len(fileContext)
        varname=[]
        varsave=[]
        for lineNum in range(0,ContextLen):
            #变量头先转为IDA模式,先用列表存起来
            regexVarLine='_?.+\$?.+size.+'
            regexVar='_?.+\$? = [-|+]?\d+'
            regexSize='size = \d+'
            if re.search(regexVarLine,fileContext[lineNum]):
                name, rest = fileContext[lineNum].split(';', 1)
                matchName=re.search(regexVar,name)
                name, offset = matchName.group().split('=',1)
                name = name.strip()
                if '_' == name[0] and '$' == name[len(name) - 1]:
                    name = name[1:len(name)-1]
                elif '_' == name[0] and '$' == name[len(name) - 2]:
                    name = name[1:len(name) - 2]
                offset = offset.strip()
                matchSize = re.search(regexSize,rest)
                left,right = matchSize.group().split('=',1)
                right=right.strip()
                wordNum='unknow'
                """
                if right == '1':
                    wordNum = 'byte'
                elif right == '2':
                    wordNum = 'word'
                elif right == '4':
                    wordNum = 'dword'
                elif right == '8':
                    wordNum == 'qword'
                """
                for eachl in fileContext:
                    if '_'+name+'$[ebp' in eachl or '_'+name+'$[rsp' in eachl or name + '[ebp' in eachl or name + '[rsp' in eachl:
                        if 'DWORD PTR' in eachl:
                            wordNum = 'dword'
                            break
                        elif 'QWORD PTR' in eachl:
                            wordNum = 'qword'
                            break
                        elif 'WORD PTR' in eachl:
                            wordNum = 'word'
                            break
                        elif 'BYTE PTR' in eachl:
                            wordNum = 'byte'
                            break
                
                varname.append(name)
                varsave.append(name+'\t\t='+' '+wordNum+' ptr ' +offset+'\n')
                continue

            #函数名转为ida格式
            regexfname="_?.+ PROC"
            if re.search(regexfname,fileContext[lineNum].strip()) and fileContext[lineNum+1][0]==' ':
                newfileContext.append(fileContext[lineNum].replace('PROC','proc near'))
                for each in varsave:
                    newfileContext.append(each)
                continue

            #开始转换正文
            for eachvar in varname:
                if '_'+eachvar+'$[ebp' in fileContext[lineNum]:
                    fileContext[lineNum]=fileContext[lineNum].replace('_'+eachvar+'$[ebp','[ebp+'+eachvar)
                    break
                elif '_'+eachvar+'$[rsp' in fileContext[lineNum]:
                    fileContext[lineNum]=fileContext[lineNum].replace('_'+eachvar+'$[rsp','[rbp+'+eachvar)
                    break
                elif eachvar+'[ebp' in fileContext[lineNum]:
                    fileContext[lineNum]=fileContext[lineNum].replace(eachvar+'[ebp','[ebp+'+eachvar)
                    break
                elif eachvar+'[rsp' in fileContext[lineNum]:
                    fileContext[lineNum]=fileContext[lineNum].replace(eachvar+'[rsp','[rbp+'+eachvar)
                    break

            #结尾符号
            if 'ENDP'in fileContext[lineNum]:
                fileContext[lineNum]=fileContext[lineNum].replace('ENDP','endp')
            
            newfileContext.append(fileContext[lineNum])
            
    #输出
    with open(path,'w') as file:
        for eachline in newfileContext:
            #print(eachline,end='')
            file.write(eachline)

            
    print('godblot format --> IDA format')
else:
    print('unknown format')

print('OK')
