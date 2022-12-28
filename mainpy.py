def spacecounter(string1):
    count = 0
    for i in range(0, len(string1)):
        if string1[i] == " ":
            count +=1
    return count
def changesRE(num1,num2):
    if(num1 >= num2):
        return num1 - num2
    else:
        return num2 - num1

def Nofletter(spaces,string_1):
    if(string_1>= spaces):
        return string_1 - spaces
    else:
        return spaces - string_1


def fileOpen(filename1,filename2):
    try:
        file_1 = open(f"{filename1}")
        file_2 = open(f"{filename2}")
        file1 = file_1.read()
        file2 = file_2.read()
        nowords1 = len(file1)
        nowords2 = len(file2)
        nospace1 = spacecounter(file1)
        nospace2 = spacecounter(file2)

        total_letter_file1 = Nofletter(nospace1,nowords1)
        total_letter_file2 = Nofletter(nospace2,nowords2)

        print(file1)
        print("LETTERS in file-1 :",total_letter_file1)
        print("\n")
        print(file2)
        print("LETTERS in file-2 :",total_letter_file2)
        print("\n")
        print("\t\tCHANGES")
        print("LETTERS :",changesRE(total_letter_file1,total_letter_file2))
        print("SPACES :",changesRE(nospace1,nospace2))

    except:
        print(FileNotFoundError)
    finally:
        pass
fileOpen("1.txt","2.txt")