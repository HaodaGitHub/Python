import pymysql

# �����ݿ�����
db = pymysql.connect("localhost", "root", "123456", "mydb",charset='utf8')


# ʹ��cursor()������ȡ�����α�
cursor = db.cursor()

# SQL �������
sql = """INSERT INTO test1(id,num)
         VALUES (2, '����' )"""
try:
    # ִ��sql���
    cursor.execute(sql)
    # �ύ�����ݿ�ִ��
    db.commit()
except Exception as e:
    # �������������ع�
    print(e)
    db.rollback()

# �ر����ݿ�����
db.close()
