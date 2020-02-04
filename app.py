import pymysql.cursors
from flask import Flask, render_template

app = Flask(__name__)

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='dc0758sw',
                             password='*********',
                             db='dc0758sw_university',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Select all Students
        sql = "SELECT * FROM Student"
        #sql = "SELECT * from Student where FIrstName = " + "'" + studentSearch + "'"
        
        # execute the SQL command
        cursor.execute(sql)
        
        # get the results
        @app.route('/')
        def index():
            return render_template('index.html')
        
        
        @app.route('/uni')
        def uni():
            #return 'Hello, Perla'
            row = "<br>"
            for result in cursor:
                row += str(result)
                row +="<br>"
            return (row)
        
      
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        # connection.commit()
            
        if __name__ == '__main__':
            app.run(debug=True, host='127.0.0.1', port='1758')
        

finally:
    connection.close()
