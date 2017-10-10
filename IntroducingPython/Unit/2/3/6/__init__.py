# 使用[]提取字符
"""
通过在字符串名字后面添加[] 来指定偏移量从而提取该字符
"""
letter = "Hello World"
print(letter[0])

### 注意事项：字符串是不可以变的
letter[0] = 'G'
print(letter)