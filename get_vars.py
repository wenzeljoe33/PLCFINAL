
import imp

def getVarFromFile(filename):
    f = open(filename)
    global data
    data = imp.load_source('data', '', f)
    f.close()

# path to "config" file
getVarFromFile('/Users/wenzeljoe/Desktop/Desktop/GSU/PLC/final/test.txt')
print (data.var1)
print (data.var2)
print (data.var3)