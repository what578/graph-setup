import errorRaiser
import column



class Graph:
    rows        = None
    columns     = None
    graphName   = None


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








if __name__ == "__main__":
    rows= 20
    graphName = "number of animals"
    catsCol = column.Column(10,"Cats")
    dogCol  = column.Column(20,"Dogs")
    wormCol = column.Column(15,"Worms")
    allCol  = [catsCol,dogCol,wormCol]
    g = Graph(rows,graphName,allCol)
