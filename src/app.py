from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='root'
)

app = Flask(__name__, template_folder='src-web')
app.secret_key = '8564916c098793bf75b9841fce7d2e6cac23df7154792270390a82a1c798f0ff'

cursor = connection.cursor()

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/presence', methods=['GET', 'POST'])
def presence():
    msg=''
    if request.method == 'POST':
        name=request.form['name']
        surname=request.form['surname']
        index_nr=request.form['index_nr']

        cursor.execute("INSERT INTO Students (name, surname, index_nr) VALUES (%s,%s,%s)", (name, surname,index_nr))

        connection.commit()

        msg = 'Dziękuje za obecność!'

    return render_template('index.html', msg=msg) 
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    msg=''
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        cursor.execute('SELECT * FROM Lecturers WHERE login=%s AND password=%s', (login,password))
        record = cursor.fetchone()
        if record:
            session['loggedin'] = True
            session['login'] = record[1]
            return redirect(url_for('table_presence'))
        else:
            msg = 'Nieprawidłowe hasło. Spróbuj ponownie!'
    
    return render_template('login.html', msg=msg)

    

@app.route('/table_presence')
def table_presence():
    
    cursor.execute("SELECT * FROM Students")

    studentDetails = cursor.fetchall()

    return render_template('student_table.html', studentDetails=studentDetails, login=session['login'])
    

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('login', None)
    return redirect(url_for('index'))
        

if __name__ == '__main__':
    app.run(debug=True)