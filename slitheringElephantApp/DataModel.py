import DataDAO

class DataModel:

    def __init__(self, dao):
        self.dao = dao

    def getData(self):
        results = self.dao.getPayload()
        return results
