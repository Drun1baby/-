import requests
import json

def fingerprint(base_url):

    url = base_url + '/webroot/decision/system/info'
    response = requests.get(url, verify=False)

    data = json.loads(response.text)

    jar_time = data['data']['versionInfo'][0]['jarTime']
    minor_version = data['data']['versionInfo'][0]['minorVersion']

    return jar_time, minor_version

# fingerprint("https://123.7.84.144:6060")