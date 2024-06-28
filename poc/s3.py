import subprocess
import requests

command1 = subprocess.run('gcloud auth print-access-token', shell=True, capture_output=True, text=True).stdout

headers = {
    'Authorization': 'Bearer ' ,
    'Content-Type': 'application/json',
}

params = {
    'project': 'nonprod-424912',
}

with open('s3.json', 'rb') as f:
    data = f.read()

response = requests.post('https://storage.googleapis.com/storage/v1/b', params=params, headers=headers, data=data)