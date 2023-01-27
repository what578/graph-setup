import errorRaiser


class Column:
    value           = None
    name            = None

    def __init__(self,value,name):
        self.setValue(value)
        self.setName(name)

    #setters
    def setValue(self,value):
        errorRaiser.typeError("Column.setValue()",value,type(5))
        self.value = value
    def setName(self,name):
        errorRaiser.typeError("Column.setName()",name,type("t"))
        self.name  = name








if __name__ == "__main__":
    co      = Column(5,"cats")
    co.setName(5)
