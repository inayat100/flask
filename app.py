from flask import Flask,render_template,request,redirect
from  flask_sqlalchemy import SQLAlchemy
from  flask_migrate import Migrate #flask db init flask db migrate  flask db upgrade





app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
mig = Migrate(app,db)

class student(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(20),nullable=True)
    last_name = db.Column(db.String(20),nullable=True)
    father = db.Column(db.String(40),nullable=True)
    mother = db.Column(db.String(40),nullable=True)
    courses = db.Column(db.String(20),nullable=True)
    gender = db.Column(db.String(10),nullable=True)
    address = db.Column(db.String(50),nullable=True)

@app.route("/",methods=['GET','POST'])
def hello_world():
    if request.method == "POST":
        fname = request.form['fname']
        lname = request.form['lname']
        father = request.form['father']
        mother = request.form['mother']
        courses = request.form['courses']
        sex = request.form['gn']
        address = request.form['address']
        stu = student(first_name=fname,last_name=lname,father=father,mother=mother,courses=courses,gender=sex,address=address)
        db.session.add(stu)
        db.session.commit()
    return render_template('home.html')

@app.route("/show")
def hello_world2():
    tt = student.query.all()
    return render_template('show.html',data=tt)

@app.route("/delete/<int:sno>")
def hello_world3(sno):
    tt1 = student.query.get(sno)
    db.session.delete(tt1)
    db.session.commit()
    return redirect('/show')
@app.route("/update/<int:sno>",methods=['GET','POST'])
def hello_world4(sno):
    tt = student.query.get(sno)
    if request.method == "POST":
        fname = request.form['fname']
        lname = request.form['lname']
        father = request.form['father']
        mother = request.form['mother']
        courses = request.form['courses']
        sex = request.form['gn']
        address = request.form['address']
        tt.first_name=fname
        tt.last_name=lname
        tt.father=father
        tt.mother=mother
        tt.gender=sex
        tt.courses=courses
        tt.address=address
        db.session.add(tt)
        db.session.commit()
        return redirect('/show')
    return render_template('update.html',data=tt)
if __name__ == '__main__':
    app.run(debug=True)