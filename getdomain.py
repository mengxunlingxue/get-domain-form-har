import json
from urllib.parse import urlparse

# 替换为您的HAR文件路径
har_file_path = '***.har'

# 读取HAR文件
with open(har_file_path, 'r') as f:
    har_data = json.load(f)

# 提取请求条目
entries = har_data['log']['entries']

# 创建一个集合来存储域名，以确保它们是唯一的
domains = set()

# 遍历所有条目并提取域名
for entry in entries:
    request_url = entry['request']['url']
    domain = urlparse(request_url).netloc
    domains.add(domain)

# 打印所有唯一的域名
for domain in domains:
    print(domain)
