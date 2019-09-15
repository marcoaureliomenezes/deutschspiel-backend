# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 00:05:06 2019

@author: Marco Menezes
"""
import xlrd
import time

mutterspracheMsg = "\nWählen Sie bitte eine Muttersprache für die Übersetzung:\n\n"
invalidInput = "Bitte geben Sie eine gültige Nummer ein!\n"
themaMsg = "\nWählen Sie bitte eine Nummer für das Thema des Spiels:\n\n"


class SpSheet():   
    def __init__(self):
        pass
#------------------------------------------------------------------------------#   
    def accessSP(aba):
        deutschspreadsheet = xlrd.open_workbook('Deutsch_Databank.xlsx')
        Aba = deutschspreadsheet.sheet_by_name(aba)
        return Aba

#------------------------------------------------------------------------------#  
    def Cell(self,Aba,line,column):
        return Aba.cell(line,column).value
#------------------------------------------------------------------------------#     
    def refCLabel(self,aba,label):
        count = 0
        while 1:
            if label == SpSheet.Cell(self,aba,0,count):
                break
            if SpSheet.Cell(self,aba,0,count) == "end":
                print("Es gibt keine Label heißt", label)
                break
            count += 1
        return count
#------------------------------------------------------------------------------#
    def refSubTitles(self,aba,name):
        lista = []
        for i in range(0,4):
            for j in range(0,100):
                if SpSheet.Cell(self,aba,i,j) == name:
                    count = 1
                    while SpSheet.Cell(self,aba,i,j + count) == '':
                        count += 1
                    lista.append([(i,j),count])
        return lista
#------------------------------------------------------------------------------#
    def gettitles(self,aba):
        titleList = []
        for i in range(0,200):
            if SpSheet.Cell(self,aba,0,i) == 'end':
                break
            if SpSheet.Cell(self,aba,0,i) != '':
                titleList.append(SpSheet.Cell(self,aba,0,i))
        return titleList
    
#------------------------------------------------------------------------------#   
    def choseTrans(self):
        tongue =[]
        tRef = SpSheet.refSubTitles(self,"Übersetzung")
       # for i in tRef: TODO: CHECK THE TRANSLATE COLUMNS PER TITLE.
       #     print(i[1])
        line = ((tRef[0])[0])[0]
        col = ((tRef[0])[0])[1]
        size = (tRef[0])[1]       
        for i in range(0,size):
            tongue.append(SpSheet.Cell(self,line+1,col+i))             
        print(mutterspracheMsg)
        inputMT = 0
        while 1:
            confList = SpSheet.printEnumList(self,tongue)
            inputMT = input("Muttersprache: ")
            if inputMT in confList:
                break
            print(invalidInput)
            time.sleep(2)                     
        inputMT = int(inputMT)
        print("Muttersprache: ",tongue[inputMT-1])
        time.sleep(2)
        return inputMT
    
#------------------------------------------------------------------------------#
        
    def numElem(self,aba, title):        
        vRef = SpSheet.refCLabel(self,aba,title)
        for i in range(1,5):
            if SpSheet.Cell(self,aba,i,vRef+1) == "":
                initLine = i+1
                break
        count = 0
        while(1):
            if SpSheet.Cell(self,aba,count,vRef) == '':
                finalLine = count
                break
            count += 1
        return [initLine,finalLine]

#------------------------------------------------------------------------------#
        
    def choseTitle(self, titles):
        confirmList = []
        print(themaMsg)
        for i in range(0,len(titles)):
            confirmList.append(str(i+1))
            print(str(i+1),"-", titles[i])
        thema = ''
        while thema not in(confirmList):
            print(invalidInput)            
            thema = input()        
        intThema = int(thema)
        return titles[intThema - 1]
    
#------------------------------------------------------------------------------#
play = SpSheet()
aba = SpSheet.accessSP("Nomen")

