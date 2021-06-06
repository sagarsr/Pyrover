import pymysql as ps
mydb=ps.connect(host="54.237.151.189",port=3306,user="balu",passwd="balu123",db="samp")
doQuery(mydb)
ch=mydb.cursor();
sql='INSERT INTO simp(v1,v2) VALUES (213,125);'
ch.execute(sql)
mydb.commit()

