#-*-coding:utf-8-*-
import re

#函数File2List将一个文件中的每一行作为字符串变量存放于一个列表中
#该函数的参数为文件的地址
def File2List(filelocalname):
    temp_List=[]
    try:
        with open(filelocalname) as file:
            for line in file.readlines():
                temp_List.append(line.strip())
        return (temp_List)
    except IOError as err:
        print('File error:'+str(err))

def VectorAddVector(a,b):
    for i in range(0,len(a)):
        if a[i] > b[i]:
            #a[i] = a[i]
            pass
        else:
            a[i] = b[i]
    for j in range(0,len(b)):
        b[j]=a[j]

def VectorReplaceVector(a,b):
    for j in range(0,len(b)):
        b[j]=a[j]

def GlobalVectorAddGlobalVector(a,b):
    for i in range(0,len(a)):
        if a[i] == 0 and b[i]!=0:
            a[i] = b[i]
        elif a[i] == 75 or a[i] == 25:
            pass
        else:
            a[i] = a[i] + b[i]

def CallingFile2ParaList(filelocalname):
    temp_List = []
    try:
        with open(filelocalname) as file:
            for line in file.readlines():
                if line.strip() != '':
                    ParaName , ParaType = line.split('\t',1)
                    temp_List.append({'funcPara': ParaName.strip(), 'paraType': ParaType.strip()})
        return (temp_List)
    except IOError as err:
        print('File error:' + str(err))

def child(TempRegister):
    if TempRegister == 'eax':
        return 'ax,al'
    elif TempRegister == 'ebx':
        return 'bx,bl'
    elif TempRegister == 'ecx':
        return 'cx,cl'
    elif TempRegister == 'edx':
        return 'dx,dl'
    elif TempRegister == 'rax':
        return 'eax,ax,al'
    elif TempRegister == 'rbx':
        return 'ebx,bx,bl'
    elif TempRegister == 'rcx':
        return 'ecx,cx,cl'
    elif TempRegister == 'rdx':
        return 'edx,dx,dl'


class FileToVector:
    def __init__(self,Type_List_file,Instructions_List_file):
        self.Type_list=File2List(Type_List_file)
        self.Instructions_list=File2List(Instructions_List_file)
        self.Name_list=[]
        self.Label_list=[]
        self.Vector_list=[]
        self.UDrelation = []
        self.UDWeakrelation = []
        self.LEArelation = []
        self.function_parameter_list = CallingFile2ParaList('SaveData/Normalization/FuncPara_List.txt')

    def UpdateUDrelation(self):
        if self.UDrelation != []:
            for each in self.UDrelation:
                left,right=each.split('---')
                if ':ds:' in left or ':ds:' in right:
                    break
                #print(left,end='---')
                #print(right)
                f=0
                s=0
                flagFS = 0
                for i in range(0,len(self.Name_list)):
                    for j in range(0,len(self.Name_list)):
                        if left==self.Name_list[i] and right==self.Name_list[j]:
                            f=i
                            s=j
                            flagFS = 1
                            break
                    if flagFS == 1:
                        break
                VectorAddVector(self.Vector_list[f],self.Vector_list[s])
        if self.UDWeakrelation != []:
            for each in self.UDWeakrelation:
                left,right=each.split('---')
                #print(left,end='---')
                #print(right)
                f=0
                s=0
                flagFS = 0
                for i in range(0,len(self.Name_list)):
                    for j in range(0,len(self.Name_list)):
                        if left==self.Name_list[i] and right==self.Name_list[j]:
                            f=i
                            s=j
                            flagFS = 1
                            break
                    if flagFS == 1:
                        break
                VectorReplaceVector(self.Vector_list[s],self.Vector_list[f])


    #函数File2Vector将一个汇编代码文件中的每个变量用一个向量的形式表示
    #该函数的第一个参数为汇编代码文件的地址,第二个参数为从源代码提取的类型信息的文件
    def File2Vector(self,filename,type_file):
        variables=[]#用于保存各个变量的信息的列表，列表中的元素是字典
        var_orgrin_type=[]#var_orgrin_type是个列表，每个函数的类型信息用一个词典来表示，例子如下：[{'functionName':func,'varType':['int a','int b','int c']}]
        newPointerList = []  # 新预测的指针

        try:
            #打开从源代码提取的类型信息的文件
            with open(type_file) as typefile:
                tempDict={'functionName':'','varType':[]}
                for line in typefile.readlines():
                    if "function:" in line:
                        left,right=line.strip().split(':',1)
                        left,right=right.strip().split('(',1)
                        tempDict['functionName']=left.strip()
                    elif "parameter:" in line:
                        left,right=line.strip().split(':',1)
                        p = re.compile('[,|)]')
                        right = p.sub("",right)
                        p = re.compile('\[.*\]')
                        right = p.sub("[]", right)
                        right=right.strip()+";"
                        tempDict['varType'].append(right)
                    elif "variable:" in line:
                        left,right=line.strip().split(':',1)
                        declar=right
                        p = re.compile('\[.*\]')#去除一些无用的符号
                        declar=p.sub("[]",declar)
                        declar=declar.strip()
                        tempDict['varType'].append(declar)
                    elif "----------" in line:
                        if not tempDict['functionName']=='':
                            var_orgrin_type.append(tempDict)
                            flag=0
                            ##print(tempDict)
                        tempDict={'functionName':'','varType':[]}
                    else:
                        pass
        except IOError as err:
            print('File error:'+ str(err))

        #print(var_orgrin_type)

        try:#打开汇编代码文件
            with open(filename,encoding='utf-8') as assemblyfile:

                flagg=0 #0表示还没找到函数名，1表示找到函数名
                for line in assemblyfile.readlines():
                    line = line.replace("\t", "\t ")
                    #得到函数名functionName
                    if flagg==0:
                        if re.search(".*__cdecl [a-zA-Z_]([a-zA-Z_]|[0-9])*(.*(,.+)*)",line):
                            functionReType,rest=line.strip().split('__cdecl',1)
                            functionName,parameterList=rest.strip().split('(',1)
                            functionName=functionName.strip()
                            flagg = 1
                        else:
                            if re.search('proc near',line):
                                functionReType, rest = line.strip().split('proc near', 1)
                                functionName = functionReType.strip()

                                if re.search('\??.+@@',functionName):
                                    pattern = re.compile("\??(.+)@@")
                                    res = pattern.search(functionName).groups()
                                    functionName=res[0].strip()
                                elif re.search('\?.+@@',functionName):
                                    pattern = re.compile("\?(.+)@@")
                                    res = pattern.search(functionName).groups()
                                    functionName=res[0].strip()
                                elif re.search('.+@@',functionName):
                                    pattern = re.compile("(.+)@@")
                                    res = pattern.search(functionName).groups()
                                    functionName=res[0].strip()
                                elif re.search('_Z[0-9](.+)P.+',functionName):
                                    pattern = re.compile("_Z[0-9](.+)P.+")
                                    res = pattern.search(functionName).groups()
                                    functionName=res[0].strip()
                                elif functionName[0] == '_':
                                    functionName = functionName[1:]
                                flagg = 1
                        #print(functionName)
                
                    #将汇编代码中的局部变量找出，并将其基本信息用一个字典的结构保存，结果追加到variables列表中
                    if re.search("[a-zA-Z_]([a-zA-Z_]|[0-9])*[ \t]*=[ \t]*.+ptr.+", line):
                        varName,rest=line.strip().split('=',1)
                        byteNum,offset=rest.strip().split('ptr',1)
                        if functionName == 'main' or functionName =='_tmain':#剔除掉main函数的三个参数
                            if varName.strip()=='argc' or varName.strip()=='argv' or varName.strip()=='envp':
                                continue
                        variables.append({'varName':varName.strip(),'byteNum':byteNum.strip(),'offset':offset.strip()})

                #print(variables)

                assemblyfile.seek(0)  # 使用seek()方法返回到文件起始位置
                fileContext = assemblyfile.readlines() #把文档内容存起来先
                assemblyfile.seek(0)
                ContextLen = len(fileContext)

                #下面这个for循环将每个变量相关的语句找出
                for each_var in variables:
                    Vector_list_element=[]#Vector_list的组成元素,初始化为全0
                    for i in range(len(self.Instructions_list)):         
                        Vector_list_element.append(0)

                    #定义一个下面经常用的函数
                    #在指令字典中查找，如果有的话就在相应的向量位置上+1
                    def updataVector(IR):
                        # 在指令字典中查找，如果有的话就在相应的向量位置上+1
                        count = 0
                        for each_instruction in self.Instructions_list:
                            if each_instruction == IR:
                                # 人为按情况调整权重
                                if IR == 'mov _ bool':
                                    Vector_list_element[count + 1] += 1  # 0和1同时也算立即数
                                if IR == 'cmp _ bool':
                                    Vector_list_element[count + 1] += 1  # 0和1同时也算立即数

                                if 'FP' in IR:
                                    Vector_list_element[count] += 2
                                    if 'FPptr' in IR:
                                        Vector_list_element[count] += 8
                                if 'address'in IR:
                                    #print(IR)
                                    Vector_list_element[count] =25
                                    break
                                Vector_list_element[count] += 1
                                break
                            elif each_instruction == '#':
                                if IR!='UK' and IR!='not _' and IR!='push' and IR!='FPvoid' and IR!='FPstruct':
                                    print(IR , end=' \tmissing\n')#总集里没有的指令输出看看
                                    pass
                                break
                            count += 1

                    #print(each_var)
                    issearchwordptr = 0

                    for lineNum in range(0, ContextLen):
                        # 有些文本不适应，后面要按照空格分割，先把\t 全换成空格
                        fileContext[lineNum] = fileContext[lineNum].replace('\t', ' \t')

                        """
                        #查找有没有[ebp+...+varname+...]的形式
                        regex1= '\[(ebp|rbp)(\[\+|-].+)+[\+|-]' + each_var['varName'] + '([\+|-][0-9][0-9a-fA-F]*h?)*\]'
                        regex2= '\[(ebp|rbp)(\[\+|-].+)*[\+|-]' + each_var['varName'] + '([\+|-][0-9][0-9a-fA-F]*h?)+\]'
                        if re.search(regex1,fileContext[lineNum]) or re.search(regex2,fileContext[lineNum]):
                            count=0
                            for each_instruction in self.Instructions_list:
                                if each_instruction=='bias in stackframe':
                                    Vector_list_element[count]=25
                                    break
                                count+=1
                                """
                        #查找[ebp+...+varname+...]的相关语句
                        varNameinregex = each_var['varName'].replace('rregg', '(rax|rbx|rcx|rdx)')
                        varNameinregex = varNameinregex.replace('reg', '(eax|ebx|ecx|edx)')
                        varNameinregex = varNameinregex.replace('al', '(al|bl|cl|dl|)')
                        varNameinregex = varNameinregex.replace('ax', '(ax|bx|cx|dx|)')

                        # 只有qword才能把+4偏移量放一起,例外
                        if each_var['byteNum'] == 'qword':
                            varNameinregex = '('+ varNameinregex + '|' + varNameinregex + '+4)'
                            #print(varNameinregex)

                        regex='\[(ebp|rbp)\+(.*\+)?' + varNameinregex.replace('+','\+') + '\]'# Deatil版本的是需要.replace('+','\+')

                        if re.search(regex,fileContext[lineNum]):
                            # 对于既不是dword，又不是qword和word的，但是不考虑byte，因为无debuginfo时IDA强行认为结构就是byte
                            if (each_var['byteNum'] != 'word' and each_var['byteNum'] != 'dword' and each_var['byteNum'] != 'qword') or re.search('\+\d+', each_var['varName']):
                                if issearchwordptr == 0 and re.search('[Pp][Tt][Rr][ ]*\[(ebp|rbp)\+' + each_var['varName'].replace('+','\+') + '\]',fileContext[lineNum]):
                                    issearchwordptr = 1
                                    if 'qword ptr' in fileContext[lineNum] or 'QWORD PTR' in fileContext[lineNum]:
                                        count = 0
                                        for each_instruction in self.Instructions_list:
                                            if each_instruction == 'qword':
                                                Vector_list_element[count] = 75
                                                break
                                            count += 1
                                    elif 'dword ptr' in fileContext[lineNum] or 'DWORD PTR' in fileContext[lineNum]:
                                        count = 0
                                        for each_instruction in self.Instructions_list:
                                            if each_instruction == 'dword':
                                                Vector_list_element[count] = 75
                                                break
                                            count += 1
                                    elif 'word ptr' in fileContext[lineNum] or 'WORD PTR' in fileContext[lineNum]:
                                        count = 0
                                        for each_instruction in self.Instructions_list:
                                            if each_instruction == 'word':
                                                Vector_list_element[count] = 75
                                                break
                                            count += 1
                                    elif 'byte ptr' in fileContext[lineNum] or 'BYTE PTR' in fileContext[lineNum]:
                                        count = 0
                                        for each_instruction in self.Instructions_list:
                                            if each_instruction == 'byte':
                                                Vector_list_element[count] = 75
                                                break
                                            count += 1

                            head,rest=fileContext[lineNum].strip().split(' ',1)
                            head=head.strip()
                            #用字符串来将各个指令化成统一的代表形式，即指令全集中的表示
                            instructionIR='UK'
                            #没有逗号的就是一元指令
                            if not ',' in fileContext[lineNum]:
                                # 关于push找call
                                if head == 'push':
                                    funcPara='..'
                                    Pi = 1
                                    for j in range(1, 15):
                                        if lineNum+j >= ContextLen:
                                            break
                                        if lineNum+j < ContextLen:
                                            regexCall = 'call[ \t]*(\w+)$'
                                            matCall = re.search(regexCall, fileContext[lineNum + j])
                                            if matCall:
                                                funcPara = matCall.groups()[0] + 'P' + str(Pi)
                                                break
                                            elif 'push' in fileContext[lineNum + j]:
                                                if re.search('\[ebp\+\w+\+4\]',fileContext[lineNum + j]) and re.search('\[ebp\+\w+\]',fileContext[lineNum+j+1]):
                                                    continue
                                                else:
                                                    Pi = Pi + 1
                                    if funcPara!='..':
                                        for each in self.function_parameter_list:
                                            if funcPara == each['funcPara'] or funcPara == '_' + each['funcPara']:
                                                if '*' in each['paraType']:
                                                    if each_var['byteNum'] == 'dword':
                                                        updataVector('FPptr')
                                                        if '*' == each['paraType']:
                                                            break
                                                        updataVector('FP' + re.sub('[^_a-zA-Z0-9]','',each['paraType']))
                                                else:
                                                    if each_var['byteNum'] == 'byte' and (each['paraType'] =='int' or '*' in each['paraType']):
                                                            break
                                                    else:
                                                        updataVector('FP' + re.sub('[^_a-zA-Z0-9]','',each['paraType']))

                                                # print(each_var['varName'],end='--')
                                                # print(each['paraType'])
                                                break

                                #对于某些一元指令，这里只考虑div、idiv、fstp、fld
                                elif head=='div':
                                    instructionIR='div _'
                                elif head=='idiv':
                                    instructionIR='idiv _'
                                elif head=='fstp':
                                    instructionIR='fstp _'
                                elif head=='fld':
                                    instructionIR='fld _'
                                elif 'FP' in head:
                                    instructionIR = head
                                else:
                                    instructionIR=head+' _'
                            #有逗号的就是二元指令
                            else:
                                rest,subn_num=re.subn("\[.+\]","_",rest)
                                rest,subn_num=re.subn("xmm[0-7]","xmm",rest)
                                rest,subn_num=re.subn("(?:rax|rbx|rcx|rdx|rsi|rdi)(?!\w)", "rregg", rest)
                                rest,subn_num=re.subn("(?:eax|ebx|ecx|edx|esi|edi)(?!\w)", "reg", rest)
                                rest,subn_num=re.subn("(?:ax|bx|cx|dx|si|di)(?!\w)", "ax", rest)
                                rest,subn_num=re.subn("(?:al|bl|cl|dl|ah|bh|ch|dh)(?!\w)", "al", rest)

                                if ',' not in rest:
                                    continue

                                left,right=rest.strip().split(',',1)
                                right=right.strip()
                                left=left.strip()
                                #head中有cvtt和cvt时，删掉2后面的。例如cvttsd2ss改写成cvtsd
                                if 'cvt' in head:
                                    if 'cvtt' in head:
                                        head = head.replace('cvtt', 'cvt')
                                    head=head[0:5]
                                    instructionIR = head
                                # 实际上lea没什么意义，关键是lea到寄存器后，寄存器中数据的走向，下一个变量往上回朔时反而加上lea更靠谱
                                elif 'lea' in head:
                                    #找出变量间指针的指向关系
                                    try:
                                        head, rest = fileContext[lineNum].strip().split(' ', 1)
                                        left, right = rest.strip().split(',', 1)
                                        tempregister = left.strip()#lea那一行的寄存器
                                        head, rest = fileContext[lineNum+1].strip().split(' ', 1)
                                        left, right = rest.strip().split(',', 1)
                                        nextregister = right.strip()#lea后面一行的寄存器
                                        if head=='mov' and tempregister==nextregister:
                                            if '[ebp+'in left or '[rbp+'in left:
                                                regexVar = '\[(ebp|rbp)\+.+\]'
                                                matchName = re.search(regexVar, left)
                                                left = matchName.group()
                                                next_var = left.replace('[ebp+','')
                                                next_var = next_var.replace('[rbp+','')
                                                next_var = next_var.replace(']', '')
                                                if not '+' in next_var:
                                                    self.LEArelation.append(functionName+':'+next_var + ' -> '+functionName+':'+each_var['varName'])
                                                    #print(next_var + ' -> '+each_var['varName'])
                                    except:
                                        pass
                                #判断下划线在左边还是右边
                                #如果下划线在左边
                                elif '_' in left.strip():
                                    #先看mov _0/1这种明显特征，不是0/1统一转成imm
                                    if (right.strip() == '0' or right.strip() == '1') and (head=='mov' or head== 'cmp'):
                                        instructionIR = head + ' _ bool'

                                    else:
                                        right, subn_num = re.subn("(0x)?[0-9][0-9a-fA-F]*h?(?!\w)", "imm", right)#不是单独的0或1 都看成是立即数
                                        # 首先检查逗号右边是不是offset和立即数
                                        if right.find('offset')!=-1:
                                            instructionIR=head+' _ offset'
                                        elif right.find('imm')!=-1:
                                            instructionIR=head+' _ '+"imm"
                                        #不是offset和立即数的情况一般就是mov了
                                        #mov的情况特殊处理,变量在左边和右边的情况视为相同
                                        elif not head.find('mo')==-1:
                                            instructionIR=head+' '+right
                                            """
                                        #下面考虑到mov reg的特殊情况，把reg替换成变量返回往上找
                                        """
                                            # 考虑到mov reg的特殊情况，把reg替换成变量返回往上找
                                            # 此处千万别改动instructionIR
                                            instructHead, instructRest = fileContext[lineNum].strip().split(' ', 1)
                                            instructLeft, instructRight = instructRest.strip().split(',', 1)
                                            # 准确提取到底是哪个寄存器，后面有用
                                            TempRegister = instructRight.strip()

                                            registerInstruction = 'UK'  # 作用类似instructionIR
                                            try:
                                                for k in range(1, 6):
                                                    fileContext[lineNum - k] = fileContext[lineNum - k].replace('\t',' \t')
                                                    if lineNum - k > 0 and ',' in fileContext[lineNum - k]:
                                                        #print(fileContext[lineNum - k],end='')
                                                        #print(fileContext[lineNum])
                                                        instructHead, instructRest = fileContext[lineNum - k].strip().split(' ', 1)
                                                        instructLeft, instructRight = instructRest.strip().split(',', 1)
                                                        instructRight = instructRight.strip()
                                                        instructLeft = instructLeft.strip()
                                                        if TempRegister in instructLeft:  # 如果出现在左边
                                                            # 那么看下有没有取值的行为
                                                            if instructLeft == TempRegister:
                                                                instructLeft, subn_num = re.subn("xmm[0-7]", "xmm",instructLeft)
                                                                instructLeft, subn_num = re.subn("(?:rax|rbx|rcx|rdx|rsi|rdi)(?!\w)", "rregg", instructLeft)
                                                                instructLeft, subn_num = re.subn("(?:eax|ebx|ecx|edx|esi|edi)(?!\w)", "reg",instructLeft)
                                                                instructLeft, subn_num = re.subn("(?:ax|bx|cx|dx|si|di)(?!\w)", "ax",instructLeft)
                                                                instructLeft, subn_num = re.subn("(?:al|bl|cl|dl|ah|bh|ch|dh)(?!\w)", "al",instructLeft)
                                                                # 因为这里是寄存器代替_，与变量不同。这里的和处理就是换位置，比如add _ reg换位成add reg _
                                                                if 'cvt' in instructHead:
                                                                    if 'cvtt' in instructHead:
                                                                        instructHead=instructHead.replace('cvtt','cvt')
                                                                    instructHead='cvt'+instructHead[6:8]
                                                                    registerInstruction=instructHead
                                                                elif instructHead == 'cmp':
                                                                    registerInstruction = 'cmp ' + instructLeft
                                                                elif 'mo' in instructHead:
                                                                    registerInstruction = instructHead+' '+instructLeft
                                                                else:
                                                                    registerInstruction = instructHead + ' ' + instructLeft + ' _'
                                                            elif re.search(regexregister, instructLeft):
                                                                if 'ebp' not in instructLeft and 'rbp' not in instructLeft:  # 有ebp的话就跟你无关了
                                                                    if re.search(regexOnlyregister, instructLeft):
                                                                        registerInstruction = '[address]'
                                                                    else:
                                                                        updataVector('[address]')
                                                                        registerInstruction = '[?+address+?]'
                                                                    newPointerList.append({'PointName': each_var['varName'],
                                                                                            'head': instructHead,
                                                                                            'TempTegister': TempRegister,
                                                                                            'InstructionNear': instructRight,
                                                                                            'keyInstruction': instructLeft.replace(TempRegister, each_var['varName']),
                                                                                            'PointNameOrigin': each_var['varName']})

                                                        elif TempRegister in instructRight:  # 如果出现在右边
                                                            if instructRight == TempRegister:
                                                                instructRight, subn_num = re.subn("xmm[0-7]", "xmm",instructRight)
                                                                instructRight, subn_num = re.subn("(?:rax|rbx|rcx|rdx|rsi|rdi)(?!\w)", "rregg",instructRight)
                                                                instructRight, subn_num = re.subn("(?:eax|ebx|ecx|edx|esi|edi)(?!\w)", "reg",instructRight)
                                                                instructRight, subn_num = re.subn("(?:ax|bx|cx|dx|si|di)(?!\w)", "ax",instructRight)
                                                                instructRight, subn_num = re.subn("(?:al|bl|cl|dl|ah|bh|ch|dh)(?!\w)", "al",instructRight)
                                                                if instructHead == 'cmp':  # mov的情况已经没有，但还有cmp
                                                                    registerInstruction = 'cmp ' + instructRight
                                                                elif 'mo' in instructHead:
                                                                    registerInstruction = instructHead + ' ' + instructRight
                                                                else:
                                                                    registerInstruction = instructHead + ' ' + instructRight + ' _'
                                                            elif re.search(regexregister, instructRight):
                                                                if 'ebp' not in instructRight and 'rbp' not in instructRight:  # 有ebp的话就跟你无关了
                                                                    if re.search(regexOnlyregister, instructRight):
                                                                        registerInstruction = '[address]'
                                                                    else:
                                                                        updataVector('[address]')
                                                                        registerInstruction = '[?+address+?]'
                                                                    newPointerList.append({'PointName': each_var['varName'],
                                                                                            'head': instructHead,
                                                                                            'TempTegister': TempRegister,
                                                                                            'InstructionNear': instructLeft,
                                                                                            'keyInstruction': instructRight.replace(TempRegister, each_var['varName']),
                                                                                            'PointNameOrigin': each_var['varName']})

                                                        #print(registerInstruction)
                                                        updataVector(registerInstruction)

                                                    elif lineNum - k > 0 and 'call' in fileContext[lineNum - k]:
                                                        regexCall = 'call[ \t]*(\w+)$'
                                                        matCall = re.search(regexCall, fileContext[lineNum - k])
                                                        if matCall:
                                                            funcRe = matCall.groups()[0] + 'Re'
                                                            for each in self.function_parameter_list:
                                                                if funcRe == each['funcPara'] or funcRe == '_' + each['funcPara']:
                                                                    if '*' in each['paraType']:
                                                                        updataVector('FPptr')
                                                                        self.FP_Pointer_rel.append(functionName + ':' + each_var['varName'] + '---' + each['paraType'])
                                                                        if '*' == each['paraType']:
                                                                            break
                                                                    updataVector('FP' + re.sub('[^a-zA-Z]', '',each['paraType']))
                                                                    break

                                                    # 如果上一行找到了temp寄存器，那就要跳出
                                                    if TempRegister in fileContext[lineNum - k] or 'call' in fileContext[lineNum - k] or 'loc' in fileContext[lineNum - k] or re.search('^j.+', instructHead):
                                                        break

                                            except:
                                                pass

                                            """
                                       #下面考虑到mov reg的特殊情况，把reg替换成变量返回往上找
                                       """
                                        elif head=='cmp':
                                            instructionIR='cmp '+right
                                        else:
                                            instructionIR=head+' _ '+right
                                #如果下划线在右边
                                elif '_' in right.strip():
                                    #mov的情况特殊处理,变量在左边和右边的情况视为相同
                                    if not head.find('mo')==-1:
                                        instructionIR=head+' '+left
                                        """
                                    #下面考虑到mov reg的特殊情况，把reg替换成变量继续往下找
                                    """
                                        #考虑到mov reg的特殊情况，把reg替换成变量继续往下找
                                        #此处千万别改动instructionIR
                                        instructHead,instructRest=fileContext[lineNum].strip().split(' ',1)
                                        instructLeft,instructRight=instructRest.strip().split(',',1)
                                        #准确提取到底是哪个寄存器，后面有用
                                        TempRegister=instructLeft.strip()
                                        TempVar=instructRight.strip()
                                        TempHead=instructHead.strip()

                                        registerInstruction='UK'#作用类似instructionIR
                                        try:
                                            for k in range(1,6):
                                                fileContext[lineNum + k] = fileContext[lineNum + k].replace('\t', ' \t')
                                                ischange = 0
                                                if lineNum+k<ContextLen and ',' in fileContext[lineNum + k]:
                                                    instructHead, instructRest = fileContext[lineNum+k].strip().split(' ', 1)
                                                    instructLeft, instructRight = instructRest.strip().split(',', 1)
                                                    instructRight = instructRight.strip()
                                                    instructLeft = instructLeft.strip()
                                                    regexregister = '\[.*' + TempRegister + '.*\]'
                                                    regexOnlyregister = '\['+ TempRegister + '\]'

                                                    if instructRight in child(TempRegister) and 'arg' in each_var['varName']:
                                                        if instructHead == TempHead and instructLeft != TempVar:
                                                            matvarnameUp = re.search('\[(ebp|rbp)\+(.+)\]', TempVar)
                                                            matvarnameDown = re.search('\[(ebp|rbp)\+(.+)\]',instructLeft)
                                                            if matvarnameUp and matvarnameDown:
                                                                VarDown = matvarnameDown.groups()[1]
                                                                VarUp = matvarnameUp.groups()[1]
                                                                if not '+' in VarUp and not '+' in VarDown:
                                                                    self.UDWeakrelation.append(functionName + ':' + VarUp + '---' + functionName + ':' + VarDown)
                                                                    #print(functionName + ':' + VarUp + '---' + functionName + ':' + VarDown)

                                                    if TempRegister in instructLeft:#如果出现在左边，并且被mo说明已经被改
                                                        #那么看下有没有取值的行为
                                                        if  instructLeft==TempRegister:
                                                            ischange = 1
                                                            if 'lea' in instructHead:
                                                                continue
                                                            elif 'mo' in instructHead and '['+ TempRegister not in instructRight:
                                                                break
                                                            else:
                                                                instructLeft, subn_num = re.subn("xmm[0-7]", "xmm", instructLeft)
                                                                instructLeft, subn_num = re.subn("(?:rax|rbx|rcx|rdx|rsi|rdi)(?!\w)", "rregg",instructLeft)
                                                                instructLeft, subn_num = re.subn("(?:eax|ebx|ecx|edx|esi|edi)(?!\w)", "reg", instructLeft)
                                                                instructLeft, subn_num = re.subn("(?:ax|bx|cx|dx|si|di)(?!\w)","ax", instructLeft)
                                                                instructLeft, subn_num = re.subn("(?:al|bl|cl|dl|ah|bh|ch|dh)(?!\w)", "al", instructLeft)
                                                                #因为这里是寄存器代替_，与变量不同。这里的和处理就是换位置，比如add _ reg换位成add reg _
                                                                if re.search(regexOnlyregister, instructRight) and 'ebp' not in instructRight and 'rbp' not in instructRight:
                                                                    registerInstruction = '[address]'
                                                                elif re.search(regexregister, instructRight) and 'ebp' not in instructRight and 'rbp' not in instructRight:
                                                                    updataVector('[address]')
                                                                    registerInstruction = '[?+address+?]'
                                                                elif 'cvt' in instructHead:
                                                                    if 'cvtt' in instructHead:
                                                                        instructHead = instructHead.replace('cvtt', 'cvt')
                                                                    instructHead = instructHead[0:5]
                                                                    registerInstruction = instructHead
                                                                elif instructHead=='cmp':#mov的情况已经没有，但还有cmp
                                                                    registerInstruction = 'cmp '+instructLeft
                                                                else:
                                                                    registerInstruction = instructHead+' '+instructLeft+' _'
                                                            if '['+ TempRegister in instructRight and instructHead != 'mov':
                                                                newPointerList.append({'PointName': each_var['varName'],
                                                                                       'head': instructHead,
                                                                                       'TempTegister': TempRegister,
                                                                                       'InstructionNear': instructLeft,
                                                                                       'keyInstruction': instructRight.replace(TempRegister,each_var['varName']),
                                                                                       'PointNameOrigin': each_var['varName']})
                                                        elif re.search(regexregister,instructLeft):
                                                            if 'lea' in instructHead:
                                                                continue
                                                            if 'ebp' not in instructLeft and 'rbp' not in instructLeft:#有ebp的话就跟你无关了
                                                                if re.search(regexOnlyregister,instructLeft):
                                                                    registerInstruction='[address]'
                                                                else:
                                                                    updataVector('[address]')
                                                                    registerInstruction = '[?+address+?]'
                                                                newPointerList.append({'PointName': each_var['varName'],
                                                                                       'head': instructHead,
                                                                                       'TempTegister': TempRegister,
                                                                                       'InstructionNear': instructRight,
                                                                                       'keyInstruction': instructLeft.replace(TempRegister,each_var['varName']),
                                                                                       'PointNameOrigin': each_var['varName']})

                                                    elif TempRegister in instructRight:#如果出现在右边
                                                        if 'lea' in instructHead:
                                                            continue
                                                        if instructRight==TempRegister:
                                                            # 先找出nearby关系
                                                            if instructHead == TempHead and instructLeft != TempVar:
                                                                matvarnameUp = re.search('\[(ebp|rbp)\+(.+)\]', TempVar)
                                                                matvarnameDown = re.search('\[(ebp|rbp)\+(.+)\]',instructLeft)
                                                                if matvarnameUp and matvarnameDown:
                                                                    VarDown = matvarnameDown.groups()[1]
                                                                    VarUp = matvarnameUp.groups()[1]
                                                                    # if not '+' in VarUp and not '+' in VarDown:
                                                                    for eavar in variables:
                                                                        if VarDown == eavar['varName']:
                                                                            if eavar['byteNum'] == each_var['byteNum']:
                                                                                self.UDrelation.append(functionName + ':' + VarUp + '---' + functionName + ':' + VarDown)
                                                                                # print(functionName + ':' + VarUp + '---' + functionName + ':' + VarDown)
                                                                    # print(functionName + ':' + VarUp + '---' + functionName + ':' + VarDown)

                                                            instructRight, subn_num = re.subn("xmm[0-7]", "xmm",instructRight)
                                                            instructRight, subn_num = re.subn("(?:rax|rbx|rcx|rdx|rsi|rdi)(?!\w)", "rregg",instructRight)
                                                            instructRight, subn_num = re.subn("(?:eax|ebx|ecx|edx|esi|edi)(?!\w)", "reg",instructRight)
                                                            instructRight, subn_num = re.subn("(?:ax|bx|cx|dx|si|di)(?!\w)", "ax", instructRight)
                                                            instructRight, subn_num = re.subn("(?:al|bl|cl|dl|ah|bh|ch|dh)(?!\w)", "al",instructRight)
                                                            if 'cvt' in instructHead:
                                                                if 'cvtt' in instructHead:
                                                                    instructHead =instructHead.replace('cvtt','cvt')
                                                                instructHead=instructHead[0:5]
                                                                registerInstruction=instructHead
                                                            elif instructHead == 'cmp':  # mov的情况已经没有，但还有cmp
                                                                registerInstruction='cmp '+instructRight
                                                            elif 'mo' in instructHead:
                                                                registerInstruction=instructHead+' '+instructRight
                                                            else:
                                                                registerInstruction=instructHead+' '+instructRight+' _'
                                                        elif re.search(regexregister,instructRight):
                                                            if 'ebp' not in instructRight and 'rbp' not in instructRight:  # 有ebp的话就跟你无关了
                                                                if re.search(regexOnlyregister, instructRight):
                                                                    registerInstruction = '[address]'
                                                                else:
                                                                    updataVector('[address]')
                                                                    registerInstruction = '[?+address+?]'
                                                                newPointerList.append({'PointName': each_var['varName'],
                                                                                       'head': instructHead,
                                                                                       'TempTegister': TempRegister,
                                                                                       'InstructionNear': instructLeft,
                                                                                       'keyInstruction': instructRight.replace(TempRegister,each_var['varName']),
                                                                                       'PointNameOrigin': each_var['varName']})

                                                                if not instructHead.find('mo') == -1:
                                                                    if lineNum + k +1 < ContextLen and ',' in fileContext[lineNum + k + 1]:
                                                                        tempHead, tempRest = fileContext[lineNum + k +1 ].strip().split(' ', 1)
                                                                        tempLeft, tempRight = tempRest.strip().split(',', 1)
                                                                        tempRight = tempRight.strip()
                                                                        tempLeft = tempLeft.strip()
                                                                        if tempRight==instructLeft or (tempLeft==instructLeft and 'mo' not in tempHead):
                                                                            newPointerList.append({'PointName': each_var['varName'],
                                                                                                   'head': tempHead,
                                                                                                   'TempTegister': '',
                                                                                                   'InstructionNear': '',
                                                                                                   'keyInstruction': instructRight.replace(TempRegister,each_var['varName']),
                                                                                                   'PointNameOrigin': each_var['varName']})
                                                                            #print(fileContext[lineNum + k +1 ])

                                                    #print(registerInstruction)
                                                    updataVector(registerInstruction)
                                                    if ischange == 1:
                                                        break
                                                elif lineNum + k < ContextLen and ',' not in fileContext[lineNum + k]:
                                                    regexregister = '\[.*' + TempRegister + '.*\]'
                                                    regexOnlyregister = '\[' + TempRegister + '\]'
                                                    if re.search(regexOnlyregister,fileContext[lineNum + k]):
                                                        updataVector('[address]')
                                                    elif re.search(regexregister,fileContext[lineNum + k]):
                                                        updataVector('[address]')
                                                        updataVector('[?+address+?]')

                                                elif lineNum + k < ContextLen and 'push' in fileContext[lineNum + k]:
                                                    matPushReg = re.search('push[ \t]+(\w+)',fileContext[lineNum + k])
                                                    if matPushReg:
                                                        if matPushReg.groups()[0] == TempRegister:
                                                            fileContext[lineNum + k] = fileContext[lineNum + k].replace(TempRegister,'[ebp+' + each_var['varName'] + ']')
                                                            break

                                                elif lineNum + k < ContextLen and 'call' in fileContext[lineNum + k]:
                                                    matCallReg = re.search('call[ \t]+(\w+)',fileContext[lineNum + k])
                                                    if matCallReg:
                                                        if matCallReg.groups()[0] == TempRegister:
                                                            updataVector('FPptr')
                                                            updataVector('FPFunc')
                                                            break

                                                # 如果下一行找到了temp寄存器，那就要跳出
                                                if TempRegister in fileContext[lineNum + k] or 'call' in fileContext[lineNum + k] or 'loc' in fileContext[lineNum + k] or re.search('^j.+', instructHead):
                                                    break

                                        except:
                                            pass
                                        """
                                    #上面考虑到mov reg的特殊情况，把reg替换成变量继续往下找
                                     """

                                    #判断左边是不是128位寄存器
                                    elif left.find('xmm')!=-1:
                                        instructionIR=head+' xmm _'
                                    elif head=='cmp':
                                        instructionIR='cmp '+left
                                    #剩下的一般都是32位寄存器，不是的话也这样处理
                                    else:
                                        instructionIR=head+' '+left+' _'
                                else:
                                    print("File2Vector Error:cannot find '_'")

                            ##print(instructionIR)

                            updataVector(instructionIR)

                    #dword,word,byte这些信息直接给一个较大的值，比如75
                    if issearchwordptr == 0:
                        count=0
                        for each_instruction in self.Instructions_list:
                            if each_instruction==each_var['byteNum']:
                                Vector_list_element[count]=75
                                break
                            count+=1

                    #下面这个for语句中的代码把相应的标签增加到self.Label_list中，同时把前面的结果追加到self.Vector_list中
                    for each_function in var_orgrin_type:
                        if each_function['functionName']==functionName:
                            isInsert=0#插入成功后置1,没插入成功的话可能是多余的变量，但为了update，要先做个标记
                            #print(each_function['varType'])
                            for each in each_function['varType']:
                                sign=0#为了防止找到重复的类型，找到就跳出，例如int a和float a，已先找到的为主
                                typeDeclar = 'UK'
                                regex = "[ a-zA-Z*]+[ \t]+"+'(.+,)*'+'\*?'+each_var['varName']+"(\[\])?"+"([^0-9a-zA-Z_].*;\Z|;\Z)"
                                if re.match(regex, each):
                                    left, right = each.strip().split(' ', 1)
                                    if left=='signed' or left=='unsigned' or left=='static' or left=='extern' or left=='const':
                                        try:
                                            left, right = right.strip().split(' ', 1)
                                        except:
                                            pass

                                    #对long long double这些近些过滤
                                    if left=='long' and 'int' in right:
                                        left='int'
                                    elif 'double' in right:
                                        left='double'
                                    elif 'float' in right:
                                        left='float'
                                    elif 'char' in right:
                                        left='char'
                                    elif left=='long':
                                        left = 'int'

                                    # 检查是否是指针类型和数组
                                    regexArray = "[ a-zA-Z]+[ \t]+" + '(.+,)*' + each_var['varName'] + "\[\]"+"([^0-9a-zA-Z_].*;\Z|;\Z)"
                                    regexPoint1 = "[ a-zA-Z]+[ \t]+"+'(.+,)*'+'\*'+each_var['varName']+"(\[\])?"+"([^0-9a-zA-Z_].*;\Z|;\Z)"
                                    regexPoint2 = "[ a-zA-Z]+\*[ \t]+"+'(.+,)*'+each_var['varName']+"(\[\])?"+"([^0-9a-zA-Z_].*;\Z|;\Z)"
                                    regexNormal = "[ a-zA-Z]+[ \t]+"+'(.+,)*'+ each_var['varName']+"([^0-9a-zA-Z_].*;\Z|;\Z)"
                                    if re.match(regexArray, each):
                                        typeDeclar = left#+'[]'
                                    elif re.match(regexPoint1, each):
                                        #typeDeclar = left + '*'
                                        typeDeclar='ptr'
                                    elif re.match(regexPoint2, each):
                                        #typeDeclar = left
                                        typeDeclar = 'ptr'
                                    elif re.match(regexNormal, each):
                                        typeDeclar = left
                                    else:
                                        typeDeclar = 'UK'

                                    if typeDeclar=='Boolean':
                                        typeDeclar='bool'
                                    #print(typeDeclar)
                                
                                    #在类型字典中查找，得到标签
                                    index=0
                                    for ea in self.Type_list:
                                        if ea==typeDeclar:
                                            #如果向量为0向量，那么去掉该向量
                                            flag=0
                                            CountNotZero=0
                                            for i in range(0, len(Vector_list_element)):
                                                if Vector_list_element[i] != 0:
                                                    CountNotZero += 1
                                                    continue
                                                if CountNotZero >= 2:
                                                    flag = 1
                                                    break
                                            """
                                            for each_is_zero in Vector_list_element:
                                                if not each_is_zero==0:
                                                    CountNotZero+=1
                                                    continue
                                                if CountNotZero>=2:
                                                    flag=1
                                                    break"""
                                            #不是0向量的是有效结果
                                            if flag==1:
                                                #print(Vector_list_element)
                                                #把这个结果追加到self.Vector_list中
                                                self.Vector_list.append(Vector_list_element)
                                                #把相应的标签增加到self.Label_list中
                                                self.Label_list.append(index)
                                                #把相应的函数及其变量名增加到self.Name_list_list中
                                                self.Name_list.append(functionName+':'+each_var['varName'])
                                                sign=1#用于跳出两层循环
                                                isInsert=1#插入成功
                                                break
                                        elif ea=='#':
                                            break
                                        else:
                                            index=index+1
                                    if sign==1:
                                        break
                                else:
                                    pass
                            if isInsert==0:#没有插入成功
                                self.Vector_list.append(Vector_list_element)
                                self.Label_list.append(-1)
                                self.Name_list.append(functionName + ':' + each_var['varName'])

        except IOError as err:
            print('File error:'+ str(err))

        # 先整理一下向量，最大值不超过10,并且有mov imm就不要mov bool了
        for each in self.Vector_list:
            for i in range(7, len(each)):
                if each[i] > 10:
                    each[i] = 10
                if self.Instructions_list[i] == 'mov _ imm' and each[i] > 0:
                    if each[i-1] == each[i]:
                        each[i] =0
                    elif each[i-1] < each[i]:
                        each[i-1] = 0
                if self.Instructions_list[i] == 'cmp _ imm' and each[i] > 0:
                    if each[i-1] == each[i]:
                        each[i] =0
                    elif each[i-1] < each[i]:
                        each[i-1] = 0

    def updateVector(self,Name,Key,weight,change=0):
        #print('\n___start update:')
        for each_name,each_vector in zip(self.Name_list,self.Vector_list):
            if each_name == Name:
                #print(Name)
                #print(each_vector)
                for i in range(0,len(self.Instructions_list)):
                    if self.Instructions_list[i] == Key:
                        if change==0:
                            each_vector[i] += weight
                        elif change==1:
                            each_vector[i] = weight

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class OnlyFileToVector:
    def __init__(self, Type_List_file, Instructions_List_file):
        self.Type_list = File2List(Type_List_file)
        self.Instructions_list = File2List(Instructions_List_file)
        self.Name_list = []
        self.Label_list = []
        self.Vector_list = []
        self.UDrelation = []
        self.UDWeakrelation = []
        self.LEArelation = []
        self.Offset_list = []
        #新的指向信息
        self.pointer_name_list = []
        self.pointer_label_list = []
        self.pointer_vector_list =[]
        self.function_parameter_list = self.function_parameter_list = CallingFile2ParaList('SaveData/Normalization/FuncPara_List.txt')
        self.FP_Pointer_rel = []
        #保存函数的参数信息
        self.FuncAndPara = []
        #保存函数的调用时，参数与变量之间的关系
        self.CallParaSet = set()

        self.PredictResult = []  # 用来存放预测的变量信息
        self.PointerResult = []  # 用来存放二次预测的指针指向的变量的信息

        self.globalVarNameSet = set()
        self.globalVarName = []
        self.globalVarLabel = []
        self.globalVarVector = []

    def UpdateUDrelation(self):
        if self.UDrelation != []:
            for each in self.UDrelation:
                left,right=each.split('---')
                #print(left,end='---')
                #print(right)
                if ':ds:' in left or ':ds:' in right:
                    break
                f=0
                s=0
                flagFS = 0
                for i in range(0,len(self.Name_list)):
                    for j in range(0,len(self.Name_list)):
                        if left==self.Name_list[i] and right==self.Name_list[j]:
                            f=i
                            s=j
                            flagFS = 1
                            break
                    if flagFS == 1:
                        break
                VectorAddVector(self.Vector_list[f],self.Vector_list[s])
        if self.UDWeakrelation != []:
            for each in self.UDWeakrelation:
                left, right = each.split('---')
                # print(left,end='---')
                # print(right)
                f = 0
                s = 0
                flagFS = 0
                for i in range(0, len(self.Name_list)):
                    for j in range(0, len(self.Name_list)):
                        if left == self.Name_list[i] and right == self.Name_list[j]:
                            f = i
                            s = j
                            flagFS = 1
                            break
                    if flagFS == 1:
                        break
                VectorReplaceVector(self.Vector_list[s], self.Vector_list[f])

    # 函数File2Vector将一个汇编代码文件中的每个变量用一个向量的形式表示
    # 该函数的第一个参数为汇编代码文件的地址
    def File2Vector(self, filename):
        indirctVar = []
        variables = []  # 用于保存各个变量的信息的列表，列表中的元素是字典
        newPointerList = []  # 新预测的指针
        globalVar = []

        try:  # 打开汇编代码文件
            with open(filename,encoding='utf-8') as assemblyfile:

                flagg = 0  # 0表示还没找到函数名，1表示找到函数名
                functionName = ''
                for line in assemblyfile.readlines():
                    line = line.replace("\t","\t ")
                    #得到函数名functionName
                    if flagg==0:
                        if re.search(".*__cdecl [a-zA-Z_]([a-zA-Z_]|[0-9])*(.*(,.+)*)",line):
                            functionReType,rest=line.strip().split('__cdecl',1)
                            functionName,parameterList=rest.strip().split('(',1)
                            functionName=functionName.strip()
                            flagg = 1
                        else:
                            if re.search('proc near',line):
                                functionReType, rest = line.strip().split('proc near', 1)
                                functionName = functionReType.strip()

                                if re.search('\??.+@@',functionName):
                                    pattern = re.compile("\??(.+)@@")
                                    res = pattern.search(functionName).groups()
                                    functionName=res[0].strip()
                                elif re.search('\?.+@@',functionName):
                                    pattern = re.compile("\?(.+)@@")
                                    res = pattern.search(functionName).groups()
                                    functionName=res[0].strip()
                                elif re.search('.+@@',functionName):
                                    pattern = re.compile("(.+)@@")
                                    res = pattern.search(functionName).groups()
                                    functionName=res[0].strip()
                                elif re.search('_Z[0-9](.+)P.+',functionName):
                                    pattern = re.compile("_Z[0-9](.+)P.+")
                                    res = pattern.search(functionName).groups()
                                    functionName=res[0].strip()
                                elif functionName[0] == '_':
                                    functionName = functionName[1:]
                                flagg = 1
                        #print(functionName)

                    # 将汇编代码中的局部变量找出，并将其基本信息用一个字典的结构保存，结果追加到variables列表中
                    if re.search("[a-zA-Z_]([a-zA-Z_]|[0-9])*[ \t]*=[ \t]*.+ptr.+", line):
                        varName, rest = line.strip().split('=', 1)
                        byteNum, offset = rest.strip().split('ptr', 1)
                        if functionName == 'main' or functionName == '_tmain':  # 剔除掉main函数的三个参数
                            if varName.strip() == 'argc' or varName.strip() == 'argv' or varName.strip() == 'envp':
                                continue
                        variables.append({'varName': varName.strip(), 'byteNum': byteNum.strip(), 'offset': offset.strip()})
                    #IDA提供的变量已经全部记录

                    for each_var in variables:
                        regex1 = '\[(ebp|rbp)([\+|-].+)+[\+|-]' + each_var['varName'] + '([\+|-][0-9][0-9a-fA-F]*h?)*\]'
                        regex2 = '\[(ebp|rbp)([\+|-].+)*[\+|-]' + each_var['varName'] + '([\+|-][0-9][0-9a-fA-F]*h?)+\]'
                        if re.search(regex1, line) or re.search(regex2, line):
                            try:
                                head, rest = line.strip().split(' ', 1)
                                newvar, rest = rest.strip().split(',', 1)
                                if '+' + each_var['varName'] in newvar:
                                    pass
                                else:
                                    newvar=rest.strip()
                                newvar = newvar.replace('[ebp+','')
                                newvar = newvar.replace('[rbp+','')
                                newvar = newvar.replace(']', '')
                                newvar = newvar.replace('dword ptr','')
                                newvar = newvar.replace('qword ptr', '')
                                newvar = newvar.replace('word ptr', '')
                                newvar = newvar.replace('byte ptr', '')
                                newvar = newvar.strip()
                                newvaroffset, subn_num = re.subn("(?:rax|rbx|rcx|rdx|rsi|rdi)(?!\w)", "?", newvar)
                                newvaroffset, subn_num = re.subn("(?:eax|ebx|ecx|edx|esi|edi)(?!\w)", "?", newvaroffset)
                                newvaroffset = newvaroffset.replace(each_var['varName'],each_var['offset'])

                                newvar, subn_num = re.subn("(?:rax|rbx|rcx|rdx|rsi|rdi)(?!\w)", "rregg", newvar)
                                newvar, subn_num = re.subn("(?:eax|ebx|ecx|edx|esi|edi)(?!\w)", "reg", newvar)
                                newvar, subn_num = re.subn("(?:ax|bx|cx|dx|si|di)(?!\w)", "ax", newvar)
                                newvar, subn_num = re.subn("(?:al|bl|cl|dl|ah|bh|ch|dh)(?!\w)", "al", newvar)

                                #如果表中没有就插入
                                flag=0
                                for each in indirctVar:
                                    if each['newvarName']==newvar:
                                        flag=1
                                        break
                                if flag==0:
                                    indirctVar.insert(0,{'varName': each_var['varName'], 'byteNum': each_var['byteNum'], 'offset': newvaroffset, 'newvarName': newvar })
                            except:
                                pass

                    #发现全局变量
                    globalSearch = re.search("([dq]?word_\w+|byte_\w+|\?\w+@@[\w@]+|ds:[\w@]+)", line)
                    if globalSearch:
                        self.globalVarNameSet.add(globalSearch.group())
                        byteNum='dword'
                        if re.search("([dq]?word_\w+|byte_\w+)", globalSearch.group()):
                            byteNum, rest = globalSearch.group().split('_',1)
                            globalVar.append({'varName': globalSearch.group(), 'byteNum': byteNum, 'offset': 'global'})
                        elif re.search("(\?\w+@@[\w@]+)", line):
                            typeNote = re.search(";[ \t]*(int|float|double)" , line)
                            if typeNote:
                                if typeNote.groups()[0] == 'int' or typeNote.groups()[0] == 'float' or '*' in typeNote.groups()[0]:
                                    byteNum = 'dword'
                                elif typeNote.groups()[0] == 'bool' or typeNote.groups()[0] == 'char':
                                    byteNum = 'byte'
                                elif typeNote.groups()[0] == 'double' or ('long' in typeNote.groups()[0] and 'int' in typeNote.groups()[0]):
                                    byteNum = 'qword'
                                elif 'short' in typeNote.groups()[0]:
                                    byteNum = 'word'
                            globalVar.append({'varName': globalSearch.group(), 'byteNum': byteNum, 'offset': 'global'})
                        elif 'ds:' in globalSearch.group():
                            if 'dword' in line:
                                byteNum = 'dword'
                            elif 'qword' in line:
                                byteNum = 'dword'
                            elif 'word' in line:
                                byteNum = 'word'
                            elif 'byte' in line:
                                byteNum = 'byte'
                            elif 'xmm' in line:
                                byteNum = 'qword'
                            else:
                                byteNum = 'dword'
                            globalVar.append({'varName': globalSearch.group(), 'byteNum': byteNum, 'offset': 'global'})

                #print(globalVar)

                for each in globalVar:
                    variables.append(each)

                #函数的参数信息用于后期把各个函数联系起来
                i = 1
                for each in variables:
                    if '-' not in each['offset']:
                        self.FuncAndPara.append({'Name':functionName + ':' + each['varName'] ,
                                                 'offset': each['offset'] ,
                                                 'ParaNum': functionName + 'P' + str(i)
                                                 })
                        i = i + 1

                #因为longlongint和double有可能会出现qword 和 +4 偏移量，此处再做一个检查
                #列表的删除需要倒序循环，不然删除元素后len不变，而且i变，各种问题
                for i in range(len(indirctVar)-1,-1,-1):
                    if indirctVar[i]['byteNum']=='qword' and  indirctVar[i]['varName'] + '+4' in indirctVar[i]['newvarName']:
                        indirctVar.remove(indirctVar[i])

                # print(self.FuncAndPara)
                # print(indirctVar)
                # print(variables)

                #把变量加偏移量的变量也整合进去
                for eachindirctVar in indirctVar:
                    for i in range(0, len(variables)):
                        if eachindirctVar['varName'] == variables[i]['varName']:
                            # 下面代码的作用是为了美观考虑，+号两边换位
                            indirctVarOffset=eachindirctVar['offset']
                            if '?' in indirctVarOffset and '+' in eachindirctVar['offset']:
                                #美观考虑，+号两边换位
                                left, right = eachindirctVar['offset'].strip().split('+', 1)
                                indirctVarOffset=right.strip() + '+' + left.strip()
                                #print(indirctVarOffset)
                            variables.insert(i+1,{'varName': eachindirctVar['newvarName'], 'byteNum': eachindirctVar['byteNum'], 'offset': indirctVarOffset})

                # print(variables)


                assemblyfile.seek(0)  # 使用seek()方法返回到文件起始位置
                fileContext = assemblyfile.readlines()#把文档内容存起来先
                assemblyfile.seek(0)
                ContextLen = len(fileContext)

                # 下面这个for循环将每个变量相关的语句找出
                for each_var in variables:
                    Vector_list_element = []  # Vector_list的组成元素,初始化为全0
                    for i in range(len(self.Instructions_list)):
                        Vector_list_element.append(0)

                    # 定义一个下面经常用的函数
                    # 在指令字典中查找，如果有的话就在相应的向量位置上+1
                    def updataVector(IR):
                        # 在指令字典中查找，如果有的话就在相应的向量位置上+1
                        count = 0
                        for each_instruction in self.Instructions_list:
                            if each_instruction == IR:
                                # 人为按情况调整权重
                                if IR == 'mov _ bool':
                                    Vector_list_element[count + 1] += 1  # 0和1同时也算立即数
                                if IR == 'cmp _ bool':
                                    Vector_list_element[count + 1] += 1  # 0和1同时也算立即数
                                if 'FP' in IR:
                                    Vector_list_element[count] += 2
                                    if 'FPptr' in IR:
                                        Vector_list_element[count] += 8
                                if 'address' in IR:
                                    # print(IR)
                                    Vector_list_element[count] = 25
                                    break
                                Vector_list_element[count] += 1
                                break
                            elif each_instruction == '#':
                                if not IR == 'UK' and IR!='not _' and IR!='push':
                                    #print(IR ,end=' \tmissing\n')  # 总集里没有的指令输出看看
                                    pass
                                break
                            count += 1

                    #print(each_var)
                    issearchwordptr = 0

                    for lineNum in range(0, ContextLen):
                        #有些文本不适应，后面要按照空格分割，先把\t 全换成空格
                        fileContext[lineNum] = fileContext[lineNum].replace('\t',' \t')
                        #全局变量改ebp格式
                        for eachgv in self.globalVarNameSet:
                            if eachgv in fileContext[lineNum] and 'ebp+'+eachgv not in fileContext[lineNum]:
                                fileContext[lineNum] = fileContext[lineNum].replace(eachgv, '[ebp+'+ eachgv +']')
                                #print(fileContext[lineNum])

                        """
                        # 查找有没有[ebp+...+varname+...]的形式
                        regex1 = '\[(ebp|rbp)(\[\+|-].+)+[\+|-]' + each_var['varName'] + '([\+|-][0-9][0-9a-fA-F]*h?)*\]'
                        regex2 = '\[(ebp|rbp)(\[\+|-].+)*[\+|-]' + each_var['varName'] + '([\+|-][0-9][0-9a-fA-F]*h?)+\]'
                        if re.search(regex1, fileContext[lineNum]) or re.search(regex2, fileContext[lineNum]):
                            count = 0
                            for each_instruction in self.Instructions_list:
                                if each_instruction == 'bias in stackframe':
                                    Vector_list_element[count] = 25
                                    break
                                count += 1
                                """
                        # 查找[ebp+...+varname+...]的相关语句
                        varNameinregex = each_var['varName'].replace('rregg', '(rax|rbx|rcx|rdx)')
                        varNameinregex = varNameinregex.replace('reg', '(eax|ebx|ecx|edx)')
                        varNameinregex = varNameinregex.replace('al', '(al|bl|cl|dl|)')
                        varNameinregex = varNameinregex.replace('ax', '(ax|bx|cx|dx|)')

                        #只有qword才能把+4偏移量放一起,例外
                        if each_var['byteNum'] == 'qword':
                            varNameinregex = '('+ varNameinregex + '|' + varNameinregex + '+4)'
                            #print(varNameinregex)
                        if '?' in varNameinregex:
                            varNameinregex = varNameinregex.replace('?','\?')

                        regex = '\[(ebp|rbp)\+(.*\+)?' + varNameinregex.replace('+','\+') + '\]'

                        if re.search(regex, fileContext[lineNum]):
                            #首先对于结构体中第一个变量不管它，带偏移量的以实际指令中的ptr为主
                            #对于既不是dword，又不是qword和word的，但是不考虑byte，因为无debuginfo时IDA强行认为结构就是byte
                            if (each_var['byteNum'] != 'word' and each_var['byteNum'] != 'dword' and each_var['byteNum'] != 'qword') or re.search('\+\d+',each_var['varName']):
                                if issearchwordptr == 0 and re.search('[Pp][Tt][Rr][ ]*\[(ebp|rbp)\+' + varNameinregex.replace('+','\+') , fileContext[lineNum]):
                                    issearchwordptr = 1
                                    if 'qword ptr' in fileContext[lineNum] or 'QWORD PTR' in fileContext[lineNum]:
                                        count = 0
                                        for each_instruction in self.Instructions_list:
                                            if each_instruction == 'qword':
                                                Vector_list_element[count] = 75
                                                break
                                            count += 1
                                    elif 'dword ptr' in fileContext[lineNum] or 'DWORD PTR' in fileContext[lineNum]:
                                        count = 0
                                        for each_instruction in self.Instructions_list:
                                            if each_instruction == 'dword':
                                                Vector_list_element[count] = 75
                                                break
                                            count += 1
                                    elif 'word ptr' in fileContext[lineNum] or 'WORD PTR' in fileContext[lineNum]:
                                        count = 0
                                        for each_instruction in self.Instructions_list:
                                            if each_instruction == 'word':
                                                Vector_list_element[count] = 75
                                                break
                                            count += 1
                                    elif 'byte ptr' in fileContext[lineNum] or 'BYTE PTR' in fileContext[lineNum]:
                                        count = 0
                                        for each_instruction in self.Instructions_list:
                                            if each_instruction == 'byte':
                                                Vector_list_element[count] = 75
                                                break
                                            count += 1

                            head, rest = fileContext[lineNum].strip().split(' ', 1)
                            head = head.strip()

                            # 用字符串来将各个指令化成统一的代表形式，即指令全集中的表示
                            instructionIR='UK'
                            # 没有逗号的就是一元指令
                            if not ',' in fileContext[lineNum]:
                                #关于push找call
                                if head == 'push':
                                    funcPara='..'
                                    Pi = 1
                                    for j in range(1, 15):
                                        if lineNum+j >= ContextLen:
                                            break
                                        regexCall = 'call[ \t]*(\w+)$'
                                        matCall= re.search(regexCall ,fileContext[lineNum+j])
                                        if matCall:
                                            funcPara = matCall.groups()[0]+'P'+str(Pi)
                                            self.CallParaSet.add(functionName+":"+ each_var['varName'] + '---' + funcPara)
                                            break
                                        elif 'push' in fileContext[lineNum + j]:
                                            if re.search('\[ebp\+\w+\+4\]',fileContext[lineNum + j]) and re.search('\[ebp\+\w+\]',fileContext[lineNum+j+1]):
                                                continue
                                            else:
                                                Pi = Pi + 1

                                    if funcPara!='..':
                                        for each in self.function_parameter_list:
                                            if funcPara==each['funcPara'] or funcPara=='_'+each['funcPara']:
                                                if '*' in each['paraType']:
                                                    if each_var['byteNum'] == 'dword':
                                                        updataVector('FPptr')
                                                        self.FP_Pointer_rel.append(functionName+':'+each_var['varName'] + '---' + each['paraType'])
                                                        if '*' == each['paraType']:
                                                            break
                                                        updataVector('FP' + re.sub('[^_a-zA-Z0-9]','',each['paraType']))
                                                else:
                                                    if each_var['byteNum'] == 'byte' and (each['paraType'] =='int' or '*' in each['paraType']):
                                                            break
                                                    else:
                                                        updataVector('FP' + re.sub('[^_a-zA-Z0-9]','',each['paraType']))
                                                # print(each_var['varName'],end='--')
                                                # print(each['paraType'])
                                                break

                                # 对于某些一元指令，这里只考虑div、idiv、fstp、fld
                                elif head == 'div':
                                    instructionIR = 'div _'
                                elif head == 'idiv':
                                    instructionIR = 'idiv _'
                                elif head == 'fstp':
                                    instructionIR = 'fstp _'
                                elif head == 'fld':
                                    instructionIR = 'fld _'
                                elif 'FP' in head:
                                    instructionIR = head
                                else:
                                    instructionIR = head + ' _'

                            # 有逗号的就是二元指令
                            else:
                                rest, subn_num = re.subn("\[.+\]", "_", rest)
                                rest, subn_num = re.subn("xmm[0-7]", "xmm", rest)
                                rest, subn_num = re.subn("(?:rax|rbx|rcx|rdx|rsi|rdi)(?!\w)", "rregg", rest)
                                rest, subn_num = re.subn("(?:eax|ebx|ecx|edx|esi|edi)(?!\w)", "reg", rest)
                                rest, subn_num = re.subn("(?:ax|bx|cx|dx|si|di)(?!\w)", "ax", rest)
                                rest, subn_num = re.subn("(?:al|bl|cl|dl|ah|bh|ch|dh)(?!\w)", "al", rest)

                                if ',' not in rest:
                                    continue

                                left, right = rest.strip().split(',', 1)
                                right = right.strip()
                                left = left.strip()

                                #去;符号
                                if ';' in right:
                                    right, rightrest = right.strip().split(';', 1)
                                    right = right.strip()

                                # head中有cvtt和cvt时，删掉2后面的。例如cvttsd2ss改写成cvtsd
                                if 'cvt' in head:
                                    if 'cvtt' in head:
                                        head = head.replace('cvtt', 'cvt')
                                    head = head[0:5]
                                    instructionIR = head
                                # 实际上lea没什么意义，关键是lea到寄存器后，寄存器中数据的走向，下一个变量往上回朔时反而加上lea更靠谱
                                elif 'lea' in head:
                                    #找出变量间指针的指向关系
                                    try:
                                        head, rest = fileContext[lineNum].strip().split(' ', 1)
                                        left, right = rest.strip().split(',', 1)
                                        tempregister = left.strip()#lea那一行的寄存器
                                        head, rest = fileContext[lineNum+1].strip().split(' ', 1)
                                        left, right = rest.strip().split(',', 1)
                                        nextregister = right.strip()#lea后面一行的寄存器
                                        if head=='mov' and tempregister==nextregister:
                                            if '[ebp+' in left or '[rbp+' in left:
                                                regexVar = '\[(ebp|rbp)\+.+\]'
                                                matchName = re.search(regexVar, left)
                                                left = matchName.group()
                                                next_var = left.replace('[ebp+','')
                                                next_var = next_var.replace('[rbp+','')
                                                next_var = next_var.replace(']', '')
                                                if not '+' in next_var:
                                                    self.LEArelation.append(functionName+':'+next_var + ' -> '+functionName+':'+each_var['varName'])
                                                    #print(next_var + ' -> '+each_var['varName'])
                                    except:
                                        pass
                                # 判断下划线在左边还是右边
                                # 如果下划线在左边
                                elif '_' in left.strip():
                                    # 先看mov _0/1这种明显特征，不是0/1统一转成imm
                                    if (right.strip() == '0' or right.strip() == '1') and (head=='mov' or head== 'cmp'):
                                        instructionIR = head + ' _ bool'

                                    else:
                                        right, subn_num = re.subn("(0x)?[0-9][0-9a-fA-F]*h?(?!\w)", "imm", right)  # 不是单独的0或1 都看成是立即数
                                        # 首先检查逗号右边是不是offset和立即数
                                        if right.find('offset') != -1:
                                            instructionIR = head + ' _ offset'
                                        elif right.find('imm') != -1:
                                            instructionIR = head + ' _ ' + "imm"
                                        # 不是offset和立即数的情况一般就是mov了
                                        # mov的情况特殊处理,变量在左边和右边的情况视为相同
                                        elif not head.find('mo') == -1:
                                            instructionIR = head + ' ' + right
                                            """
                                        #下面考虑到mov reg的特殊情况，把reg替换成变量返回往上找
                                        """
                                            # 考虑到mov reg的特殊情况，把reg替换成变量返回往上找
                                            # 此处千万别改动instructionIR
                                            instructHead, instructRest = fileContext[lineNum].strip().split(' ', 1)
                                            instructLeft, instructRight = instructRest.strip().split(',', 1)
                                            # 准确提取到底是哪个寄存器，后面有用
                                            TempRegister = instructRight.strip()

                                            registerInstruction = 'UK'  # 作用类似instructionIR
                                            try:
                                                for k in range(1,6):
                                                    fileContext[lineNum - k] = fileContext[lineNum - k].replace('\t',' \t')
                                                    if lineNum - k > 0 and ','in fileContext[lineNum - k]:
                                                        # print(fileContext[lineNum - k],end='')
                                                        # print(fileContext[lineNum])
                                                        instructHead, instructRest = fileContext[lineNum - k].strip().split(' ', 1)
                                                        instructLeft, instructRight = instructRest.strip().split(',', 1)
                                                        instructRight = instructRight.strip()
                                                        instructLeft = instructLeft.strip()
                                                        if TempRegister in instructLeft:  # 如果出现在左边
                                                            # 那么看下有没有取值的行为
                                                            if instructLeft == TempRegister:
                                                                instructLeft, subn_num = re.subn("xmm[0-7]", "xmm",instructLeft)
                                                                instructLeft, subn_num = re.subn("(?:rax|rbx|rcx|rdx|rsi|rdi)(?!\w)", "rregg",instructLeft)
                                                                instructLeft, subn_num = re.subn("(?:eax|ebx|ecx|edx|esi|edi)(?!\w)", "reg",instructLeft)
                                                                instructLeft, subn_num = re.subn("(?:ax|bx|cx|dx|si|di)(?!\w)", "ax", instructLeft)
                                                                instructLeft, subn_num = re.subn("(?:al|bl|cl|dl|ah|bh|ch|dh)(?!\w)", "al",instructLeft)
                                                                # 因为这里是寄存器代替_，与变量不同。这里的和处理就是换位置，比如add _ reg换位成add reg _
                                                                if 'cvt' in instructHead:
                                                                    if 'cvtt' in instructHead:
                                                                        instructHead=instructHead.replace('cvtt','cvt')
                                                                    instructHead='cvt'+instructHead[6:8]
                                                                    registerInstruction=instructHead
                                                                elif instructHead == 'cmp':
                                                                    registerInstruction = 'cmp ' + instructLeft
                                                                elif 'mo' in instructHead:
                                                                    registerInstruction = instructHead + ' ' + instructLeft
                                                                else:
                                                                    registerInstruction = instructHead + ' ' + instructLeft + ' _'
                                                            elif re.search(regexregister, instructLeft):
                                                                if 'ebp' not in instructLeft and 'rbp' not in instructLeft:  # 有ebp的话就跟你无关了
                                                                    if re.search(regexOnlyregister, instructLeft):
                                                                        registerInstruction = '[address]'
                                                                    else:
                                                                        updataVector('[address]')
                                                                        registerInstruction = '[?+address+?]'
                                                                    newPointerList.append({'PointName': each_var['varName'],
                                                                                            'head': instructHead,
                                                                                            'TempTegister': TempRegister,
                                                                                            'InstructionNear': instructRight,
                                                                                            'keyInstruction': instructLeft.replace(TempRegister, each_var['varName']),
                                                                                            'PointNameOrigin': each_var['varName']})

                                                        elif TempRegister in instructRight:  # 如果出现在右边
                                                            if instructRight == TempRegister:
                                                                instructRight, subn_num = re.subn("xmm[0-7]", "xmm",instructRight)
                                                                instructRight, subn_num = re.subn("(?:rax|rbx|rcx|rdx|rsi|rdi)(?!\w)", "rregg",instructRight)
                                                                instructRight, subn_num = re.subn("(?:eax|ebx|ecx|edx|esi|edi)(?!\w)", "reg",instructRight)
                                                                instructRight, subn_num = re.subn("(?:ax|bx|cx|dx|si|di)(?!\w)", "ax", instructRight)
                                                                instructRight, subn_num = re.subn("(?:al|bl|cl|dl|ah|bh|ch|dh)(?!\w)", "al",instructRight)
                                                                if instructHead == 'cmp':  # mov的情况已经没有，但还有cmp
                                                                    registerInstruction = 'cmp ' + instructRight
                                                                elif 'mo' in instructHead:
                                                                    registerInstruction = instructHead + ' ' + instructRight
                                                                else:
                                                                    registerInstruction = instructHead + ' ' + instructRight + ' _'
                                                            elif re.search(regexregister, instructRight):
                                                                if 'ebp' not in instructRight and 'rbp' not in instructRight:  # 有ebp的话就跟你无关了
                                                                    if re.search(regexOnlyregister, instructRight):
                                                                        registerInstruction = '[address]'
                                                                    else:
                                                                        updataVector('[address]')
                                                                        registerInstruction = '[?+address+?]'
                                                                    newPointerList.append({'PointName': each_var['varName'],
                                                                                            'head': instructHead,
                                                                                            'TempTegister': TempRegister,
                                                                                           'InstructionNear': instructLeft,
                                                                                            'keyInstruction': instructRight.replace(TempRegister, each_var['varName']),
                                                                                            'PointNameOrigin': each_var['varName']})

                                                        updataVector(registerInstruction)

                                                    elif lineNum - k > 0 and 'call' in fileContext[lineNum - k]:
                                                        regexCall = 'call[ \t]*(\w+)$'
                                                        matCall = re.search(regexCall , fileContext[lineNum - k])
                                                        if matCall:
                                                            funcRe = matCall.groups()[0]+'Re'
                                                            for each in self.function_parameter_list:
                                                                if funcRe==each['funcPara'] or funcRe=='_'+each['funcPara']:
                                                                    if  '*' in each['paraType']:
                                                                        updataVector('FPptr')
                                                                        self.FP_Pointer_rel.append(functionName+':'+each_var['varName'] + '---' + each['paraType'])
                                                                        if '*' == each['paraType']:
                                                                            break
                                                                    updataVector('FP' + re.sub('[^a-zA-Z]','',each['paraType']))
                                                                    break

                                                    #如果上一行找到了temp寄存器，那就要跳出
                                                    if TempRegister in fileContext[lineNum - k] or 'call' in fileContext[lineNum - k] or 'loc' in fileContext[lineNum - k] or re.search('^j.+', instructHead):
                                                        break

                                            except:
                                                pass

                                            """
                                       #下面考虑到mov reg的特殊情况，把reg替换成变量返回往上找
                                       """
                                        elif head == 'cmp':
                                            instructionIR = 'cmp ' + right
                                        else:
                                            instructionIR = head + ' _ ' + right
                                # 如果下划线在右边
                                elif '_' in right.strip():
                                    # mov的情况特殊处理,变量在左边和右边的情况视为相同
                                    if not head.find('mo') == -1:
                                        instructionIR = head + ' ' + left
                                        """
                                    #下面考虑到mov reg的特殊情况，把reg替换成变量继续往下找
                                    """
                                        # 考虑到mov reg的特殊情况，把reg替换成变量继续往下找
                                        # 此处千万别改动instructionIR
                                        instructHead, instructRest = fileContext[lineNum].strip().split(' ', 1)
                                        instructLeft, instructRight = instructRest.strip().split(',', 1)
                                        # 准确提取到底是哪个寄存器，后面有用
                                        TempRegister = instructLeft.strip()
                                        TempVar = instructRight.strip()
                                        TempHead = instructHead.strip()

                                        registerInstruction = 'UK'  # 作用类似instructionIR
                                        try:
                                            for k in range(1, 6):
                                                fileContext[lineNum + k] = fileContext[lineNum + k].replace('\t', ' \t')
                                                ischange = 0
                                                if lineNum + k < ContextLen and ',' in fileContext[lineNum + k]:
                                                    instructHead, instructRest = fileContext[lineNum + k].strip().split(' ', 1)
                                                    instructLeft, instructRight = instructRest.strip().split(',', 1)
                                                    instructRight = instructRight.strip()
                                                    instructLeft = instructLeft.strip()
                                                    regexregister = '\[.*' + TempRegister + '.*\]'
                                                    regexOnlyregister = '\[' + TempRegister + '\]'

                                                    if instructRight in child(TempRegister) and 'arg' in each_var['varName']:
                                                        if instructHead == TempHead and instructLeft != TempVar:
                                                            matvarnameUp = re.search('\[(ebp|rbp)\+(.+)\]', TempVar)
                                                            matvarnameDown = re.search('\[(ebp|rbp)\+(.+)\]',instructLeft)
                                                            if matvarnameUp and matvarnameDown:
                                                                VarDown = matvarnameDown.groups()[1]
                                                                VarUp = matvarnameUp.groups()[1]
                                                                if not '+' in VarUp and not '+' in VarDown:
                                                                    self.UDWeakrelation.append(functionName + ':' + VarUp + '---' + functionName + ':' + VarDown)
                                                                    #print(functionName + ':' + VarUp + '---' + functionName + ':' + VarDown)

                                                    if TempRegister in instructLeft:  # 如果出现在左边，并且被mo说明已经被改
                                                        # 那么看下有没有取值的行为
                                                        if instructLeft == TempRegister:
                                                            ischange = 1
                                                            if 'lea' in instructHead:
                                                                continue
                                                            elif 'mo' in instructHead and '[' + TempRegister not in instructRight:
                                                                break
                                                            else:
                                                                instructLeft, subn_num = re.subn("xmm[0-7]", "xmm",instructLeft)
                                                                instructLeft, subn_num = re.subn("(?:rax|rbx|rcx|rdx|rsi|rdi)(?!\w)", "rregg",instructLeft)
                                                                instructLeft, subn_num = re.subn("(?:eax|ebx|ecx|edx|esi|edi)(?!\w)", "reg",instructLeft)
                                                                instructLeft, subn_num = re.subn("(?:ax|bx|cx|dx|si|di)(?!\w)", "ax", instructLeft)
                                                                instructLeft, subn_num = re.subn("(?:al|bl|cl|dl|ah|bh|ch|dh)(?!\w)", "al",instructLeft)
                                                                # 因为这里是寄存器代替_，与变量不同。这里的和处理就是换位置，比如add _ reg换位成add reg _
                                                                if re.search(regexOnlyregister, instructRight) and 'ebp' not in instructRight and 'rbp' not in instructRight:
                                                                    registerInstruction = '[address]'
                                                                elif re.search(regexregister, instructRight) and 'ebp' not in instructRight and 'rbp' not in instructRight:
                                                                    updataVector('[address]')
                                                                    registerInstruction = '[?+address+?]'
                                                                elif 'cvt' in instructHead:
                                                                    if 'cvtt' in instructHead:
                                                                        instructHead = instructHead.replace('cvtt', 'cvt')
                                                                    instructHead = instructHead[0:5]
                                                                    registerInstruction = instructHead
                                                                elif instructHead == 'cmp':  # mov的情况已经没有，但还有cmp
                                                                    registerInstruction = 'cmp ' + instructLeft
                                                                elif 'mo' in instructHead:
                                                                    registerInstruction = instructHead + ' ' + instructLeft
                                                                else:
                                                                    registerInstruction = instructHead + ' ' + instructLeft + ' _'
                                                            if '['+ TempRegister in instructRight and instructHead != 'mov':
                                                                if 'lea' in instructHead:
                                                                    continue
                                                                newPointerList.append({'PointName': each_var['varName'],
                                                                                       'head': instructHead,
                                                                                       'TempTegister': TempRegister,
                                                                                       'InstructionNear': instructLeft,
                                                                                       'keyInstruction': instructRight.replace(TempRegister,each_var['varName']),
                                                                                       'PointNameOrigin': each_var['varName']})
                                                        elif re.search(regexregister, instructLeft):
                                                            if 'lea' in instructHead:
                                                                continue
                                                            if  'ebp' not in instructLeft and 'rbp' not in instructLeft:  # 有ebp的话就跟你无关了
                                                                if re.search(regexOnlyregister, instructLeft):
                                                                    registerInstruction = '[address]'
                                                                else:
                                                                    updataVector('[address]')
                                                                    registerInstruction = '[?+address+?]'
                                                                newPointerList.append({'PointName': each_var['varName'],
                                                                                       'head': instructHead,
                                                                                       'TempTegister': TempRegister,
                                                                                       'InstructionNear': instructRight,
                                                                                       'keyInstruction': instructLeft.replace(TempRegister,each_var['varName']),
                                                                                      'PointNameOrigin': each_var['varName']})
                                                                #print(newPointerList)

                                                    elif TempRegister in instructRight:  # 如果出现在右边
                                                        if 'lea' in instructHead:
                                                            continue
                                                        if instructRight == TempRegister:
                                                            # 先找出nearby关系
                                                            if instructHead == TempHead and instructLeft != TempVar:
                                                                matvarnameUp = re.search('\[(ebp|rbp)\+(.+)\]', TempVar)
                                                                matvarnameDown = re.search('\[(ebp|rbp)\+(.+)\]',instructLeft)
                                                                if matvarnameUp and matvarnameDown:
                                                                    VarDown = matvarnameDown.groups()[1]
                                                                    VarUp = matvarnameUp.groups()[1]
                                                                    #if not '+' in VarUp and not '+' in VarDown:
                                                                    for eavar in variables:
                                                                        if VarDown == eavar['varName']:
                                                                            if eavar['byteNum'] == each_var['byteNum']:
                                                                                self.UDrelation.append(functionName + ':' + VarUp + '---' + functionName + ':' + VarDown)
                                                                                # print(functionName + ':' + VarUp + '---' + functionName + ':' + VarDown)
                                                                            elif eavar['byteNum'] != each_var['byteNum']:
                                                                                if 'arg' in each_var['varName']:
                                                                                    each_var['byteNum'] = eavar['byteNum']
                                                                                    self.UDrelation.append(functionName + ':' + VarUp + '---' + functionName + ':' + VarDown)
                                                                                    # print(functionName + ':' + VarUp + '---' + functionName + ':' + VarDown)
                                                                        elif 'arg' in each_var['varName'] and VarDown == eavar['varName'] + '+4':
                                                                            #删除这种arg
                                                                            removeIndex = 0
                                                                            for i in range(len(self.FuncAndPara) - 1, -1, -1):
                                                                                if self.FuncAndPara[i]['Name'] == functionName + ':' + each_var['varName'] :
                                                                                    self.FuncAndPara.remove(self.FuncAndPara[i])
                                                                                    removeIndex = i
                                                                                    break
                                                                            #因为删了一个，函数表里面要调整
                                                                            if removeIndex != 0:
                                                                                for i in range(removeIndex,len(self.FuncAndPara)):
                                                                                    if functionName + ':' in self.FuncAndPara[i]['Name']:
                                                                                        self.FuncAndPara[i]['ParaNum'] = functionName + 'P' + str(i+1)
                                                                            #print(functionName + ':' + VarUp + '---' + functionName + ':' + VarDown)

                                                                    # print(functionName + ':' + VarUp + '---' + functionName + ':' + VarDown)

                                                            instructRight, subn_num = re.subn("xmm[0-7]", "xmm",instructRight)
                                                            instructRight, subn_num = re.subn("(?:rax|rbx|rcx|rdx|rsi|rdi)(?!\w)", "rregg",instructRight)
                                                            instructRight, subn_num = re.subn("(?:eax|ebx|ecx|edx|esi|edi)(?!\w)", "reg",instructRight)
                                                            instructRight, subn_num = re.subn("(?:ax|bx|cx|dx|si|di)(?!\w)", "ax", instructRight)
                                                            instructRight, subn_num = re.subn("(?:al|bl|cl|dl|ah|bh|ch|dh)(?!\w)", "al",instructRight)
                                                            if 'cvt' in instructHead:
                                                                if 'cvtt' in instructHead:
                                                                    instructHead = instructHead.replace('cvtt', 'cvt')
                                                                instructHead = instructHead[0:5]
                                                                registerInstruction = instructHead
                                                            elif instructHead == 'cmp':  # mov的情况已经没有，但还有cmp
                                                                registerInstruction = 'cmp ' + instructRight
                                                            elif 'mo' in instructHead:
                                                                registerInstruction = instructHead + ' ' + instructRight
                                                            else:
                                                                registerInstruction = instructHead + ' ' + instructRight + ' _'
                                                        elif re.search(regexregister, instructRight):
                                                            if 'ebp' not in instructRight and 'rbp' not in instructRight:  # 有ebp的话就跟你无关了
                                                                if re.search(regexOnlyregister, instructRight):
                                                                    registerInstruction = '[address]'
                                                                else:
                                                                    updataVector('[address]')
                                                                    registerInstruction = '[?+address+?]'
                                                                newPointerList.append({'PointName': each_var['varName'],
                                                                                       'head': instructHead,
                                                                                       'TempTegister': TempRegister,
                                                                                       'InstructionNear': instructLeft,
                                                                                       'keyInstruction': instructRight.replace(TempRegister,each_var['varName']),
                                                                                       'PointNameOrigin': each_var['varName']})

                                                                if not instructHead.find('mo') == -1:
                                                                    if lineNum + k +1 < ContextLen and ',' in fileContext[lineNum + k + 1]:
                                                                        tempHead, tempRest = fileContext[lineNum + k +1 ].strip().split(' ', 1)
                                                                        tempLeft, tempRight = tempRest.strip().split(',', 1)
                                                                        tempRight = tempRight.strip()
                                                                        tempLeft = tempLeft.strip()
                                                                        if tempRight==instructLeft or (tempLeft==instructLeft and 'mo' not in tempHead):
                                                                            newPointerList.append({'PointName': each_var['varName'],
                                                                                                   'head': tempHead,
                                                                                                   'TempTegister': '',
                                                                                                   'InstructionNear': '',
                                                                                                   'keyInstruction': instructRight.replace(TempRegister,each_var['varName']),
                                                                                                   'PointNameOrigin': each_var['varName']})
                                                                        elif '['+instructLeft+']' in tempLeft or '['+instructLeft+']' in tempRight:
                                                                            newPointerList.append(
                                                                                    {'PointName': each_var['varName'],
                                                                                     'head': '[address]',
                                                                                     'TempTegister': '',
                                                                                     'InstructionNear': '',
                                                                                     'keyInstruction': instructRight.replace(TempRegister,each_var['varName']),
                                                                                     'PointNameOrigin': each_var['varName']})

                                                                        #print(fileContext[lineNum + k +1 ])

                                                    #print(registerInstruction)
                                                    updataVector(registerInstruction)

                                                    if ischange ==1:
                                                        break

                                                elif lineNum + k < ContextLen and ',' not in fileContext[lineNum + k]:
                                                    regexregister = '\[.*' + TempRegister + '.*\]'
                                                    regexOnlyregister = '\[' + TempRegister + '\]'
                                                    if re.search(regexOnlyregister,fileContext[lineNum + k]):
                                                        updataVector('[address]')
                                                    elif re.search(regexregister,fileContext[lineNum + k]):
                                                        updataVector('[address]')
                                                        updataVector('[?+address+?]')

                                                elif lineNum + k < ContextLen and 'push' in fileContext[lineNum + k]:
                                                    matPushReg = re.search('push[ \t]+(\w+)',fileContext[lineNum + k])
                                                    if matPushReg:
                                                        if matPushReg.groups()[0] == TempRegister:
                                                            fileContext[lineNum + k] = fileContext[lineNum + k].replace(TempRegister , '[ebp+'+each_var['varName']+']')
                                                            break

                                                elif lineNum + k < ContextLen and 'call' in fileContext[lineNum + k]:
                                                    matCallReg = re.search('call[ \t]+(\w+)', fileContext[lineNum + k])
                                                    if matCallReg:
                                                        if matCallReg.groups()[0] == TempRegister:
                                                            updataVector('FPptr')
                                                            updataVector('FPFunc')
                                                            self.FP_Pointer_rel.append(functionName+':'+each_var['varName']+'---Func*')
                                                            break

                                                # 如果下一行找到了temp寄存器，那就要跳出
                                                if TempRegister in fileContext[lineNum + k] or 'call' in fileContext[lineNum + k] or 'loc' in fileContext[lineNum + k] or re.search('^j.+', instructHead):
                                                    pass

                                        except:
                                            pass
                                        """
                                    #上面考虑到mov reg的特殊情况，把reg替换成变量继续往下找
                                     """

                                    # 判断左边是不是128位寄存器
                                    elif left.find('xmm') != -1:
                                        instructionIR = head + ' xmm _'
                                    elif head == 'cmp':
                                        instructionIR = 'cmp ' + left
                                    # 剩下的一般都是32位寄存器，不是的话也这样处理
                                    else:
                                        instructionIR = head + ' ' + left + ' _'
                                else:
                                    #print("File2Vector Error:cannot find '_'")
                                    pass

                            updataVector(instructionIR)

                    # dword,word,byte这些信息直接给一个较大的值，比如75
                    if issearchwordptr==0:
                        count = 0
                        for each_instruction in self.Instructions_list:
                            if each_instruction == each_var['byteNum']:
                                Vector_list_element[count] = 75
                                break
                            count += 1

                    # 如果向量为0向量，那么去掉该向量
                    flag = 0
                    CountNotZero = 0
                    for i in range(0,len(Vector_list_element)):
                        #if i==9:#这个刚好是mov，要根据Instructions_List修改
                        #    continue
                        if Vector_list_element[i] != 0:
                            CountNotZero += 1
                            continue
                        #elif CountNotZero == 1 and each_var['byteNum'] == 'byte':
                        #    flag = 0
                        elif CountNotZero >= 1:
                            flag = 1
                            break

                    """
                    for each_is_zero in Vector_list_element:
                        if each_is_zero != 0:
                            CountNotZero += 1
                            continue
                        if CountNotZero >= 1:
                            flag = 1
                            break"""
                    # 不是0向量的是有效结果
                    if flag == 1:
                        if each_var['offset'] != 'global':
                            # 把前面的结果追加到self.Vector_list中
                            self.Vector_list.append(Vector_list_element)
                            # 把相应的函数及其变量名增加到self.Name_list_list中
                            if '+' in each_var['varName']:
                                if re.search('(reg|rregg|eax|ebx|ecx|edx|rax|rbx|rcx|rdx)' , each_var['varName']):
                                    tempLeft,tempRight = each_var['varName'].split('+',1)
                                    each_var['varName'] = tempRight + '+' + tempLeft
                                #print(each_var['varName'])
                            self.Name_list.append(functionName + ':' + each_var['varName'])
                            # label随便给标签
                            self.Label_list.append(-1)
                            self.Offset_list.append(each_var['offset'])

                        elif each_var['offset'] == 'global':
                            self.globalVarVector.append(Vector_list_element)
                            self.globalVarName.append(each_var['varName'])
                            self.globalVarLabel.append(-1)

        except IOError as err:
            print('File error:' + str(err))





        #然后把指向的变量也转成向量进行预测
        #相同名字的整理到一起
        TempPointName=set()#创建一个暂时用来保存指针名信息的集合
        for i in range(0,len(newPointerList)):
            index1=newPointerList[i]['keyInstruction'].find('[')
            index2=newPointerList[i]['keyInstruction'].find(']')
            #去掉诸如eax+i*4这种情况
            if not newPointerList[i]['PointName'] + '*' in newPointerList[i]['keyInstruction'][index1+1:index2]:
                TempPointName.add(newPointerList[i]['keyInstruction'][index1+1:index2])
                newPointerList[i]['PointName']=newPointerList[i]['keyInstruction'][index1+1:index2]

        #print(newPointerList)
        #print(TempPointName)

        L=list(TempPointName)
        L.sort()
        for each in L:
            Vector_list_element = []  # Vector_list的组成元素,初始化为全0

            for i in range(len(self.Instructions_list)):
                Vector_list_element.append(0)

                # 定义一个下面经常用的函数
                # 在指令字典中查找，如果有的话就在相应的向量位置上+1
            def updataVectorOnlyHead(head):
                # 在指令字典中查找，如果有的话就在相应的向量位置上+1
                count = 0
                for each_instruction in self.Instructions_list:
                    if head in each_instruction:
                        if 'byte' in head or 'word' in head:
                            Vector_list_element[count] = 75
                            break
                        if 'address' in head:
                            # print(IR)
                            Vector_list_element[count] = 25
                            break
                        Vector_list_element[count] += 1
                        break
                    elif each_instruction == '#':
                        if not head == 'UK' and head != 'not _' and head != 'push':
                            #print(head,end=' \t...\n')  # 总集里没有的指令输出看看
                            pass
                        break
                    count += 1

            for every in newPointerList:
                if each==every['PointName']:
                    IR=every['head']
                    isupdatebitnum=0#0已经更新了位数信息
                    if 'byte ptr' in every['keyInstruction'] or 'BYTE PTR' in every['keyInstruction']:
                        updataVectorOnlyHead("byte")
                        isupdatebitnum=1
                    elif 'dword ptr' in every['keyInstruction'] or 'DWORD PTR' in every['keyInstruction']:
                        updataVectorOnlyHead("dword")
                        isupdatebitnum=1
                    elif 'qword ptr' in every['keyInstruction'] or 'QWORD PTR' in every['keyInstruction']:
                        updataVectorOnlyHead("qword")
                        isupdatebitnum=1
                    elif 'word ptr' in every['keyInstruction'] or 'WORD PTR' in every['keyInstruction']:
                        updataVectorOnlyHead("word")
                        isupdatebitnum = 1

                    instructionNear, subn_num = re.subn("(0x)?[0-9][0-9a-fA-F]*h?(?!\w)", "imm", every['InstructionNear'])  # 单独数,都看成是立即数
                    instructionNear, subn_num = re.subn("xmm[0-7]", "xmm", instructionNear)
                    instructionNear, subn_num = re.subn("(?:rax|rbx|rcx|rdx|rsi|rdi)(?!\w)", "rregg", instructionNear)
                    instructionNear, subn_num = re.subn("(?:eax|ebx|ecx|edx|esi|edi)(?!\w)", "reg", instructionNear)
                    instructionNear, subn_num = re.subn("(?:ax|bx|cx|dx|si|di)(?!\w)", "ax", instructionNear)
                    instructionNear, subn_num = re.subn("(?:al|bl|cl|dl|ah|bh|ch|dh)(?!\w)", "al", instructionNear)

                    if 'imm' in instructionNear:
                        updataVectorOnlyHead(head + ' _ ' + 'imm')

                    if isupdatebitnum==0:

                        if 'xmm' in instructionNear:
                            updataVectorOnlyHead('qword')
                        if 'ax' in instructionNear:
                            updataVectorOnlyHead('word')
                        if 'reg' in instructionNear:
                            updataVectorOnlyHead('dword')
                        if 'al' in instructionNear:
                            updataVectorOnlyHead('byte')

                    updataVectorOnlyHead(IR)

            FPset = set(self.FP_Pointer_rel)  # 集合去重复
            for e in FPset:
                left,right=e.split('---',1)
                if functionName + ':' + each == left:
                    if '*' in right:
                        updataVectorOnlyHead('FPptr')
                        if "*" == right:
                            break
                    updataVectorOnlyHead('FP' + right.replace('*',''))
                    updataVectorOnlyHead('FP' + right.replace('*',''))
                    updataVectorOnlyHead('FP' + right.replace('*',''))


            self.pointer_name_list.append(functionName+':'+each)
            self.pointer_label_list.append(-1)
            self.pointer_vector_list.append(Vector_list_element)

            #print(Vector_list_element)


        # 先整理一下向量，最大值不超过10,并且有mov imm就不要mov bool了
        for each in self.Vector_list:
            for i  in range(7, len(each)):
                if each[i] > 10:
                    each[i] = 10
                if self.Instructions_list[i] == 'mov _ imm' and each[i] > 0:
                    if each[i-1] == each[i]:
                        each[i] =0
                    elif each[i-1] < each[i]:
                        each[i-1] = 0
                if self.Instructions_list[i] == 'cmp _ imm' and each[i] > 0:
                    if each[i-1] == each[i]:
                        each[i] =0
                    elif each[i-1] < each[i]:
                        each[i-1] = 0
        for each in self.pointer_vector_list:
            for i in range(7, len(each)):
                if each[i] > 10:
                    each[i] = 10


        #print(self.function_parameter_list)
        #print('over')


    def updateVector(self,Name,Key,weight,change=0):
        #print('\n___start update:')
        for each_name,each_vector in zip(self.Name_list,self.Vector_list):
            if each_name == Name:
                #print(Name)
                #print(each_vector)
                for i in range(0,len(self.Instructions_list)):
                    if self.Instructions_list[i] == Key:
                        if change==0:
                            each_vector[i] += weight
                        elif change==1:
                            each_vector[i] = weight

    def addFunctionPrototype(self,filename):
        try:
            with open(filename) as FPfile:
                for line in FPfile.readlines():
                    mat = re.search('([A-Za-z0-9_]+)\((.*)\)', line)
                    if mat:
                        Fname = mat.groups()[0]
                        temp = mat.groups()[1]
                        temp = temp.replace('size_t','int')
                        if 'const' in temp:
                            temp = temp.replace(' const ', '')
                            temp = temp.replace(' const', '')
                            temp = temp.replace('const ', '')
                            temp = temp.replace('const','')
                        if 'struct' in temp:
                            temp = temp.replace(' struct ', '')
                            temp = temp.replace(' struct', '')
                            temp = temp.replace('struct ', '')
                            temp = temp.replace('struct', '')
                        temp = temp.replace('\t', ' ')
                        temp = temp.strip()

                        lasttype = ''  # 如果遇到...就有用
                        i = 1
                        while True:
                            if Fname=='printf' or Fname=='sprintf':
                                break
                            try:
                                if ',' in temp:
                                    para , temp = temp.split(',',1)
                                    temp = temp.strip()
                                    para = para.strip()
                                    if re.search('\[.*\]',para):
                                        p = re.compile('\[.*\]')
                                        para = p.sub('', para)
                                        left , right = para.split(' ',1)
                                        para = left+'* '+right
                                    if ' ' not in para:
                                        paratype = para
                                        if re.search('(int|float|double|long|bool|char|short|void)',paratype) or paratype=='*':
                                            self.function_parameter_list.append({'funcPara': Fname + 'P' + str(i), 'paraType': paratype})
                                        else:
                                            if '*' in paratype:
                                                paratype = 'void*'
                                                self.function_parameter_list.append({'funcPara': Fname + 'P' + str(i), 'paraType': paratype})
                                            else:
                                                pass
                                                #paratype = 'struct'
                                                #self.function_parameter_list.append({'funcPara': Fname + 'P' + str(i), 'paraType': paratype})
                                        lasttype = paratype  # 如果遇到...就有用
                                        # print (Fname+'P'+str(i) , paratype)
                                    else:
                                        paratype, notimport = para.split(' ',1)
                                        #先统一删除*，然后再统一添加
                                        if '*' in paratype:
                                            p = re.compile('\*')
                                            paratype = p.sub('', paratype)
                                        #统一加*
                                        if '*' in para:
                                            paratype = paratype + '*'
                                        if re.search('(int|float|double|long|bool|char|short|void)',paratype) or paratype == '*':
                                            self.function_parameter_list.append({'funcPara':Fname+'P'+str(i) , 'paraType':paratype})
                                        else:
                                            if '*' in paratype:
                                                paratype = 'void*'
                                                self.function_parameter_list.append({'funcPara': Fname + 'P' + str(i), 'paraType': paratype})
                                            else:
                                                pass
                                                #paratype = 'struct'
                                                #self.function_parameter_list.append({'funcPara': Fname + 'P' + str(i), 'paraType': paratype})
                                        lasttype = paratype  # 如果遇到...就有用
                                        #print (Fname+'P'+str(i) , paratype)
                                else:
                                    if temp.strip()!='' and ' ' in temp:
                                        temp = temp.strip()
                                        if re.search('\[.*\]', temp):
                                            p = re.compile('\[.*\]')
                                            temp = p.sub('', temp)
                                            left, right = temp.split(' ', 1)
                                            temp = left + '* ' + right
                                        temptype, notimport = temp.split(' ', 1)
                                        # 先统一删除*，然后再统一添加
                                        if '*' in temptype:
                                            p = re.compile('\*')
                                            temptype = p.sub('', temptype)
                                        # 统一加*
                                        if '*' in temp:
                                            temptype = temptype + '*'
                                        if re.search('(int|float|double|long|bool|char|short|void)',temptype) or temptype == '*':
                                            self.function_parameter_list.append({'funcPara': Fname + 'P' + str(i), 'paraType': temptype})
                                        else:
                                            if '*' in temptype:
                                                temptype = 'void*'
                                                self.function_parameter_list.append({'funcPara': Fname + 'P' + str(i), 'paraType': temptype})
                                            else:
                                                pass
                                                #temptype = 'struct'
                                                #self.function_parameter_list.append({'funcPara': Fname + 'P' + str(i), 'paraType': temptype})
                                        lasttype = temptype#如果遇到...就有用
                                        #print(Fname + 'P' + str(i), temptype)
                                    elif ' ' not in temp.strip():
                                        temptype=temp.strip()
                                        if temptype=='...' and lasttype!='':
                                            if Fname=='error':
                                                break
                                            self.function_parameter_list.append({'funcPara': Fname + 'P' + str(i), 'paraType': lasttype})
                                            self.function_parameter_list.append({'funcPara': Fname + 'P' + str(i+1), 'paraType': lasttype})
                                            self.function_parameter_list.append({'funcPara': Fname + 'P' + str(i+2), 'paraType': lasttype})
                                            # print(Fname + 'P' + str(i), lasttype)
                                        elif temptype!='void':
                                            if re.search('(int|float|double|long|bool|char|short|void)',temptype) or temptype == '*':
                                                self.function_parameter_list.append({'funcPara': Fname + 'P' + str(i), 'paraType': temptype})
                                            else:
                                                if '*' in temptype:
                                                    temptype = 'void*'
                                                    self.function_parameter_list.append({'funcPara': Fname + 'P' + str(i), 'paraType': temptype})
                                                else:
                                                    pass
                                                    #temptype = 'struct'
                                                    #self.function_parameter_list.append({'funcPara': Fname + 'P' + str(i), 'paraType': temptype})
                                            lasttype = temptype  # 如果遇到...就有用
                                            #print(Fname + 'P' + str(i), temptype)
                                    break
                                i = i + 1
                            except:
                                pass
        except:
            pass

    def mergeGlobalVar(self):
        GolbalList = list(self.globalVarNameSet)
        GolbalVector = []

        for each in GolbalList:
            vectorEle = [0] * len(self.globalVarVector[0])
            GolbalVector.append(vectorEle)

        for eachGolbalVar,eachGolbalVector in zip(GolbalList,GolbalVector):
            for eachName,eachVector in zip(self.globalVarName, self.globalVarVector):
                if eachName == eachGolbalVar:
                    GlobalVectorAddGlobalVector(eachGolbalVector,eachVector)

        self.globalVarName = GolbalList
        self.globalVarVector = GolbalVector
        self.globalVarLabel = [-1] * len(self.globalVarName)
