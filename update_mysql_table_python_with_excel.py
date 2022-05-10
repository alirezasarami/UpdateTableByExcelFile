                                                                                   
import mysql.connector

#CONNECT TO DB
mydb = mysql.connector.connect(
  host="localhost",
  user="db_name",
  password="password",
  database = "user",
)

#OPEN EXCEL FILE WITH .XLSX FORMAT
csv_file = pandas.ExcelFile('solomon_carpet.xlsx')
df = csv_file.parse(csv_file.sheet_names[0])

#CONVERT EXCEL DATA TO DICT 
dic = df.to_dict()

#GET NUMBER OF ROW DATA
rang = len(dic['column name'])


id_ = dic['column 1']
procode = dic['column 2']

#UPDATE PROCODE OF TABLE
for counter in range(rang):
    mycursor = mydb.cursor()
    pro = procode[counter]
    id = id_[counter]
    sql = f"UPDATE TABLE SET procode = {pro} WHERE id = {id}"
    mycursor.execute(sql)
    mydb.commit()

