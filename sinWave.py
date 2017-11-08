print("---SINE/COSINE/TAN WAVES---")
import time,math

def wave(function, leftCharacter, rightCharacter, value, maxCharacters,withNumbers):
    currentFuncValue=round(function(value),2)
    abscurrentFuncValue=int(abs(currentFuncValue)*maxCharacters)
    if currentFuncValue>0:
        if withNumbers:
            endStr=" "*(maxCharacters)+" "+str(currentFuncValue)
        else:
            endStr=" "*maxCharacters
        endStr+=rightCharacter*abscurrentFuncValue
    else:
        endStr=" "*(maxCharacters-abscurrentFuncValue)
        endStr+=leftCharacter*abscurrentFuncValue
        if withNumbers:
            endStr+=str(currentFuncValue)+" "*(maxCharacters-len(str(currentFuncValue)))
        else:
            " "*maxCharacters
    return(endStr)

functionInpt=""
while functionInpt!="1" and functionInpt!="2" and functionInpt!="3":
    functionInpt=input("Functions: sin (1), cos (2), tan (3): ")
    if functionInpt=="1":
        function=math.sin
    elif functionInpt=="2":
        function=math.cos
    elif functionInpt=="3":
        print("TAN DOES NOT REALLY WORK WITH TEXT-WRAPPING")
        input("Press enter to continue..")
        function=math.tan

withNumbers=""
while withNumbers!="0" and withNumbers!="1":
    withNumbers=input("Print with aproximate numbers(1) or without numbers(0): ")
withNumbers=int(withNumbers)

current=0
while True:
    endStr=wave(function,"(",")",current,50,withNumbers)
    print(endStr)
    time.sleep(0.1)
    current+=0.1
