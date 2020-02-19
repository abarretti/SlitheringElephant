import DataModel
import DataDAO
import JSONFunctions

class DataController:

    def __init__(self, dataModel, keyModel):
        self.dataModel = dataModel
        self.keyModel = keyModel

    def getData(self):
        if self.keyModel.isKey():
            return JSONFunctions.convertSQLResultsToJSONString(self.dataModel.getData())
        else:
            return 'Access Denied'
