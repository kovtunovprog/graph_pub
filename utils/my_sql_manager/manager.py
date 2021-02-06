

from mysql.connector import MySQLConnection, Error


# TODO: Допиши сюда что надо и используй в своих целях
class MySqlManager(object):
    def __init__(self, mysql_conn_conf):
        self.conn = MySQLConnection(**mysql_conn_conf)

    def query_fetchone(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        return row

    def query_fetchall(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        return rows
