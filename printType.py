def printType(x):
    if isinstance(x,(int,long,float,complex)):
        print "It's a number"
        return
    if isinstance(x, str):
        print "It's a string"
        return
    if isinstance(x,list):
        print "It's a list"
        return
    if isinstance(x,dict):
        print "It's a dictionary"
        return
    if isinstance(x,tuple):
        print "It's a tuple"
        return
