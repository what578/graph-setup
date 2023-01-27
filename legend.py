import column
import numpy
import errorRaiser


class Legend:
    columns         = None
    legend          = None
    def __init__(self,columns):
        self.setColumns(columns)
    def setColumns(self,columns):
        errorRaiser.typeError("setColumns",columns,type([4]))
        if len(columns) == 0:
            raise Valuerror("invalid number of columns")
        for x in columns:
            errorRaiser.typeError("setColumns",x,type(column.Column(5,"t")))
            self.columns = columns
    def createLegend(self):
        largestStr = self.largestStr()
        legend     = []
        legend.append(self.createTopofLegend(largestStr))
        legend = self.createCoreOfLegend(legend,largestStr)
        legend.append(self.creatBotOfLegend(largestStr))
        self.legend=legend
    def createTopofLegend(self,largestStr):
        return " "+ "_" * (largestStr + 5)
    def createCoreOfLegend(self,legendArr,largestStr):
        legend = legendArr
        rowCount = 1
        for col in self.columns:
            dif = largestStr - len(col.name)
            row ="|" + col.name
            row += " " * dif
            row += " = " +f"{rowCount} |"
            rowCount += 1
            legend.append(row)
        return legend
    def creatBotOfLegend(self,largestStr):
        return "|" + "_" * largestStr + "_____|"

    def largestStr(self):
        largestStr = 0
        for col in self.columns:
            if len(col.name) > largestStr:
                largestStr = len(col.name)
        return largestStr
    def printLegend(self):
        if self.legend == None:
            raise ValueError("NoneType cannot be printed")
        for row in self.legend:
            print(row)

if __name__ == "__main__":
    catsCol = column.Column(20,"Cats")
    dogCol  = column.Column(15,"Dogs")
    wormCol = column.Column(12,"Worm")
    allCol  = [catsCol,dogCol,wormCol]
    l = Legend(allCol)
    l.createLegend()
    l.printLegend()
