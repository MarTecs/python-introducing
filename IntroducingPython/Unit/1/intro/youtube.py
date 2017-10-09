
# 从python 标准库中导入名为json的所有代码
import json
# 从python标准urllib库中导入urlopen函数
from urllib import urlopen
# 给变量url赋值一个youtube地址
url = "https://gdata.youtube.com/feeds/api.standardfeeds/top_rated?alt=json"
# 连接指定地址处的Web服务器并请求指定url地址
response = urlopen(url)
# 获取响应数据，并将指定数据赋值给指定变量
contents = response.read()
# 把text转换为data -- 一个存储视频信息的Python数据结构
text = contents.decode("utf8")
# 每次获取一个视频的信息并将视频信息赋值给变量data
data = json.loads(text)
# 使用两层python字典data['feed']['entry'] 和 切片操作[0:6]
for video in data['feed']['entry'][0:6]:
    # 使用print函数打印视频标题
    print(video['title']['$t'])