import requests
import re

def handle(url):

    response = requests.get(url, verify=False)

# 使用正则表达式提取href值
    href_pattern = re.findall(r'location\.href=([^;]+)', response.text)
    if href_pattern:
        for match in href_pattern:
            parts = match.split('?')
            if len(parts) > 1:
                result = parts[0][1:]
                print(f"获取到的 webroot 为 {result}")
                return result
    else:
        print('未找到匹配的关键字')
        return ''

if __name__ == '__main__':
    test_url = 'https://112.90.146.204/'
    handle(test_url)