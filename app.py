from flask import Flask, render_template, request, jsonify , redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from datetime import date

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    password = db.Column(db.String(20))
    email = db.Column(db.String(30))
    join_date = db.Column(db.DateTime)

@app.route('/')
def index():
    #show the members in the db
    members = Member.query.all()
    return render_template('index.html', members=members)

@app.route('/update', methods=['POST'])
def update_member():
    # get the member id and new data from the form
    member_id = request.form['id']
    member_name = request.form['name']
    member_password = request.form['password']
    member_email = request.form['email']


    # find the member in the db and update their data
    member = Member.query.get(member_id)
    if member_password == "":
        member_password = member.password
    member.name = member_name
    member.password = member_password
    member.email = member_email

    # commit the changes to the db
    db.session.commit()

    # redirect to the home page
    return redirect('/')

@app.route('/search', methods=['GET', 'POST'])
def search_member():
    if request.method == 'POST':
        # get the search query from the form
        search_query = request.form['search_query']

        # search for members in the db that match the query
        members = Member.query.filter(or_(Member.name.like(f'%{search_query}%'), Member.email.like(f'%{search_query}%'))).all()

        # render the search results page with the matching members
        return render_template('search.html', members=members)

    # if the request method is GET, render the search page
    return render_template('search.html')

@app.route('/add', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        # get the new member data from the form
        member_name = request.form['name']
        member_password = request.form['password']
        member_email = request.form['email']

        # create a new member object and add it to the db
        new_member = Member(name=member_name, password=member_password, email=member_email, join_date=date.today())
        db.session.add(new_member)
        db.session.commit()

        # scale the IDs of the members
        scale_id()

        # redirect to the home page
        return redirect('/')

    # if the request method is GET, render the add member page
    return render_template('add_member.html')

@app.route('/delete' , methods=['POST'])
def delete_member():
    # find the member in the db and delete them
    id = request.form['id']
    member = Member.query.get(id)
    db.session.delete(member)
    db.session.commit()
    
    # scale the IDs of the members
    scale_id()

    # redirect to the home page
    return redirect('/')

def scale_id():
    #get all the members from the database
    members = Member.query.all()

        #update the IDs of the members
    for i, member in enumerate(members):
        member.id = i + 1

        # commit the changes to the database
    db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)