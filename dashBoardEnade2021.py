# Esse DahsBoard tem o objetivo de exibir informações do último Enade, realizado em 2021, no qual tivemos
# a participação dos alunos do curso de Sistemas de Informação da UFERSA-Angicos/RN.

# O Dashboard foi desenvolvido em Python, utilizando a biblioteca PyMongo para acessar os dados 
# dos arquivos diretamente na nuvem e o Matplotlib para gerar os gráficos.

# Trabalho para o projeto da disciplina de Projeto e Administração de Banco de Dados.

# Desenvolvido por Ywry Scheller Medeiros Galvão, João Victor Cunha e Marcelo Júnior.

from pymongo import MongoClient
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Requisitando os dados na nuvem (MongoDB).
client = MongoClient("mongodb+srv://ywry:44852@cluster0.n5lvyox.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
dadosEnade = client["dadosEnade"]

#informacoesCurso = dadosEnade["informacoesCurso"]
#data = pd.read_csv("/content/sample_data/microdados2021_arq1.txt", delimiter=";")
#data_dict = data.to_dict("records")
#informacoesCurso.insert_many(data_dict)

#informacoesAcademicas = dadosEnade["informacoesAcademicas"]
#data = pd.read_csv("/content/sample_data/microdados2021_arq2.txt", delimiter=";")
#data_dict = data.to_dict("records")
#informacoesAcademicas.insert_many(data_dict)

#data = pd.read_csv("/content/sample_data/microdados2021_arq3.txt", delimiter=";")
#data.drop(data.columns[[0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18,19,20,21,22,23,24,25,26,43,44,45,46,47,48,49,50,51]], axis=1, inplace=True)
#desempenho = dadosEnade["desempenho"]
#data_dict = data.to_dict("records")
#desempenho.insert_many(data_dict)

#sexo = dadosEnade["sexo"]
#data = pd.read_csv("/content/sample_data/microdados2021_arq5.txt", delimiter=";")
#data_dict = data.to_dict("records")
#sexo.insert_many(data_dict)


# Consultando e manipulando os dados

consulta1 = pd.DataFrame(list(dadosEnade.informacoesCurso.find({"CO_IES":589, "CO_MUNIC_CURSO":2400802}, {"CO_CURSO":True, "CO_IES":True, "CO_MUNIC_CURSO":True, "_id":False})))
sns.countplot(y = consulta1['CO_CURSO'])

#dadosEnade.informacoesCurso.update_many({"CO_CURSO":1117717},{"$set":{"CO_CURSO":"Sistemas de Informação"}})
#dadosEnade.informacoesCurso.update_many({"CO_CURSO":1117715},{"$set":{"CO_CURSO":"Computação e Informática"}})
#dadosEnade.informacoesCurso.update_many({"CO_CURSO":1383124},{"$set":{"CO_CURSO":"Pedagogia"}})
consulta2 = pd.DataFrame(list(dadosEnade.informacoesCurso.find({"CO_IES":589, "CO_MUNIC_CURSO":2400802}, {"CO_CURSO":True, "CO_IES":True, "CO_MUNIC_CURSO":True, "_id":False})))
sns.countplot(y = consulta2['CO_CURSO'])


consulta3 = pd.DataFrame(list(dadosEnade.desempenho.find({"$or":[{"CO_CURSO":1117717},{"CO_CURSO":1117715},{"CO_CURSO":1383124}]})))
consulta3

sns.countplot(x = consulta3['TP_PRES'])

consulta3 = pd.DataFrame(list(dadosEnade.desempenho.find({"$and":[{"$or":[{"CO_CURSO":1117717},{"CO_CURSO":1117715},{"CO_CURSO":1383124}]},{"TP_PRES":555}]})))
consulta3

plt.figure(figsize=(12,8))
plt.plot(consulta3['NT_FG'], label = 'Conhecimentos gerais')
plt.plot(consulta3['NT_CE'], label = 'Componente específico')
plt.title('Pontuações - Angicos')
plt.grid(True)
plt.legend()
plt.ylabel('Pontuações ENADE')
plt.show

consulta4 = pd.DataFrame(list(dadosEnade.desempenho.find({"$and":[{"CO_CURSO":1117717},{"TP_PRES":555}]})))
consulta4


plt.figure(figsize=(12,8))
plt.plot(consulta4['NT_FG'], label = 'Conhecimentos gerais')
plt.plot(consulta4['NT_CE'], label = 'Componente específico')
plt.title('Pontuações - BSI')
plt.grid(True)
plt.legend()
plt.ylabel('Pontuações ENADE')
plt.show


plt.figure(figsize=(12,8))
plt.plot(consulta4['NT_OBJ_CE'], label = 'Componente Específico(Objetiva)')
plt.plot(consulta4['NT_DIS_CE'], label = 'Componente Específico(Discurssiva)')
plt.title('Pontuações - BSI')
plt.grid(True)
plt.legend()
plt.ylabel('Pontuações ENADE')
plt.show


consultaM = pd.DataFrame(list(dadosEnade.sexo.find({"$and":[{"$or":[{"CO_CURSO":1117717},{"CO_CURSO":1117715}]},{"TP_SEXO":'M'}]})))
consultaF = pd.DataFrame(list(dadosEnade.sexo.find({"$and":[{"$or":[{"CO_CURSO":1117717},{"CO_CURSO":1117715}]},{"TP_SEXO":'F'}]})))

fig, ax = plt.subplots()
ax.pie([len(consultaF), len(consultaM)], labels=['Feminino','Masculino'], autopct='%1.0f%%')