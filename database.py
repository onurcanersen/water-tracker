import sqlite3 as dbapi2
import json
import datetime

from log import Log

class Database:
    def __init__(self, database_file):
        self.database_file = database_file
    
    def create_log(self, amount):
        with dbapi2.connect(self.database_file) as connection:
            cursor = connection.cursor()
            query = "INSERT INTO LOG (AMOUNT) VALUES (?)"
            cursor.execute(query, (amount, ))
            connection.commit()
    
    def delete_log(self, id):
        with dbapi2.connect(self.database_file) as connection:
            cursor = connection.cursor()
            query = "DELETE FROM LOG WHERE (ID = ?)"
            cursor.execute(query, (id, ))
            connection.commit()

    def get_logs(self):
        logs = []
        with dbapi2.connect(self.database_file) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, DATE, AMOUNT FROM LOG ORDER BY DATE DESC"
            cursor.execute(query)
            for id, date, amount in cursor:
                logs.append(Log(id, date, amount))
        return logs

    def get_todays_logs(self):
        logs = []
        with dbapi2.connect(self.database_file) as connection:
            cursor = connection.cursor()
            query = "SELECT ID, DATE, AMOUNT FROM LOG WHERE (DATE(DATE) = ?) ORDER BY DATE DESC"
            today = datetime.datetime.now().date()
            cursor.execute(query, (today, ))
            for id, date, amount in cursor:
                logs.append(Log(id, date, amount))
        return logs

    def get_todays_total(self):
        with dbapi2.connect(self.database_file) as connection:
            cursor = connection.cursor()
            query = "SELECT SUM(AMOUNT) FROM LOG WHERE (DATE(DATE) = ?)"
            today = datetime.datetime.now().date()
            cursor.execute(query, (today, ))
            sum = cursor.fetchone()[0]
            return sum

    def get_dates_amounts(self):
        dates = []
        amounts = []
        with dbapi2.connect(self.database_file) as connection:
            cursor = connection.cursor()
            query = "SELECT DATE(DATE), SUM(AMOUNT) FROM LOG GROUP BY DATE(DATE)"
            cursor.execute(query)
            for date, amount in cursor:
                dates.append(date)
                amounts.append(amount)
        return json.dumps(dates), json.dumps(amounts)

    def update_target(self, target):
        with dbapi2.connect(self.database_file) as connection:
            cursor = connection.cursor()
            query = "UPDATE SETTINGS SET TARGET = ?"
            cursor.execute(query, (target, ))
            connection.commit()
    
    def get_target(self):
        with dbapi2.connect(self.database_file) as connection:
            cursor = connection.cursor()
            query = "SELECT TARGET FROM SETTINGS"
            cursor.execute(query)
            target = cursor.fetchone()[0]
            return target