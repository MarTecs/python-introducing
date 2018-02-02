# python-introducing


## 尹成Python



### OS 模块下执行指令乱码解决方法
```Python
import os

os.system("ipconfig")##打印本机的IP地址，将不会打印中文


```

> 打开pycharm 的 File-->Settings-->Editor-->File Encodings-->修改Project Encoding为 GBK


