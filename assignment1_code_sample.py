import os
import pymysql
from urllib.request import urlopen

# OWASP A02: Cryptographic Failures - CM
# Sensitive data exposure
db_config = {
    'host': 'https://mydatabase.com', 
    # OWASP A05: Security Misconfiguration - CM
    # URL incomplete should be a proper secured host/website ex. https://mydatabase.com
    # re-configure the host site to https://mydatabase.com for secured hosting
    'user': 'admin',
    'password': 'secret123'
}

def get_user_input():
    user_input = input('Enter your name: ')
    return user_input

def send_email(to, subject, body):
    os.system(f'echo {body} | mail -s "{subject}" {to}')

def get_data():
    url = 'https://insecure-api.com/get-data' 
    # OWASP A05: Security Misconfiguration - CM
    # URLs should use https to have the page more secured
    # changed the url to 'https'
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
