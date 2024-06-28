from google.cloud import storage
REQUESTS_CA_BUNDLE="/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/certifi/cacert.pem"
import requests
import requests
url = 'https://storage.googleapis.com'
response = requests.get(url, verify=False)
r = requests.get(url, verify='/Users/akshayshrivastava/.mac-ca-roots')

print(r)
def create_bucket(bucket_name):
    """Creates a new bucket."""
    # bucket_name = "your-new-bucket-name"

    storage_client = storage.Client()

    bucket = storage_client.create_bucket(bucket_name)

    print(f"Bucket {bucket.name} created")
# create_bucket("test123559")