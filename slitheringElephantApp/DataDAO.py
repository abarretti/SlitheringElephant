import sqlite3

class DataDAO:
    def __init__(self, dBName):
        self.conn = sqlite3.connect(dBName)
        self.cur = self.conn.cursor()

    def getPayload(self):
        self.cur.execute('SELECT * FROM TestTable')
        fieldNames = [member[0] for member in self.cur.description]
        results = self.cur.fetchall()
        return self.getFieldRecordDictionary(fieldNames, results)

    def getFieldNames(self, tableName):
        fieldList = []
        fieldNames = self.cur.execute('PRAGMA TABLE_INFO({})'.format(tableName))
        for field in fieldNames:
            fieldList.append(field[1])
        return fieldList

    def getFieldRecordDictionary(self, fieldNames, records):
        recordsList = []
        for row in records:
            recordDict = {}
            for item in range(0,len(row)):
                recordDict[fieldNames[item]] = row[item]
            recordsList.append(recordDict)
        return recordsList
