search, replace, input, output, build = "Harvey", "****", "abc.txt", "new.txt", ""
for x in open(input, "r").read(): build += x

def findWord(message, search, replace):
        newWord, length, i = "", len(search), 0
        while(i  < len(message)): 
            tmpWord = ""
            if((i + length) <= len(message)): tmpWord = build[i : i+length]
            if(tmpWord == search):
                newWord = newWord + replace
                i = i + len(search)-1
            else: newWord = newWord + build[i : i+1]
            i += 1
        return newWord
open(output, "a").write(findWord(build, search, replace))
