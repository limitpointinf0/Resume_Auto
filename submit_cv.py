import attach
import csv

with open('list.csv','r') as f:
    reader = csv.reader(f)
    for r in reader:
        print('sending email to:', r[1], r[2])
        attach.send_mail('youremail@email.com',[r[1]], r[2] + ' position at ' + r[3], 'Please see resume.', use_tls=True, username='youremail@email.com', password='password')
        print('email sent to ', r[1])
