# Import the module
import subprocess
import settings as directory
import csv

tool = 'curl'
target = directory.url['url']
from_='From={}'.format(directory.my_phone['phone'])
body = 'Body={}'.format(directory.messages['real'])
creds = directory.creds['real']
numbers = []
with open('list.csv') as f:
    reader = csv.reader(f)
    for r in reader:
        numbers.append(r[4])

for i in numbers:
    num_str = 'To={}'.format(i)
    request = [
            tool,
            target,
            '-X',
            'POST',
            '--data-urlencode',
            num_str,
            '--data-urlencode',
            from_,
            '--data-urlencode',
            body,
            '-u',
            creds
            ]

    # Set up the echo command and direct the output to a pipe
    message = subprocess.Popen(request, stdout=subprocess.PIPE)

    # Run the command
    output = message.communicate()

    print(output)

