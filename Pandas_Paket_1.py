import pandas as pd
import numpy as np



iris_dict = {
    "Sepal_lenght" : [5.1 , 4.9, 4.7, 4.6, 5.0, 6.7, 6.3, 6.5, 6.2, 5.9],
    "sepal_width" : [3.5 , 3.0, 3.2, 3.1, 3.6, 3.0, 2.5, 3.0, 3.4, 3.0],
    "Petal_lenght" : [1.4, 1.4, 1.3, 1.5, 1.4, 5.2, 5.0, 5.2, 5.4, 5.1],
    "Petal_width" : [0.2, 0.2, 0.2, 0.2, 0.2, 2.3, 1.9, 2.0, 2.3, 1.8],
    "species" : ["setosa", "setosa", "setosa" , "setosa", "setosa", "virginica", "virginica", 
                "virginica" ,"virginica" ,"virginica" ]
}

print(iris_dict)

# şimdi pandastan verileri çekip çerçeveye alalım.

iris = pd.DataFrame(iris_dict)
print(iris)

import seaborn as sns
iris_real = sns.load_dataset("iris")

print(iris_real)

