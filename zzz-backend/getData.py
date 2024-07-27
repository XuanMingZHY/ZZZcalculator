import requests
from lxml import html

# 设置目标URL
url = 'http://demo.zzz.zzzwiki.cn/agents/1191'  # 替换为实际URL

# 发送HTTP GET请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 解析网页内容
    tree = html.fromstring(response.content)
    
    # 使用XPath提取数据
    data = tree.xpath('/html/body/div[1]/div[1]/div/div[2]/div[2]/div[1]/div/div[1]/div[1]/div[3]/div[3]/div[2]/span[2]')
    
    # 打印提取的数据
    if data:
        print('提取的数据:', data[0])
    else:
        print('没有找到匹配的数据')
else:
    print('请求失败，状态码:', response.status_code)