from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from flask_mail import Mail, Message

app = Flask(__name__, instance_relative_config=True)

app.config["SECRET_KEY"] = "myapplication123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = os.environ.get("RECEIVER-EMAIL")
app.config["MAIL_PASSWORD"] = os.environ.get("GOOGLE-EMAIL-PASSWORD")

db = SQLAlchemy(app=app)

mail = Mail(app=app)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.String(80))
    occupation = db.Column(db.String(80)) 

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["first_name"].capitalize()
        last_name = request.form["last_name"].capitalize()
        email = request.form["email"]
        date = request.form["date"]
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        occupation = request.form["occupation"].capitalize()
        
        # Add the new form entry to the database
        new_entry = Form(first_name=first_name, last_name=last_name, 
                         email=email, date=date_obj, occupation=occupation)
        db.session.add(new_entry)
        db.session.commit()

        # sending mail
        message_body = f'''Thanks for your submission, {first_name}.\
            Your details are as following:-\n\
                1. First Name: {first_name}\n
                2. Last Name: {last_name}\n
                3. Occupation: {occupation}'''
        
        message = Message(subject=f"New Form Submission - {date_obj}",
                          sender=app.config["MAIL_USERNAME"],
                          recipients=[email],
                          body=message_body)
        
        mail.send(message=message)

        # Giving dynamic input to html page with "flash"
        flash(f"{first_name} your form was submitted successfully !")
    
    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        # all db instance will be generated in root directory in an "instance" folder
        db.create_all()
        app.run(debug=True, port=5001)
