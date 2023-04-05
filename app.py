from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app =Flask(__name__)
db_local = 'expenses.db'

@app.route('/')
@app.route('/home')
def home_page():
    expense_data = query_expense_details()
    dataObject = {
        "Fuel":0,
        "Hotel":0,
        "Shopping":0,
        "Utility":0,
        "Clothing":0,
        "Entertainment":0,
        "Other":0
    }
    total = 0
    for tup in expense_data:
        total+=tup[1]
        if tup[2]=="Fuel":
            dataObject["Fuel"]+=tup[1]
        if tup[2]=="Hotel":
            dataObject["Hotel"]+=tup[1]
        if tup[2]=="Shopping":
            dataObject["Shopping"]+=tup[1]
        if tup[2]=="Utility":
            dataObject["Utility"]+=tup[1]
        if tup[2]=="Clothing":
            dataObject["Clothing"]+=tup[1]
        if tup[2]=="Entertainment":
            dataObject["Entertainment"]+=tup[1]
        if tup[2]=="Other":
            dataObject["Other"]+=tup[1]

    labelArray = []

    dataObjectPercentageArray = []
    for k,v in dataObject.items():
        if v>0:
            p = round(v/total * 100,2)
        else:
            p=0
        if(int(p)!=0):
            dataObjectPercentageArray.append(p)
            labelArray.append(str(k))

    # setcount=1
    # count=0
   

    return render_template('home.html', expense_data=expense_data, dataObjectPercentageArray=dataObjectPercentageArray,labelArray=labelArray)



@app.route('/', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'GET':
        pass
    else:
        expense_details=(
            request.form['exp'],
            request.form['catg'],
            request.form['date'],
            request.form['desc']
        )
        insert_expense(expense_details)
        return redirect(url_for('home_page'))

# _____________________________________________________________editing_____________________________________________________________

# @app.route('/edit_entry')
# def edit_entry():
#     return render_template('edit.html')



# #_____________________________________________________________editing_______________________________________________________________


# _____________________________________________________________deleting_____________________________________________________________
@app.route('/delete/<int:id>')
def delete_entry(id):
   con = sqlite3.connect("expenses.db")
   con.row_factory = sqlite3.Row
   cur = con.cursor()
   id=int(id)
   cur.execute("delete from anlysis where id=?", (id,))
   con.commit()    
   con.close()
   return redirect(url_for('home_page'))  


#_____________________________________________________________deleting_____________________________________________________________

def insert_expense(expense_details):
    conn =sqlite3.connect(db_local)
    c = conn.cursor()
    execute_string = 'INSERT INTO anlysis (exp, catg, date, desc) VALUES (?,?,?,?)'
    c.execute(execute_string, expense_details)
    conn.commit()
    conn.close()


def query_expense_details():
    conn =sqlite3.connect(db_local)
    c = conn.cursor()
    c.execute("""
    SELECT * FROM anlysis
    """)
    expense_data=c.fetchall()
    return expense_data


if __name__ == '__main__':
    app.run()
