# stores in MS Sql
import pyodbc

class MSSqlStore:

    conn: pyodbc.Connection
    cursor: pyodbc.Cursor

    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=pocketworlds;Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()

    def insert(self, url) -> int:
        cur = self.cursor.execute(f"insert urls([url]) values ('{url}')")
        cur = self.cursor.execute(f"select SCOPE_IDENTITY() [id]")
        row = cur.fetchone()
        return int(row.id)

    def get(self, id: int) -> str:
        cur = self.cursor.execute(f"select [url] from urls where id={id}")
        row = cur.fetchone()
        if not row:
            return None
        return row.url

