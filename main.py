import pymysql as pm
import pymysql.cursors

conn = pm.connect(host='localhost', user='root', password='rootroot')

# create_database = 'create database test' # sql 구문 입력
# conn.cursor().execute(create_database)

cursor = conn.cursor(pymysql.cursors.DictCursor)  # 데이터를 정리해서 보여주기 위해 사용
cursor.execute('use test;')

# insert_sql = 'insert into test_table values(1, "Java")'
# cursor.execute(insert_sql)

# insert_sql = 'insert into test_table(name) values("Python")'
# cursor.execute(insert_sql)

select_sql = 'select * from test_table;'
cursor.execute(select_sql)
result = cursor.fetchall()  # 모든 데이터 담으라는 명령어
print(result)

# update_sql = 'update test_table set name = "HTML"' + 'where name = "Java"'
# cursor.execute(update_sql)

# delete_sql = 'delete from test_table where id = 2'
# cursor.execute(delete_sql)

# delete_database = 'DROP DATABASE test2'
# cursor.execute(delete_database)

conn.commit()
conn.close()
