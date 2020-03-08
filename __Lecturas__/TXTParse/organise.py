import os

def open_file(filename):
    with open(filename,mode="r+",encoding="UTF-8") as file:
        M = file.readlines() 
        file.close()
    counter = 0
    for i in M:
        M[counter] = M[counter].replace("«","")
        M[counter] = M[counter].replace("»","")
        M[counter] = M[counter].replace("","")
        M[counter] = M[counter].replace("\n","")
        M[counter] = M[counter].replace("—","")
        M[counter] = M[counter].replace("- ","")
        M[counter] = M[counter].replace("•","")
        if "-----------------------------------------------------" in M[counter]:
            M[counter] = "\n"
        counter += 1
    
    s = ""
    for n in M:
        s = s + n 
    
    s = s.split()
    
    with open(filename,mode="w+",encoding="UTF-8") as file:
        file.seek(0)
        file.truncate()
        file.seek(0)
        counter = 0
        temp = ""
        for l in s:
            temp = temp + l + " "
            if (counter % 20 == 0) and (counter != 0):
                file.write(temp + "\n")
                temp = ""
            counter += 1
        
        file.close()
                        

def runner():
    txt = os.listdir("txt/")
    for i in txt:
        open_file(i)


if __name__ == "__main__":
    # runner()
    open_file("txt/CostAnalysis-Cap9_OCR.txt")
