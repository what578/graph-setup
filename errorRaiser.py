



def typeError(method,value,propValueType):
    if type(value) != propValueType:
        raise TypeError("Invalid value ,%s was given value %s, which is type %s, should be %s"%(method,value,type(value),propValueType))
