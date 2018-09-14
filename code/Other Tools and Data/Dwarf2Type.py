#此脚本忽略了dwarf信息中的结构类型，生成的类型信息中将不包含结构变量
#DW_TAG_structure_type 和 DW_TAG_typedef 没找

import re

###########################
### Function definition ###
###########################

def main():
    filePath = 'dwarf.txt' #dwarf文件的路径
    TransformDwarfFile(filePath) #提取dwarf中的类型信息并输出
    
def TransformDwarfFile(path):
    try:
        with open(path, 'r', encoding= 'utf-8') as file:
            #先把文件内容读出来，存在fileContext里面
            fileContext = file.readlines()
            ContextLen = len(fileContext)

            #第一次扫描取出base_type信息
            varCollection = [] #该列表用于保存base_type信息
            varGlobal = [] #该列表用于保存全局变量的信息
            for lineNum in range(0, ContextLen):
                matBaseType = re.search("< ?1><(.+)>.*(DW_TAG_base_type).*", fileContext[lineNum])
                matPointerType = re.search("< ?1><(.+)>.*DW_TAG_pointer_type.*", fileContext[lineNum])
                matArraryType = re.search("< ?1><(.+)>.*(DW_TAG_array_type).*", fileContext[lineNum])
                matConstType = re.search("< ?1><(.+)>.*(DW_TAG_const_type).*", fileContext[lineNum])
                if matBaseType:
                    basetypeAdress=matBaseType.groups()[0]
                    if not basetypeAdress[0:2]=='0x':
                        basetypeAdress ='0x' + basetypeAdress
                    basetypeName='uk'
                    for k in range(1,10):
                        if fileContext[lineNum+k].strip()=='' or re.search("<.+><.+>",fileContext[lineNum+k]):
                            break
                        else:
                            #变量的类型
                            matName = re.search('DW_AT_name', fileContext[lineNum + k])
                            if matName:
                                fileContext[lineNum + k] = fileContext[lineNum + k].replace(':','')
                                if '(' in fileContext[lineNum + k] and ')' in fileContext[lineNum + k]:
                                    a=fileContext[lineNum + k].find('(')
                                    b=fileContext[lineNum + k].find(')')
                                    fileContext[lineNum + k] =fileContext[lineNum + k][0:a]+fileContext[lineNum + k][b+1:]
                                if '<' in fileContext[lineNum + k] and '>' in fileContext[lineNum + k]:
                                    a=fileContext[lineNum + k].find('<')
                                    b=fileContext[lineNum + k].find('>')
                                    fileContext[lineNum + k] =fileContext[lineNum + k][0:a]+fileContext[lineNum + k][b+1:]
                                basetypeName = fileContext[lineNum + k].replace('DW_AT_name', '')
                                basetypeName = basetypeName.strip()
                                if '_Bool' in basetypeName:
                                    basetypeName = basetypeName.replace('_Bool','bool')
                    varCollection.append({'basetypeAdress': basetypeAdress ,"basetypeName": basetypeName})

                elif matPointerType:
                    typeAdress = matPointerType.groups()[0]
                    if not typeAdress[0:2] == '0x':
                        typeAdress = '0x' + typeAdress
                    # 从basetype中找
                    for k in range(1, 5):
                        if fileContext[lineNum + k].strip() == '' or re.search("<.+><.+>",fileContext[lineNum + k]):
                            break
                        else:
                            matType = re.search('DW_AT_type.+<(\w+)>', fileContext[lineNum + k])
                            if matType:
                                flag=1
                                for each in varCollection:
                                    if matType.groups()[0] == each['basetypeAdress']:
                                        typeName = each['basetypeName'] + '*'
                                        varCollection.append({'basetypeAdress': typeAdress, "basetypeName": typeName})
                                        flag=1
                                        break
                                if flag==0:
                                    varCollection.append({'basetypeAdress': typeAdress, "basetypeName": '*'})

                elif matArraryType:
                    typeAdress = matArraryType.groups()[0]
                    if not typeAdress[0:2] == '0x':
                        typeAdress = '0x' + typeAdress
                    # 从basetype中找
                    for k in range(1,5):
                        if fileContext[lineNum+k].strip()=='' or re.search("<.+><.+>",fileContext[lineNum+k]):
                            break
                        else:
                            matType = re.search('DW_AT_type.+<(\w+)>', fileContext[lineNum + k])
                            if matType:
                                for each in varCollection:
                                    if matType.groups()[0] == each['basetypeAdress']:
                                        typeName = each['basetypeName'] + '[]'
                                        varCollection.append({'basetypeAdress': typeAdress, "basetypeName": typeName})
                                        break

                elif matConstType:
                    typeAdress = matConstType.groups()[0]
                    if not typeAdress[0:2] == '0x':
                        typeAdress = '0x' + typeAdress
                    # 从basetype中找
                    for k in range(1, 5):
                        if fileContext[lineNum + k].strip() == '' or re.search("<.+><.+>", fileContext[lineNum + k]):
                            break
                        else:
                            matType = re.search('DW_AT_type.+<(\w+)>', fileContext[lineNum + k])
                            if matType:
                                for each in varCollection:
                                    if matType.groups()[0] == each['basetypeAdress']:
                                        typeName = 'const ' + each['basetypeName']
                                        varCollection.append({'basetypeAdress': typeAdress, "basetypeName": typeName})
                                        break


            #第二次扫描取出更复杂一点的信息，指针和全局变量
            for lineNum in range(0, ContextLen):
                matPointerType = re.search("< ?1><(.+)>.*DW_TAG_pointer_type.*", fileContext[lineNum])
                matGlobalType = re.search("< ?1><(.+)>.*DW_TAG_variable.*", fileContext[lineNum])
                if matPointerType:
                    typeAdress = matPointerType.groups()[0]
                    if not typeAdress[0:2] == '0x':
                        typeAdress = '0x' + typeAdress
                    # 从basetype中找
                    for k in range(1, 5):
                        if fileContext[lineNum + k].strip() == '' or re.search("<.+><.+>", fileContext[lineNum + k]):
                            break
                        else:
                            matType = re.search('DW_AT_type.+<(\w+)>', fileContext[lineNum + k])
                            flag = 0
                            if matType:
                                for each in varCollection:
                                    if matType.groups()[0] == each['basetypeAdress']:
                                        typeName = each['basetypeName'] + '*'
                                        varCollection.append({'basetypeAdress': typeAdress, "basetypeName": typeName})
                                        flag = 1
                                        break
                                if flag == 0:
                                    varCollection.append({'basetypeAdress': typeAdress, "basetypeName": 'unknown*'})

                elif matGlobalType:
                    globaltypeAdress = matGlobalType.groups()[0]
                    globaltypeName = 'uk'
                    globaltypeCode = 'uk'
                    for k in range(1, 10):
                        if fileContext[lineNum + k].strip() == '' or re.search("<.+><.+>", fileContext[lineNum + k]):
                            break
                        else:
                            # 变量的类型
                            matName = re.search('DW_AT_name', fileContext[lineNum + k])
                            matTypeCode = re.search('DW_AT_type.+<(\w+)>', fileContext[lineNum + k])
                            if matName:
                                fileContext[lineNum + k] = fileContext[lineNum + k].replace(':', '')
                                if '(' in fileContext[lineNum + k] and ')' in fileContext[lineNum + k]:
                                    a = fileContext[lineNum + k].find('(')
                                    b = fileContext[lineNum + k].find(')')
                                    fileContext[lineNum + k] = fileContext[lineNum + k][0:a] + fileContext[lineNum + k][b + 1:]
                                if '<' in fileContext[lineNum + k] and '>' in fileContext[lineNum + k]:
                                    a = fileContext[lineNum + k].find('<')
                                    b = fileContext[lineNum + k].find('>')
                                    fileContext[lineNum + k] = fileContext[lineNum + k][0:a] + fileContext[lineNum + k][b + 1:]
                                globaltypeName = fileContext[lineNum + k].replace('DW_AT_name', '')
                                globaltypeName = globaltypeName.strip()
                            elif matTypeCode:
                                globaltypeCode = matTypeCode.groups()[0]
                    varGlobal.append({'globaltypeCode': globaltypeCode, "globaltypeName": globaltypeName})


            #第三次扫描取出函数信息(已改善，紧接着第二次后面)
            for lineNum in range(0, ContextLen):
                matSubProgram = re.search("< ?1><.+>.*DW_TAG_subprogram.*", fileContext[lineNum])
                if matSubProgram:
                    i = 1
                    SubProgramName='uk'
                    SubProgramType='uk'
                    varList=[]#后面用于保存该函数的变量信息
                    #此处找出该函数的信息
                    while True:
                        if lineNum+i == ContextLen -1:
                            break
                        if fileContext[lineNum+i].strip()=='' or re.search("<.+><.+>",fileContext[lineNum+i]):#跳出循环的条件
                            break
                        else:
                            #函数名
                            matName = re.search('DW_AT_name', fileContext[lineNum + i])
                            matType = re.search('DW_AT_type.+<(\w+)>', fileContext[lineNum + i])
                            if matName:
                                fileContext[lineNum + i] = fileContext[lineNum + i].replace(':', '')
                                if '(' in fileContext[lineNum + i] and ')' in fileContext[lineNum + i]:
                                    a = fileContext[lineNum + i].find('(')
                                    b = fileContext[lineNum + i].find(')')
                                    fileContext[lineNum + i] = fileContext[lineNum + i][0:a] + fileContext[lineNum+i][b+1:]
                                if '<' in fileContext[lineNum + i] and '>' in fileContext[lineNum + i]:
                                    a = fileContext[lineNum + i].find('<')
                                    b = fileContext[lineNum + i].find('>')
                                    fileContext[lineNum + i] = fileContext[lineNum + i][0:a] + fileContext[lineNum+i][b+1:]
                                SubProgramName = fileContext[lineNum + i].replace('DW_AT_name', '')
                                SubProgramName = SubProgramName.strip()
                            #函数的返回类型
                            elif matType:
                                #从varCollection中找
                                for each in varCollection:
                                    if matType.groups()[0]==each['basetypeAdress']:
                                        SubProgramType = each['basetypeName']
                            #循环过程中在改变的量
                            i = i + 1

                    #print(SubProgramName)
                    #print(SubProgramType)

                    #此处找的是DW_TAG_formal_parameter和DW_TAG_variable
                    while True:
                        #跳出循环的条件
                        if lineNum+i == ContextLen -1:
                            break
                        elif fileContext[lineNum + i].strip() == '' or re.search("< ?1><.+>", fileContext[lineNum + i]):
                            break

                        #查找DW_TAG_formal_parameter和DW_TAG_variable
                        matParameter = re.search("< ?2><.+>.*DW_TAG_formal_parameter.*", fileContext[lineNum + i])
                        matVariable  = re.search("< ?2><.+>.*DW_TAG_variable.*", fileContext[lineNum + i])

                        if matParameter or matVariable:
                            varName='uk'
                            varType='uk'
                            for k in range(1,10):
                                if fileContext[lineNum + i + k].strip() == '' or re.search("<.+><.+>", fileContext[lineNum + i + k]):
                                    i = i + k - 1
                                    break
                                else:
                                    #变量名字
                                    matName = re.search('DW_AT_name', fileContext[lineNum + i + k])
                                    matType = re.search('DW_AT_type.+<(\w+)>', fileContext[lineNum + i + k])
                                    if matName:
                                        fileContext[lineNum + i + k] = fileContext[lineNum + i + k].replace(':', '')
                                        if '(' in fileContext[lineNum + i + k] and ')' in fileContext[lineNum + i + k]:
                                            a = fileContext[lineNum + i + k].find('(')
                                            b = fileContext[lineNum + i + k].find(')')
                                            fileContext[lineNum + i + k] = fileContext[lineNum + i + k][0:a] + fileContext[lineNum + i + k][b + 1:]
                                        if '<' in fileContext[lineNum + i + k] and '>' in fileContext[lineNum + i + k]:
                                            a = fileContext[lineNum + i + k].find('<')
                                            b = fileContext[lineNum + i + k].find('>')
                                            fileContext[lineNum + i + k] = fileContext[lineNum + i + k][0:a] + fileContext[lineNum + i + k][b + 1:]
                                        varName = fileContext[lineNum + i + k].replace('DW_AT_name', '')
                                        varName = varName.strip()
                                        #print(varName)
                                    #变量类型
                                    elif matType:
                                        # 从varCollection中找
                                        for each in varCollection:
                                            if matType.groups()[0] == each['basetypeAdress']:
                                                varType = each['basetypeName']
                                                break
                                        #print(varType)
                            if matParameter:
                                varList.append({'varName':varName, 'varType':varType, 'PorV':'parameter'})
                            elif matVariable:
                                varList.append({'varName':varName, 'varType':varType, 'PorV':'variable'})
                        # 循环过程中在改变的量
                        i = i + 1

                    #输出结果
                    print(SubProgramType, end=' ')
                    print(SubProgramName, end='(){\n')

                    if not varList==[]:
                        for each in varList:
                            if each['varName']!='uk' and each['varType']!='uk':
                                if each['PorV'] == 'parameter':
                                    print('    ', end='') 
                                    print(each['PorV'], end=': ')
                                    print(each['varType'], end=' ')
                                    print(each['varName'], end=';\n')
                                else:
                                    print('\t', end='') 
                                    print(each['varType'], end=' ')
                                    print(each['varName'], end=';\n')
                    print("}\n")

            #输出全局变量
            if not varGlobal == []:
                for eachGvar in varGlobal:
                    for each in varCollection:
                        if eachGvar['globaltypeCode'] == each['basetypeAdress']:
                            print('variable: ', end = '')
                            print(each['basetypeName'], end = ' ')
                            print(eachGvar['globaltypeName'], end=';\n')
                            
    except IOError as err:
        print('File error:' + str(err))



##########################
### executing the code ###
##########################

main()
