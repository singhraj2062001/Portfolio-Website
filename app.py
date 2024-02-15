from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


app = Flask(__name__)
app.secret_key = '**********'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/datasets')
def datasets():
    return render_template('datasets.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Process the form data (e.g., save to database, send email, etc.)
        # Example: send an email
        # Replace the following code with your email sending logic

        sender_email = "hint4success@gmail.com"
        receiver_email = "singhraj2062001@gmail.com"
        password = "nskzadyxlxqosulz"

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = "New Message from Contact Form"

        body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())

        # Display success message
        flash('Your message has been sent successfully!', 'success')

        return redirect(url_for('contact'))

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
