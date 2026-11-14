import sqlite3

conn = sqlite3.connect("sqlite.db")

conn.execute('''
        Create table student(
            st_id INT AUTO_INCREMENT PRIMARY KEY,
            st_name VARCHAR(50),
            st_class VARCHAR(10),
            st_email VARCAHR(30)
            ) 
''')

# ins ='''
#     insert into student(st_name,st_class,st_email) VALUES('RAM',12th,'ram@gmail.com')
# '''
# conn.execute(ins)
# conn.commit()

conn.close()