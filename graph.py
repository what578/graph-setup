import errorRaiser
import column



class Graph:
    rows        = None
    columns     = None
    graphName   = None
    graph       = None


    def __init__(self,rows,graphName,columns= None):
        self.setRows(rows)
        self.setGraphName(graphName)
        if columns != None:
            self.setColumns(columns)


    def setRows(self,rows):
        errorRaiser.typeError("Graph.setRows",rows,type(5))
        if rows == 0:
            raise Valuerror("invalid number of rows, must be greater then 0 was given %s"%(rows))
        self.rows = rows
    def setColumns(self,columns):
        errorRaiser.typeError("setColumns",columns,type([4]))
        if len(columns) == 0:
            raise Valuerror("invalid number of columns")
        for x in columns:
            errorRaiser.typeError("setColumns",x,type(column.Column(5,"t")))
        self.columns = columns
    def setGraphName(self,name):
        errorRaiser.typeError("setGraphName",name,type("t"))
        self.graphName = name

    def createGraph(self):
        titleRow = ""
        bottomLine= ""
        bottomRow= ""
        maxValue = self.maxValue()
        #multiply this by each row to get value scale
        rowValue = maxValue/self.rows
        startRows = []
        largestStr = self.largestRowString(rowValue)
        for row in range(1,self.rows+1):
            initalRow = f"{int(row*rowValue)}"
            dif = largestStr - len(initalRow)
            initalRow += " " * dif + " |"
            startRows.append(initalRow)
        self.graph = startRows
        return None
    #we will use maxValue to set the value of the rows 
    def maxValue(self):
        max = 0
        for col in self.columns:
            if col.value > max:
                max = col.value
        return max
    #knowing the largest row string helps us set the proper amount of spacing between numbers and the graph
    #ex  notice the differnt amount of " " in the ex largetstRow helps calculate that space
    # 1  |
    # 10 |
    def largestRowString(self,rowValue):
        largestString = 0
        for row in range(1,self.rows+1):
            x = len(str(int(row*rowValue)))
            if x > largestString:
                largestString = x
        return largestString

    def printGraph(self):
        for row in self.graph:
            print(row)




if __name__ == "__main__":
    rows= 25
    graphName = "number of animals"
    catsCol = column.Column(10,"Cats")
    dogCol  = column.Column(20,"Dogs")
    wormCol = column.Column(15,"Worms")
    allCol  = [catsCol,dogCol,wormCol]
    g = Graph(rows,graphName,allCol)
    g.createGraph()
    g.printGraph()
