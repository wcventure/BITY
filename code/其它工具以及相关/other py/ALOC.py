#coding=utf-8
#ALOC.py

with open('123.txt') as f:
    text=f.readlines()
    lineCount =0
    for eachline in text:
        if eachline.strip() != "": #remove space and tabIndent line
            if eachline.find(';') == 0: #remove comment
                pass
            else:
                lineCount += 1

    print(lineCount)
