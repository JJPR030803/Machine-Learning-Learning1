from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np


dataset = pd.read_csv("Dataset\Online Sales Data.csv")

ct_product_category = ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[2])],remainder="passthrough",)
ct_product_name = ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[4])],remainder="passthrough",)
ct_region = ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[7])],remainder="passthrough",)
ct_payment = ColumnTransformer(transformers=[("encoder",OneHotEncoder(),[8])],remainder="passthrough",)

columnas_categoricas = dataset.iloc[:,]

product_one = ct_product_category.fit_transform(columnas_categoricas)
product_name_one = ct_product_name.fit_transform(columnas_categoricas)
one_region = ct_region.fit_transform(columnas_categoricas)
one_payment = ct_payment.fit_transform(columnas_categoricas)

print(product_one)
print(product_name_one)
print(one_region)
print(one_payment)


#x = ct.fit_transform()