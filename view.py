

from tkinter import *
lastValue=""
memoryValue=""
memoryOperator=""
memory=[]
#***************************************************************************
#***********************************inputWrite******************************
#***************************************************************************      
def inputWrite(btnValue):
        global lastValue
        global memoryValue
        global memoryOperator
        #***************************numberWrite*****************************
        if (btnValue in [1,2,3,4,5,6,7,8,9]):
            if(lastValue != "" and memoryValue=="" and memoryOperator==""and lastValue!="0"):
                lastValue+=str(btnValue)
                btnValue=str(btnValue)
                print("numberWrite 01 --> :",lastValue) 
                s=len(inputDisplay.get())
                inputDisplay.insert(s,str(btnValue))  
                totalDisplay['text']=lastValue
            elif(lastValue == "" and memoryValue=="" and memoryOperator==""and lastValue!="0"):
                lastValue+=str(btnValue)
                btnValue=str(btnValue)
                print("numberWrite 02 --> :",lastValue) 
                s=len(inputDisplay.get())
                inputDisplay.insert(s,str(btnValue))  
                totalDisplay['text']=lastValue
            elif(lastValue != "0" and memoryValue!="" and memoryOperator!=""):
                if(memoryOperator=="="):
                    memoryValue=""
                    memoryOperator=""
                lastValue+=str(btnValue)
                btnValue=str(btnValue)
                print("numberWrite 03 --> :",lastValue) 
                s=len(inputDisplay.get())
                inputDisplay.insert(s,str(btnValue))  
                totalDisplay['text']=memoryValue+memoryOperator+lastValue
            elif(lastValue == "" and memoryValue!="" and memoryOperator==""):
                lastValue+=str(btnValue)
                memoryValue=""
                btnValue=str(btnValue)
                print("numberWrite 04 --> :",lastValue) 
                s=len(inputDisplay.get())
                inputDisplay.insert(s,str(btnValue))  
                totalDisplay['text']=""
            elif(lastValue == "0" and memoryValue=="" and memoryOperator=="."):
                print("numberWrite 05 --> :",lastValue) 
                s=len(inputDisplay.get())
                inputDisplay.insert(s,str(btnValue))  
                totalDisplay['text']=""
        #***************************zeroWrite*******************************
        if (btnValue==0):
            print(" zeroWite welecome :",btnValue)
            print("lastValue :",lastValue)
            print("btnValue :",btnValue)
            print("memoryOperator :",memoryOperator)
            print("memoryValue :",memoryValue)
            btnValue=str(btnValue)
            print(type(btnValue))
            if ( memoryValue=="" and lastValue =="" and memoryOperator==""):
                print("zeroWrite:01")
                lastValue += btnValue
                s=len(inputDisplay.get())
                inputDisplay.insert(s,str(btnValue))  
                totalDisplay['text']=lastValue
                
            elif ( lastValue == "0." and memoryValue=="" and memoryOperator==""): 
                print("zeroWrite:02")
                lastValue += btnValue
                s=len(inputDisplay.get())
                inputDisplay.insert(s,str(btnValue))  
                totalDisplay['text']=lastValue
            
            elif (  lastValue !="0"and  memoryValue==""and memoryOperator==""): 
                print("zeroWrite:03")
                lastValue += btnValue
                s=len(inputDisplay.get())
                inputDisplay.insert(s,str(btnValue))  
                totalDisplay['text']=lastValue
                
            elif (  lastValue !="0"and  memoryValue!=""and memoryOperator!=""):
                print("zeroWrite:04")
                lastValue += btnValue
                s=len(inputDisplay.get())
                inputDisplay.insert(s,str(btnValue))
                totalDisplay['text']=memoryValue +memoryOperator + lastValue

            elif ( lastValue ==""and memoryValue!=""and memoryOperator==""):
                print("zeroWrite:05")
                memoryValue=""
                lastValue += btnValue
                s=len(inputDisplay.get())
                inputDisplay.insert(s,str(btnValue))
                totalDisplay['text']=lastValue
         #**************************doubleZeroWrite*************************  
        if (btnValue=="00"):
            print(" doubleZeroWite wlecome :",btnValue)
            print("double zero type--->",type(btnValue))
            if (lastValue == "."and memoryValue=="" and memoryOperator==""): 
                print("doubleZeroWrite:01")
                lastValue += btnValue
                s=len(inputDisplay.get())
                inputDisplay.insert(s,str(btnValue))
                totalDisplay['text']=lastValue
                
            elif (lastValue != "" and memoryValue!=""and memoryOperator !="" and lastValue!="0"):
                print("doubleZeroWrite:02")
                lastValue += btnValue
                s=len(inputDisplay.get())
                inputDisplay.insert(s,str(btnValue))
                totalDisplay['text']= memoryValue + memoryOperator + lastValue
                               
            elif (lastValue != ""and memoryValue!="" and memoryOperator !="" and lastValue!="0"):
                print("doubleZeroWrite:03")
                lastValue += btnValue
                s=len(inputDisplay.get())
                inputDisplay.insert(s,str(btnValue))
                totalDisplay['text']=memoryValue + memoryOperator + lastValue
                
            elif (lastValue != ""and memoryValue=="" and memoryOperator ==""and lastValue!="0"):
                print("doubleZeroWrite:04")
                lastValue += btnValue
                s=len(inputDisplay.get())
                inputDisplay.insert(s,str(btnValue))
                totalDisplay['text']=lastValue

            elif (lastValue != ""and memoryValue!=""and memoryOperator =="" and lastValue!="0"): 
                print("doubleZeroWrite:05")
                lastValue += btnValue
                s=len(inputDisplay.get())
                inputDisplay.insert(s,str(btnValue))
                totalDisplay['text']=lastValue
          #*************************pointWrite******************************  
        if (btnValue=="."):

            if((not btnValue in lastValue) and memoryOperator!="" and memoryValue!="" ):
                if(memoryOperator=="="):
                    memoryValue=""
                    memoryOperator=""
                if (lastValue =="" ):
                    btnValue="0"+btnValue
                lastValue+=btnValue
                print("pointWrite 01 --> :",lastValue) 
                s=len(inputDisplay.get())
                inputDisplay.insert(s,str(btnValue))  
                totalDisplay['text'] =memoryValue+memoryOperator+lastValue  

            elif((not btnValue in lastValue) and memoryOperator=="" and memoryValue==""):
                if (lastValue ==""):
                    btnValue="0"+btnValue
                lastValue+=btnValue
                print("pointWrite 02 --> :",lastValue) 
                s=len(inputDisplay.get())
                inputDisplay.insert(s,str(btnValue))  
                totalDisplay['text'] =memoryValue+memoryOperator+lastValue   

            elif(memoryValue!="" and memoryOperator!="" and lastValue!="." and (not btnValue in lastValue)):
                lastValue+=btnValue
                print("pointWrite 03 --> :",lastValue) 
                s=len(inputDisplay.get())
                inputDisplay.insert(s,str(btnValue))
                totalDisplay['text'] =lastValue
            elif((not btnValue in lastValue) and memoryOperator=="" and memoryValue!=""):
                if (lastValue ==""):
                    btnValue="0"+btnValue
                memoryValue=""
                lastValue+=btnValue
                print("pointWrite 04--> :",lastValue) 
                s=len(inputDisplay.get())
                inputDisplay.insert(s,str(btnValue))  
                totalDisplay['text'] =""                          
#***************************************************************************     
# **********************************Calculate*******************************
# **************************************************************************
def calculate(btnValue):
        global lastValue
        global memoryValue
        global memoryOperator
        #***************************addition********************************
        if(btnValue=="+"):
            print(" calculate -->Value :",btnValue)
            if (memoryOperator == "+" and lastValue != "" and  memoryValue != ""):
                memoryValue = str((float(memoryValue) + float(lastValue)))
                inputDisplay.delete(0,END)
                totalDisplay['text'] =memoryValue + btnValue            
                memoryOperator = btnValue
                btnValue = ""
                lastValue = ""
            elif (memoryOperator == "-" and lastValue != "" and memoryValue != ""):
                memoryValue = str((float(memoryValue) - float(lastValue)))
                inputDisplay.delete(0,END)
                totalDisplay['text'] =memoryValue + btnValue
                memoryOperator = btnValue
                lastValue = ""
            elif (memoryOperator == "x" and lastValue != "" and memoryValue != ""): 
                memoryValue = str((float(memoryValue) * float(lastValue)))
                inputDisplay.delete(0,END)
                totalDisplay['text']=memoryValue + btnValue
                memoryOperator = btnValue
                lastValue = ""
           
            elif (memoryOperator == "/" and lastValue != "" and memoryValue != ""):
                memoryValue = str((float(memoryValue) / float(lastValue)))
                inputDisplay.delete(0,END)
                totalDisplay['text']=memoryValue + btnValue
                memoryOperator = btnValue
                lastValue = ""
            
            elif (memoryOperator == "%" and lastValue != "" and  memoryValue 
              != ""):
                memoryValue = str(((float(memoryValue) /100)*float(lastValue)))
                inputDisplay.delete(0,END)
                totalDisplay['text']=memoryValue + btnValue
                memoryOperator = btnValue
                btnValue = ""
                lastValue = ""
            
            elif (memoryOperator != "+" and memoryOperator != "" and lastValue == ""):
                memoryOperator = btnValue
                totalDisplay['text'] =memoryValue + btnValue
    
            
            elif (memoryOperator != "+" and memoryOperator == "" and lastValue == "" and  memoryValue!=""):
                memoryOperator = btnValue
                totalDisplay['text']=memoryValue + btnValue
        
            
            elif (memoryOperator == "" and memoryValue == "" and lastValue != ""):
                inputDisplay.delete(0,END)
                totalDisplay['text']=lastValue + btnValue
                memoryValue = lastValue
                memoryOperator = btnValue;  
                btnValue = ""
                lastValue = ""

            #***********************subtraction*****************************

        if(btnValue=="-"):
            print(" calculate -->Value :",btnValue)
            if (memoryOperator == "+" and lastValue != "" and  memoryValue != ""):
                memoryValue = str((float(memoryValue) + float(lastValue)))
                inputDisplay.delete(0,END)
                totalDisplay['text'] =memoryValue + btnValue            
                memoryOperator = btnValue
                btnValue = ""
                lastValue = ""
            elif (memoryOperator == "-" and lastValue != "" and memoryValue != ""):
                memoryValue = str((float(memoryValue) - float(lastValue)))
                inputDisplay.delete(0,END)
                totalDisplay['text'] =memoryValue + btnValue
                memoryOperator = btnValue
                lastValue = ""
            
            elif (memoryOperator == "x" and lastValue != "" and memoryValue != ""): 
                memoryValue = str((float(memoryValue) * float(lastValue)))
                inputDisplay.delete(0,END)
                totalDisplay['text']=memoryValue + btnValue
                memoryOperator = btnValue
                lastValue = ""
            
            elif (memoryOperator == "/" and lastValue != "" and memoryValue != ""):
                memoryValue = str((float(memoryValue) / float(lastValue)))
                inputDisplay.delete(0,END)
                totalDisplay['text']=memoryValue + btnValue
                memoryOperator = btnValue
                lastValue = ""
            
            elif (memoryOperator == "%" and lastValue != "" and  memoryValue 
              != ""):
                memoryValue = str(((float(memoryValue) /100)*float(lastValue)))
                inputDisplay.delete(0,END)
                totalDisplay['text']=memoryValue + btnValue
                memoryOperator = btnValue
                btnValue = ""
                lastValue = ""
            
            elif (memoryOperator != "-" and memoryOperator != "" and lastValue == ""):
                memoryOperator = btnValue
                totalDisplay['text'] =memoryValue + btnValue
    
            
            elif (memoryOperator != "-" and memoryOperator == "" and lastValue == "" and  memoryValue!=""):
                memoryOperator = btnValue
                totalDisplay['text']=memoryValue + btnValue
        
            
            elif (memoryOperator == "" and memoryValue == "" and lastValue != ""):
                inputDisplay.delete(0,END)
                totalDisplay['text']=lastValue + btnValue
                memoryValue = lastValue
                memoryOperator = btnValue;  
                btnValue = ""
                lastValue = ""

             #**********************multiplition*****************************
        
        if(btnValue=="x"):
            print(" calculate -->Value :",btnValue)
            if (memoryOperator == "+" and lastValue != "" and  memoryValue != ""):
                memoryValue = str((float(memoryValue) + float(lastValue)))
                inputDisplay.delete(0,END)
                totalDisplay['text'] =memoryValue + btnValue            
                memoryOperator = btnValue
                btnValue = ""
                lastValue = ""
            elif (memoryOperator == "-" and lastValue != "" and memoryValue != ""):
                memoryValue = str((float(memoryValue) - float(lastValue)))
                inputDisplay.delete(0,END)
                totalDisplay['text'] =memoryValue + btnValue
                memoryOperator = btnValue
                lastValue = ""
            
            elif (memoryOperator == "x" and lastValue != "" and memoryValue != ""): 
                memoryValue = str((float(memoryValue) * float(lastValue)))
                inputDisplay.delete(0,END)
                totalDisplay['text']=memoryValue + btnValue
                memoryOperator = btnValue
                lastValue = ""
            
            elif (memoryOperator == "/" and lastValue != "" and memoryValue != ""):
                memoryValue = str((float(memoryValue) / float(lastValue)))
                inputDisplay.delete(0,END)
                totalDisplay['text']=memoryValue + btnValue
                memoryOperator = btnValue
                lastValue = ""
            
            elif (memoryOperator == "%" and lastValue != "" and  memoryValue 
              != ""):
                memoryValue = str(((float(memoryValue) /100)*float(lastValue)))
                inputDisplay.delete(0,END)
                totalDisplay['text']=memoryValue + btnValue
                memoryOperator = btnValue
                bntValue = ""
                lastValue = ""
            
            elif (memoryOperator != "x" and memoryOperator != "" and lastValue == ""):
                memoryOperator = btnValue
                totalDisplay['text'] =memoryValue + btnValue
    
            elif (memoryOperator != "x" and memoryOperator == "" and lastValue == "" and  memoryValue!=""):
                memoryOperator = btnValue
                totalDisplay['text']=memoryValue + btnValue
        
            elif (memoryOperator == "" and memoryValue == "" and lastValue != ""):
                inputDisplay.delete(0,END)
                totalDisplay['text']=lastValue + btnValue
                memoryValue = lastValue
                memoryOperator = btnValue;  
                btnValue = ""
                lastValue = ""

            #***********************divide*********************************** 

        if(btnValue=="/"):
            print(" calculate -->Value :",btnValue)
            if (memoryOperator == "+" and lastValue != "" and  memoryValue != ""):
                memoryValue = str((float(memoryValue) + float(lastValue)))
                inputDisplay.delete(0,END)
                totalDisplay['text'] =memoryValue + btnValue            
                memoryOperator = btnValue
                btnValue = ""
                lastValue = ""
            elif (memoryOperator == "-" and lastValue != "" and memoryValue != ""):
                memoryValue = str((float(memoryValue) - float(lastValue)))
                inputDisplay.delete(0,END)
                totalDisplay['text'] =memoryValue + btnValue
                memoryOperator = btnValue
                lastValue = ""
            
            elif (memoryOperator == "x" and lastValue != "" and memoryValue != ""): 
                memoryValue = str((float(memoryValue) * float(lastValue)))
                inputDisplay.delete(0,END)
                totalDisplay['text']=memoryValue + btnValue
                memoryOperator = btnValue
                lastValue = ""
            
            elif (memoryOperator == "/" and lastValue != "" and memoryValue != ""):
                memoryValue = str((float(memoryValue) / float(lastValue)))
                inputDisplay.delete(0,END)
                totalDisplay['text']=memoryValue + btnValue
                memoryOperator = btnValue
                lastValue = ""
            
            elif (memoryOperator == "%" and lastValue != "" and  memoryValue 
              != ""):
                memoryValue = str(((float(memoryValue) /100)*float(lastValue)))
                inputDisplay.delete(0,END)
                totalDisplay['text']=memoryValue + btnValue
                memoryOperator = bntValue
                bntValue = ""
                lastValue = ""
            
            elif (memoryOperator != "/" and memoryOperator != "" and lastValue == ""):
                memoryOperator = btnValue
                totalDisplay['text'] =memoryValue + btnValue
    
            elif (memoryOperator != "/" and memoryOperator == "" and lastValue == "" and  memoryValue!=""):
                memoryOperator = btnValue
                totalDisplay['text']=memoryValue + btnValue
        
            elif (memoryOperator == "" and memoryValue == "" and lastValue != ""):
                inputDisplay.delete(0,END)
                totalDisplay['text']=lastValue + btnValue
                memoryValue = lastValue
                memoryOperator = btnValue;  
                btnValue = ""
                lastValue = ""   
             
            # **********************absuluteValueChange**********************
        if(btnValue=="+/-"):
            print("absuluteValueChange")
            if(lastValue != ""and memoryValue == ""and memoryOperator == "" and lastValue !="0"):
                
                print("chageValue 1")
                if (lastValue!=""and float(lastValue)>0):  
                    lastValue=-1*float(lastValue) 
                    lastValue=str(lastValue)
                else:
                    lastValue=-1*float(lastValue)
                    lastValue=str(lastValue)   
                s=len(inputDisplay.get())
                inputDisplay.delete(0,END)
                inputDisplay.insert(0,str(lastValue)) 
                totalDisplay['text']=lastValue
                   
            if (lastValue != ""and memoryValue != ""and memoryOperator != ""and lastValue !="0" ):
                print("chageValue 2")
                if (lastValue!=""and float(lastValue) > 0):
                    lastValue=-1*float(lastValue)
                    lastValue=str(lastValue)
                else:
                    lastValue=-1*float(lastValue)
                    lastValue=str(lastValue)
                s=len(inputDisplay.get())
                inputDisplay.delete(0,END)
                inputDisplay.insert(0,str(lastValue)) 
                if(float(lastValue)>0):
                    totalDisplay['text']=memoryValue+memoryOperator+lastValue
                else:
                    totalDisplay['text']=memoryValue+memoryOperator+"("+lastValue+")"
            
            if (lastValue == ""and memoryValue != ""and memoryOperator == ""and memoryValue !="0"): 
                print("chageValue 3")
                if (memoryValue!=""and float(memoryValue) > 0):
                    memoryValue=-1*float(memoryValue)
                    memoryValue=str(memoryValue)
                else:
                    memoryValue=-1*float(memoryValue)
                    memoryValue=str(memoryValue)
                inputDisplay.delete(0,END)
                totalDisplay['text']=memoryValue+memoryOperator+lastValue
            if (lastValue == ""and memoryValue != ""and memoryOperator != ""and memoryValue !="0"): 
                print("chageValue 3")
                if (memoryValue!=""and float(memoryValue) > 0):
                    memoryValue=-1*float(memoryValue)
                    memoryValue=str(memoryValue)
                    memoryOperator=""
                else:
                    memoryValue=-1*float(memoryValue)
                    memoryValue=str(memoryValue)
                    memoryOperator=""
                inputDisplay.delete(0,END)
                totalDisplay['text']=memoryValue

            # **********************equal ***********************************
        if(btnValue=="="): 
            print("epual)")
            if(memoryOperator=="%"):
                memoryValue=float(memoryValue)*(float(lastValue)/100)
                memoryValue=str(memoryValue)
                inputDisplay.delete(0,END)
                totalDisplay['text']=memoryValue
                memoryOperator=btnValue   
                lastValue =""

            elif (memoryOperator == "+" and lastValue != "" and memoryValue != ""):
                memoryValue = (float(memoryValue) + float(lastValue))
                memoryValue=str(memoryValue)
                inputDisplay.delete(0,END)
                totalDisplay['text']=memoryValue
                memoryOperator=btnValue 
                btnValue =""
                lastValue = ""
            elif (memoryOperator == "-" and lastValue != "" and memoryValue != ""):
                memoryValue = (float(memoryValue) - float(lastValue))
                memoryValue=str(memoryValue)
                inputDisplay.delete(0,END)
                totalDisplay['text']=memoryValue
                memoryOperator=btnValue 
                btnValue =""
                lastValue = ""

            elif (memoryOperator == "x" and lastValue != "" and memoryValue != ""):
                memoryValue = (float(memoryValue) * float(lastValue))
                memoryValue=str(memoryValue)
                inputDisplay.delete(0,END)
                totalDisplay['text']=memoryValue
                memoryOperator=btnValue 
                btnValue =""
                lastValue = ""

            elif (memoryOperator == "/" and lastValue != "" and memoryValue != ""):
                memoryValue = (float(memoryValue) / float(lastValue))
                memoryValue=str(memoryValue)
                inputDisplay.delete(0,END)
                totalDisplay['text']=memoryValue
                memoryOperator=btnValue 
                btnValue =""
                lastValue = ""
            #***********************sqrtOperation**************************** 
        if(btnValue=="√¯"):
            import math
            print("square :"+btnValue)

            if (lastValue != "" and memoryValue == "" and memoryOperator == "" and float(lastValue)>=0 ):
                lastValue=float(lastValue)
                sqrtValue = math.sqrt(lastValue)
                sqrtValue=str(sqrtValue)
                memoryValue = sqrtValue
                lastValue=str(lastValue)
                totalDisplay['text'] = memoryValue
                inputDisplay.delete(0,END)
                print("*****************") 
                lastValue =""
  
            elif (lastValue == ""and memoryValue != "" and memoryOperator == ""): 
                sqrtValue = math.sqrt(float(memoryValue))
                memoryValue = str(sqrtValue)
                totalDisplay['text']= memoryValue
                inputDisplay.delete(0,END)
                print("*****************") 
                lastValue =""   
            elif (lastValue == ""and memoryValue != "" and memoryOperator != ""): 
                sqrtValue = math.sqrt(float(memoryValue))
                memoryValue = str(sqrtValue)
                totalDisplay['text']= memoryValue
                inputDisplay.delete(0,END)
                print("*****************") 
                memoryOperator =""       
            
            elif (lastValue != "" and memoryValue != "" and memoryOperator == ""):
                sqrtValue = math.sqrt(float(lastValue))
                memoryValue = str(sqrtValue)
                totalDisplay['text']= memoryValue
                inputDisplay.delete(0,END)
                print("*****************") 
                lastValue =""
            
            elif (lastValue != "" and memoryValue != "" and memoryOperator != ""):
                sqrtValue = math.sqrt(float(lastValue))
                if(memoryOperator == "+"): 
                    sqrtValue = float(memoryValue) + float( sqrtValue)
                    sqrtValue=str(sqrtValue)
                    totalDisplay['text']= memoryValue =memoryValue+memoryOperator+"("+"√¯"+lastValue+")"+"="+sqrtValue
                if(memoryOperator == "-"): 
                    sqrtValue = float(memoryValue) - float( sqrtValue)
                    sqrtValue=str(sqrtValue)
                    totalDisplay['text']= memoryValue =memoryValue+memoryOperator+"("+"√¯"+lastValue+")"+"="+sqrtValue   
                if(memoryOperator == "x"): 
                    sqrtValue = float(memoryValue) * float( sqrtValue)
                    sqrtValue=str(sqrtValue)
                    totalDisplay['text']= memoryValue =memoryValue+memoryOperator+"("+"√¯"+lastValue+")"+"="+sqrtValue  
                if(memoryOperator == "/"): 
                    sqrtValue = float(memoryValue) / float( sqrtValue)
                    sqrtValue=str(sqrtValue)
                    totalDisplay['text']= memoryValue =memoryValue+memoryOperator+"("+"√¯"+lastValue+")"+"="+sqrtValue  

                if (memoryOperator == "%"):
                    print("% kare")
                    sqrtValue = (float(memoryValue)/100) * float(sqrtValue)
                    sqrtValue=str(sqrtValue)
                    totalDisplay['text']=memoryValue+memoryOperator+"("+"√¯"+lastValue+")"+"="+sqrtValue

                inputDisplay.delete(0,END) 
                lastValue = ""
                memoryOperator=""
                memoryValue = sqrtValue
            #***********************exponentiation*************************** 
        if(btnValue=="x2"):
            if (lastValue != "" and memoryValue == "" and  memoryOperator == ""):
                takeSquare= float(lastValue)*float(lastValue)
                takeSquare=str(takeSquare)
                totalDisplay['text'] = takeSquare
                inputDisplay.delete(0,END) 
                lastValue = ""
                memoryValue = takeSquare
            
            elif(lastValue == "" and memoryValue != "" and  memoryOperator == ""):
                takeSquare=float(memoryValue)*float(memoryValue)
                takeSquare=str(takeSquare)
                totalDisplay['text'] = takeSquare
                inputDisplay.delete(0,END)
                lastValue = ""
                memoryValue = takeSquare
            elif(lastValue == "" and memoryValue != "" and  memoryOperator != ""):
                takeSquare=float(memoryValue)*float(memoryValue)
                takeSquare=str(takeSquare)
                totalDisplay['text'] = takeSquare
                inputDisplay.delete(0,END)
                memoryOperator = ""
                memoryValue = takeSquare
            
            elif(lastValue != "" and memoryValue != "" and  memoryOperator == ""):
                takeSquare= float(lastValue)*float(lastValue)
                takeSquare=str(takeSquare)
                totalDisplay['text'] = takeSquare
                inputDisplay.delete(0,END)
                lastValue = ""
                memoryValue = takeSquare
        
            elif(lastValue != ""and memoryValue != "" and  memoryOperator != ""): 
                takeSquare= float(lastValue)*float(lastValue)
                if (memoryOperator == "+"):
                  takeSquare= float(memoryValue) + float(takeSquare)
                  takeSquare= str(takeSquare)
                  totalDisplay['text'] =memoryValue+memoryOperator+"("+lastValue+"x"+lastValue+")"+"="+takeSquare
                if (memoryOperator == "-"):
                  takeSquare= float(memoryValue) - float(takeSquare)
                  takeSquare= str(takeSquare)
                  totalDisplay['text'] =memoryValue+memoryOperator+"("+lastValue+"x"+lastValue+")"+"="+takeSquare
                if (memoryOperator == "x"): 
                  takeSquare= float(memoryValue) * float(takeSquare)
                  takeSquare= str(takeSquare)
                  totalDisplay['text'] =memoryValue+memoryOperator+"("+lastValue+"x"+lastValue+")"+"="+takeSquare
                if (memoryOperator == "/"):
                  takeSquare= float(memoryValue) / float(takeSquare)
                  takeSquare= str(takeSquare)
                  totalDisplay['text'] =memoryValue+memoryOperator+"("+lastValue+"x"+lastValue+")"+"="+takeSquare

                elif (memoryOperator == "%"):
                    takeSquare= (float(memoryValue)/100) * float(takeSquare)
                    takeSquare=str(takeSquare)
                    totalDisplay['text'] =memoryValue+memoryOperator+"("+lastValue+"x"+lastValue+")"+"="+takeSquare
                    
                inputDisplay.delete(0,END)
                lastValue = ""
                memoryOperator=""
                memoryValue = takeSquare
            #***********************percent**********************************
        if(btnValue=="%"):  
            print("percent calculate")
            if(lastValue!=""and memoryOperator==""and memoryValue==""):
                print("yüzde :01")
                totalDisplay['text'] = lastValue+btnValue
                inputDisplay.delete(0,END)
                memoryValue=lastValue
                lastValue = ""
                memoryOperator=btnValue
                
            elif (memoryValue!=""and memoryOperator!="%"and lastValue==""):
                print("yüzde :02")
                memoryOperator=btnValue
                totalDisplay['text'] = memoryValue+memoryOperator
                btnValue=""
            
#*****************************************************************************
#***********************************inputClear********************************
#***************************************************************************** 
def inputClear(btnValue):
        global lastValue
        global memoryValue
        global memoryOperator
        
        if(btnValue=="ON/C"):
             print("inputClear 01-->Value :",btnValue)
             lastValue=""
             memoryOperator=""
             memoryValue=""
             print("inputClear-->Value :",lastValue)
             inputDisplay.delete(0,END)
             totalDisplay['text'] =lastValue

        elif(btnValue=="<--" and lastValue!=""and memoryOperator!="" and memoryValue!=""):
             print("inputClear 02-->Value :",lastValue)
             s=len(inputDisplay.get())
             s=s-1
             inputDisplay.delete(s,END) 
             lastValue=lastValue[:-1]
             totalDisplay['text'] =memoryValue+memoryOperator+lastValue

        elif(btnValue=="<--" and lastValue==""and memoryOperator!="" and memoryValue!=""):
             print("inputClear 03-->Value :",memoryValue)
             print("inputClear 03-->Value :",memoryOperator)
             memoryOperator=""
             totalDisplay['text'] =memoryValue

        elif(btnValue=="<--" and lastValue=="" and memoryOperator=="" and memoryValue!=""):
             print("inputClear 04-->Value :",lastValue)
             s=len(inputDisplay.get())
             s=s-1
             inputDisplay.delete(s,END) 
             memoryValue=memoryValue[:-1]
             totalDisplay['text'] =memoryValue  

        elif(btnValue=="<--"):
             #lastValue=""
             print("inputClear 05-->Value :",lastValue)
             s=len(inputDisplay.get())
             s=s-1
             inputDisplay.delete(s,END) 
             lastValue=lastValue[:-1]
             totalDisplay['text'] =lastValue

#***************************************************************************** 
# **********************************memoryOpretion****************************
#*****************************************************************************                        
def memoryOpreation(btnValue):
    global lastValue
    global memoryValue
    global memoryOperator
    global memory
    print(" memoryOperation -->Value :",btnValue)
           # **********************memory add positive ***************************  
    if(btnValue=="M+"):
        print("*****************") 
        print("lastValue :"+lastValue)
        print("memoryValue :"+memoryValue)
        print("memoryOperator :"+memoryOperator)
        if(btnValue=="M+"and memoryOperator!="" and memoryValue!=""and lastValue!=""):
            print("1111111111111111111111111")
            if(memoryOperator=="+"):
                print("1-2222222222222222222222")
                memoryValue=float(memoryValue)+float(lastValue)
                memoryValue=str(memoryValue)
                memory.append(memoryValue)
                for index in memory:
                    print(index)    
     
            elif(memoryOperator=="-"):
                print("1-3333333333333333333333")
                memoryValue=float(memoryValue)-float(lastValue)
                memoryValue=str(memoryValue)
                memory.append(memoryValue)
                for index in memory:
                    print(index); 
           
            elif(memoryOperator=="x"):
                print("1-44444444444444444444444444444444")
                memoryValue=float(memoryValue)*float(lastValue)
                memoryValue=str(memoryValue)
                memory.append(memoryValue)
                for index in memory: 
                    print(index) 
             
            elif(memoryOperator=="/"):
                print("1-555555555555555555555555555555555555")
                memoryValue=float(memoryValue)/float(lastValue)
                memoryValue=str(memoryValue)
                memory.append(memoryValue)
                for index in memory:
                    print(index)             
     
            elif(memoryOperator=="%"):
                print("1-655555555555555555555555555555555555")
                memoryValue=float(memoryValue)/100*float(lastValue)
                memoryValue=str(memoryValue)
                memory.append(memoryValue)
                for index in memory:
                    print(index)             
        
            totalDisplay['text'] =memoryValue
            inputDisplay.delete(0,END)
            lastValue="" 
            memoryOperator=""
            print("******EXIT********") 
            print("lastValue :",lastValue)
            print("memoryValue :",memoryValue)
            print("memoryOperator :",memoryOperator)
     
        elif(memoryOperator=="" and  memoryValue!=""and lastValue==""):
            print("77777777777777777777777777777777777777")
            memory.append(memoryValue)
            for index in memory:
                print(index)
            totalDisplay['text'] = memoryValue
            inputDisplay.delete(0,END)           
 
        elif(memoryOperator=="" and  memoryValue!=""and lastValue!=""):
            print("66666666666666666666666666666666666666666")
            memory.append(lastValue)
            memoryValue=lastValue
            for index in memory:
                print(index)
            totalDisplay['text'] = memoryValue
            inputDisplay.delete(0,END)                  
            lastValue=""
       
        elif (memoryOperator=="" and  memoryValue=="" and  lastValue!="" ): 
            print("???????????????????????") 
            print("lastValue :"+lastValue)
            print("memoryValue :"+memoryValue)
            print("memoryOperator :"+memoryOperator)
            memory.append(lastValue)
            memoryValue=lastValue
            for index in memory:
                print(index)
            totalDisplay['text'] = memoryValue
            inputDisplay.delete(0,END)   
            lastValue=""
            memoryOperator=""
            print("lastValue :"+lastValue)
            print("memoryValue :"+memoryValue)
           # **********************memory add negative*****************************
    if(btnValue=="M-"):
        print("*****************") 
        print("lastValue :"+lastValue)
        print("memoryValue :"+memoryValue)
        print("memoryOperator :"+memoryOperator)
        if( memoryOperator!="" and memoryValue!=""and lastValue!=""):
            print("1111111111111111111111111")
            if(memoryOperator=="+"):
                print("1-2222222222222222222222")
                memoryValue=-1*(float(memoryValue)+float(lastValue))
                memoryValue=str(memoryValue)
                memory.append(memoryValue)
                for index in memory:
                    print(index)    
     
            elif(memoryOperator=="-"):
                print("1-3333333333333333333333")
                memoryValue=-1*(float(memoryValue)-float(lastValue))
                memoryValue=str(memoryValue)
                memory.append(memoryValue)
                for index in memory:
                    print(index); 
           
            elif(memoryOperator=="x"):
                print("1-44444444444444444444444444444444")
                memoryValue=-1*(float(memoryValue)*float(lastValue))
                memoryValue=str(memoryValue)
                memory.append(memoryValue)
                for index in memory: 
                    print(index) 
             
            elif(memoryOperator=="/"):
                print("1-555555555555555555555555555555555555")
                memoryValue=-1*(float(memoryValue)/float(lastValue))
                memoryValue=str(memoryValue)
                memory.append(memoryValue)
                for index in memory:
                    print(index)             
     
            elif(memoryOperator=="%"):
                print("1-655555555555555555555555555555555555")
                memoryValue=-1*(float(memoryValue)/100*float(lastValue))
                memoryValue=str(memoryValue)
                memory.append(memoryValue)
                for index in memory:
                    print(index)             
        
            totalDisplay['text'] =memoryValue
            inputDisplay.delete(0,END)
            lastValue="" 
            memoryOperator=""
            print("******EXIT********") 
            print("lastValue :",lastValue)
            print("memoryValue :",memoryValue)
            print("memoryOperator :",memoryOperator)
     
        elif(memoryOperator=="" and  memoryValue!=""and lastValue==""):
            print("77777777777777777777777777777777777777")
            memory.append((float(memoryValue))*-1)
            for index in memory:
                print(index)
            totalDisplay['text'] = memoryValue
            inputDisplay.delete(0,END)           
 
        elif(memoryOperator=="" and  memoryValue!=""and lastValue!=""):
            print("66666666666666666666666666666666666666666")
            memory.append(-1*float(lastValue))
            memoryValue=lastValue
            for index in memory:
                print(index)
            totalDisplay['text'] = memoryValue
            inputDisplay.delete(0,END)                  
            lastValue=""
       
        elif (memoryOperator=="" and  memoryValue=="" and  lastValue!="" ): 
            print("???????????????????????") 
            print("lastValue :"+lastValue)
            print("memoryValue :"+memoryValue)
            print("memoryOperator :"+memoryOperator)
            memory.append(-1*float(lastValue))
            memoryValue=lastValue
            for index in memory:
                print(index)
            totalDisplay['text'] = memoryValue
            inputDisplay.delete(0,END)   
            lastValue=""
            memoryOperator=""
            print("lastValue :"+lastValue)
            print("memoryValue :"+memoryValue)

           # **********************memory sum **************************************
    if(btnValue=="MR"):
        memoryAdd=0
        if (len(memory)>0 ):
            for index in memory:
                print(index)
                memoryAdd += float(index)
    
            memoryValue=memoryAdd; 
            memoryValue=str(memoryValue)
        totalDisplay['text']  = "MR="+ memoryValue 
        memoryAdd=""
        lastValue=""
        print("MR sum :"+memoryAdd); 
        print("memoryValue :"+memoryValue) 
        print("memoryOperator :"+memoryOperator)
        print("lastvalue  :"+lastValue)
           # **********************memory clear ************************************
    if(btnValue=="MC"):  
        if (len(memory)>0):
           memory=[]
        totalDisplay['text'] =""; 
        inputDisplay.delete(0,END) 
        memoryValue="" 
        memoryOperator=""
        lastValue=""
        print("*****MEMORY CLEAR***********")
   
#***************************************************************************** 
# ***********************************contoller********************************
#*****************************************************************************         
def btnTextControl(btnValue):
    btnTextNumbersArray=[0,"00",1,2,3,4,5,6,7,8,9,"."] 
    btnTxetOperatorsArray=["+","-","x","/","x2","√¯","%","+/-","="] 
    btnTextClearArray=["<--","ON/C","OFF"] 
    btnTextMemoryArray=["M+","M-","MC","MR"]

    if(btnValue in btnTextNumbersArray):
        print(btnValue)
        inputWrite(btnValue)

    if(btnValue in btnTxetOperatorsArray):
        print(btnValue)
        calculate(btnValue)

    if(btnValue in btnTextClearArray):
        print(btnValue)
        inputClear(btnValue)

    if(btnValue in btnTextMemoryArray):
        print(btnValue)
        memoryOpreation(btnValue)
#*****************************************************************************
# ************************************VIEW************************************
# **************************************************************************** 
window = Tk()
window.geometry("520x320+200+200")
totalDisplay = Label(bg="gray",fg="white",font="verdana 8 bold",justify=RIGHT,anchor='e')
totalDisplay.place(x=20,y=20,width=480,height=19)
window.title("Calculator")
inputDisplay = Entry(bg="black", fg="white",
              font="verdana 14 bold",justify=['right'])
inputDisplay.place(x=20, y=40, width=480, height=35)
btnTextIndex = 0
btnName = []
btnText = ["OFF", 7, 8, 9, "<--", "x2", "MC", "%", 4, 5, 6, "-", "/", "MR",
      "+/-", 1, 2, 3, "+", "x", "M-", "ON/C", 0, "00", ".", "√¯", "=", "M+"]
for i in range(85, 236, 50):
        for j in range(7):
            btnName.append(Button(text=str(btnText[btnTextIndex]), bg="black", fg="white",font="verdana 12 bold", command=lambda btnValue=btnText[btnTextIndex]: btnTextControl(btnValue)))
            btnName[btnTextIndex].place(x=20+j*70, y=i, width=60, height=40)
            btnTextIndex += 1
window.mainloop()
