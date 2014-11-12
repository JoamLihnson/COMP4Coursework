from PyQt4.QtSql import *
from PyQt4.QCore import *



class SQLConnection:
    def __init_(self, path):
        self.path = path
        self.db = None

    def open_database(self):
        if self.db:
            self.close_database()
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.path)
        ok = self.db.open()
        return ok
        
    def close_database(self):
        self.db.close()
        QSqlDatabase.removeDatabase("conn")

    def closeEvent(self,event):
        self.close_database()

    def find_products_by_number(self):
        pass
