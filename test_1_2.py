#!/user/bin/python3.11
# -*- coding: utf-8 -*-

import pandas as pd
import pyarrow

df = pd.read_csv("product_class.csv")
print(df)


class Goods:
    title = "Мороженое"
    weight = 154
    tp = "Еда"
    price = 1024


Goods.price = 2048
Goods.inflation = 100


class Car:
    pass


setattr(Car, "model", "Тойота")
setattr(Car, "color", "Розовый")
setattr(Car, "number", "П111УУ77")

print(Car.__dict__["color"])


