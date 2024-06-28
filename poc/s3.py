import subprocess
import requests

command1 = subprocess.run('gcloud auth print-access-token', shell=True, capture_output=True, text=True).stdout

headers = {
    'Authorization': 'Bearer ya29.a0AXooCgtSRmQKHxdGZU_9yzERYC-Q8hwd2N_laICtitIxq8Hxhbe39pf253Tuv24WpBEHsdUJ6_Rx7Pgx8rreckRgYfL2wD9k-GVJ5DSOYVcpPcGY6McWxwoyWCwaxdcUyMgVy0SsaaYe4LMKP3BmpLmXsss4ya9l_sUnLcYroZmKaCgYKASQSARMSFQHGX2MiTxSL7vV58Tp-1ZQADsv_zg0179',
    'Content-Type': 'application/json',
}

params = {
    'project': 'nonprod-424912',
}

with open('s3.json', 'rb') as f:
    data = f.read()

response = requests.post('https://storage.googleapis.com/storage/v1/b', params=params, headers=headers, data=data)