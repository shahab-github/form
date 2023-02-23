import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="python",
  password="password"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")

##########################################################
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="python",
  password="password",
  database="myusers"
)

mycursor = mydb.cursor()

sql = "INSERT INTO users "
val = ("John", "Highway", "21", "admin@gmail.com")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
