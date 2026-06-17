#TempConvert.py
TempStr = input("Key in Temperature with Symbol:")
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8
    print("After Change Temperature Result {:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("After Change Temperature Result {:.2f}F".format(F))
else:
    print ("Wrong Key Format")
