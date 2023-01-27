import errorRaiser
import column
import numpy



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
        maxValue = self.maxValue()
        #multiply this by each row to get value scale
        rowValue = maxValue/self.rows
        startRows = []
        largestStr = self.largestRowString(rowValue)
        bottomRow= self.createBottomRow(largestStr)
        bottomLine = " "*largestStr +   " |"+"_" * (len(bottomRow) + 4)
        startRows.append(bottomRow)
        startRows.append(bottomLine)
        for row in range(1,self.rows+1):
            currentRowValue = int(row*rowValue)
            initalRow = f"{currentRowValue}"
            dif = largestStr - len(initalRow)
            initalRow += " " * dif + " |"
            for col in self.columns:
                initalRow += " "
                if currentRowValue <= col.value:
                    initalRow +="[]"
                else:
                    initalRow +="  "

            startRows.append(initalRow)
        emptyRow = ""
        startRows.append(emptyRow)
        startRows.append(self.createTitleRow(bottomRow))

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
    def createBottomRow(self,largestString):
        space = "  "
        bottomRow = " " * (largestString) + " "
        for x in range(len(self.columns)):
            bottomRow += space + str(x+1)
        return bottomRow
    def createTitleRow(self,bottomRow):
        titleRow = " " * int(((len(bottomRow)/2)))
        return titleRow + self.graphName
    def printGraph(self):
        for row in numpy.flip(self.graph):
            print(row)




if __name__ == "__main__":
    rows= 20
    graphName = "number of animals"
    catsCol = column.Column(20,"Cats")
    dogCol  = column.Column(15,"Dogs")
    wormCol = column.Column(12,"Worms")
    allCol  = [catsCol,dogCol,wormCol]
    g = Graph(rows,graphName,allCol)
    g.createGraph()
    g.printGraph()
