import sqlite3
class exam():
    def __init__(self):
        self.con=sqlite3.connect("d:/ui_prj/data.db")
        self.cur=self.con.cursor()

    def creat_table(self):

        self.cur.execute("""
                create table if not exists web (id integer primary key , name , lname ,course , password , lpassword
                """)
        self.con.commit()

    def update_all(self):
        lst=[]
        self.cur.execute("select * from web")
        result = self.cur.fetchall()
        for i in result:
            lst.append(f"{i[0]}-{i[1]}-{i[2]}-dar dore{i[3]}sabt shode")
        return lst


    def insert_record(self,name , lname , course , password ,):
        self.cur.execute("insert into web values (null , ?,?,?,?)",(name , lname , course , password ))
        self.con.commit()

    def login(self,pas):
        self.cur.execute("select pas from web")
        s = self.cur.fetchall()
        for password in s:
            if pas == password:
                return True
            return False
    def delete(self,id):
        self.cur.execute("delete * from web were id = ?", (id))
        self.con.commit()




