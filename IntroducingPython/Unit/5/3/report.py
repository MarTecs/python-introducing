from random import choice


def get_description():  #看到下面的文档字符串了么
    """Return random weather, just like the pros"""

    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)