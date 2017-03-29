import pymysql


class Database:
    """
    Połączenie z bazą danych. Ważne jest, aby zawsze zamykać połączenie - najlepiej od razu po wykonaniu sql'ki
    (im krócej trwa połączenie tym lepiej - mniejsza szansa, że zostanie zerwane).
    Przykładowe użycie:

    mineDatabase = Database()
    mineDatabase.connect()
    results = mineDatabase.processSqlQuery("Select * From nazwa_tabeli")
    mineDatabase.disconnect()

    gdzie results jest listą z wynikami -> każdy element listy to jeden record z wyniku zapytania
    """

    def __init__(self):
        self.cnx = None

    def connect(self, dbSetting):
        self.cnx = pymysql.connect(user=dbSetting["user"], passwd=dbSetting["password"],
                                   host=dbSetting["host"], port=dbSetting["port"], db=dbSetting["name"])

    def processSqlQuery(self, sqlQuery, update=False):
        cursor = self.cnx.cursor()
        cursor.execute(sqlQuery)
        if update:
            self.cnx.commit()
        records = [record for record in cursor]
        cursor.close()
        return records

    def disconnect(self):
        self.cnx.close()
