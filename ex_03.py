"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""
import json
# Identificando qual arquivo que ele vai usar
filename = 'dados.json'
qtd_dias = 0
maxValue=0
allValores = []
# abrindo o arquivo no modo de leitura e carregando os datos 
with open(filename, "r") as json_file:
    data = json.load(json_file)
    print(data[0])
    days_data = (data)
    
    for i in days_data:
        somaValores=0
        dia = int((i["dia"]))
        valor = float((i["valor"]))

        if valor != 0:
            somaValores += valor
            allValores.append(valor)


valormed = somaValores / len(days_data)

for valor in allValores:   
    if valor > valormed:
         qtd_dias+=1
    if valor > maxValue:
        maxValue = valor

print(f"O menor valor de faturamento ocorrido em um dia do mês: {min(allValores)}")
print(f"O maior valor de faturamento ocorrido em um dia do mês: {maxValue}")
print(f"Número de dias no mês em que o valor de faturamento diário foi superior à média mensal: {qtd_dias}")
