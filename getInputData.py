# Run this to get the input for the day into the correct day's directory
import os
import requests
from mySession import cookie
day = input('Enter the day whose input is to be fetched: ')
url = f"https://adventofcode.com/2024/day/{day}/input"
response = requests.get(url, 
    cookies=cookie)

if response.status_code == 200:
    html_content = response.text
    data = html_content
else:
    print(response.status_code)
if not os.path.isdir(f'Day{day}'):
    os.mkdir(f'Day{day}')
    with open(f'Day{day}/input.txt', 'w') as f:
        f.write(data)
        print(f'input.txt is added to Day{day}')
else:
    print('File aldready exists')