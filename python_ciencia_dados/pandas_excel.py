import pandas as pd


### lendo arquivo
arq = pd.read_excel('C:\\Users\\joth1\\Desktop\\python\\Aprendendo-python\\python_ciencia_dados\\dadospandas.xlsx')
arq1 = pd.read_excel('C:\\Users\\joth1\\Desktop\\python\\Aprendendo-python\\python_ciencia_dados\\dadospandas copy.xlsx')
arq2 = pd.read_excel('C:\\Users\\joth1\\Desktop\\python\\Aprendendo-python\\python_ciencia_dados\\dadospandas copy 2.xlsx')

# juntando arquivos 
arq_final= pd.concat([arq,arq1,arq2])

print(arq_final.head(30))

### verificando tipo de dados
print('tipos de dados ')
print(arq_final.dtypes)

# verificando itens aleatorios 
print

