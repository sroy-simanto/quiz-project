import mysql.connector as connector

class DB:
    def __init__(self):
        self.con = connector.connect(host='localhost', 
                                     password='yourdbpassword', 
                                     user='root',
                                     database='quizgame')
        query = 'create table if not exists questions(id INT AUTO_INCREMENT PRIMARY KEY,question varchar(200), options varchar(200), answer varchar(200))'
        cur = self.con.cursor()
        cur.execute(query)
        print("Created")

    #Insert
    def insert_qua(self, question, options, answer):
        query = "insert into questions(question,options,answer) values({},'{}','{}')".format(
            question, options, answer)
        #print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("questions saved to db")

    #Fetch
    def fetch_qua(self):
        query = "select * from questions"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Id : ", row[0])
            print("Question :", row[1])
            print("Options :", row[2])
            print("Answer : ", row[3])

    #Delete 
    def delete_qua(self, id):
        query = "delete from questions where id= {}".format(id)
        print(query)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("deleted")

    #Update
    def update_qua(self, question, options, answer):
        query = "update questions set question='{}',options='{}' where id={}".format(
            question, options, answer)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")
