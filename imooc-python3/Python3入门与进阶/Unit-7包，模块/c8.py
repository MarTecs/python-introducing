## import只可以导入模块
import c7;

print(c7.a);

## 可以将导入的模块取一个别名
import c7 as c;
print(c.a);

import t.c1 as c1;
print(c1.a);

## 使用from导入
###from module_name import def,variable_name
from c7 import a
print(a);


from t import c1
print(c1.a);

from t.c1 import a
print(a);


## 将c1中的内容全部导入,过多的使用*将会造成引入不明确，效率低下
from t.c1 import *
print(c);
print(d)    #当我们在t.c1中指定__all__=['a','b']的时候，我们使用*只会导入__all__中指定的内容，并不会全部导入

## 当我们一次从模块中导入内容过多的时候，我们需要注意，每行建议不超过80个字符，如果需要换行，可以采用如下方式

### 方法一，行末加一个\
from t.c1 import a,b,\
    c;
print(c);
print(b);

### 方法二：对于要导入的使用括号括起来
from t.c1 import (a,b,c)
print(b)


