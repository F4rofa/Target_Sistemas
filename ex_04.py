"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro
do valor total mensal da distribuidora. """

sp, rj, mg, es = 67836.43, 36678.66, 29229.88, 27165.48
others = 19849.53
soma = sp + rj + mg + es + others
state = input("Digite qual estado você quer ver: ")

perc_sp = (sp / soma) * 100
perc_rj = (rj / soma) * 100
perc_mg = (mg / soma) * 100
perc_es = (es / soma) * 100
perc_others = (others / soma) * 100

while state:
    print('Digite "stop" para parar o loop')
    match state:
        case 'sp':
            print(f"SP: {round(perc_sp, 2)}%")
        case 'rj':
            print(f"RJ: {round(perc_rj, 2)}%")
        case 'mg':
            print(f"MG: {round(perc_mg, 2)}%")
        case 'es':
            print(f"ES: {round(perc_es, 2)}%")
        case 'outros':
            print(f"Outros: {round(perc_others, 2)}%")
        case 'todos':
            print(f"SP: {round(perc_sp, 2)}%")
            print(f"RJ: {round(perc_rj, 2)}%")
            print(f"ES: {round(perc_es, 2)}%")
            print(f"Outros: {round(perc_others, 2)}%")
        case 'stop':
            break
        case _:
            print('Digite de novo')
