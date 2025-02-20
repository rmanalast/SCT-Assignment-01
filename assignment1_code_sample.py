import os
import pymysql
from urllib.request import urlopen

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

db_config = {
    'host': 'mydatabase.com',
    'user': 'admin',
    'password': 'secret123'
}

def get_user_input():
    user_input = input('Enter your name: ')
    return user_input

def send_email(to, subject, body):
    # OWASP A1: Injection (Command Injection)
    # Using os.system() to execute shell commands allows attackers to inject malicious shell commands.
    # If 'body' contains a malicious payload, it could execute arbitrary commands.
    # Mitigation: Use a secure email library instead of executing shell commands.
    
    msg = MIMEMultipart()
    msg['From'] = 'noreply@example.com'
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(os.getenv('SMTP_USER'), os.getenv('SMTP_PASS'))  # Use environment variables
            text = msg.as_string()
            server.sendmail('noreply@example.com', to, text)
    except Exception as e:
        print(f"Error sending email: {e}")

def get_data():
    url = 'http://insecure-api.com/get-data'
    data = urlopen(url).read().decode()
    return data

def save_to_db(data):
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
