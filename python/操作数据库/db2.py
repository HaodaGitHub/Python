import pymysql

# �����ݿ�����
db = pymysql.connect("127.0.0.1", "root", "123456", "mytestdb",charset="utf8" )

# ʹ��cursor()������ȡ�����α�
cursor = db.cursor()

# SQL �������
sql = "INSERT INTO EMPLOYEE(name,  \
          AGE, SEX, INCOME)  \
         VALUES ('%s',  '%d', '%s', '%d')" % \
      ('����2',  21, 'F', 2000)
try:
    # ִ��sql���
    cursor.execute(sql)
    # �ύ�����ݿ�ִ��
    db.commit()
except Exception as e:
    print( e )
    # �������������ع�
    db.rollback()

# �ر����ݿ�����
db.close()
