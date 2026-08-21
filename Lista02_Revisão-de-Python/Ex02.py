mes=int(input("Informe o número do mês:"))

meses=["Janeiro", "Fevereiro","Março","Abril","Maio","Junho","Julho",
       "Agosto","Setembro","Outubro","Novembro","Dezembro"]

trimestre_mes="primeiro"
if mes>=3:
    if 3<mes<=6:
        trimestre_mes="segundo"
    if 6<mes<=9:
        trimestre_mes="terceiro"
    if 9<mes<=12:
        trimestre_mes="quarto"

print("O mês de", meses[mes-1],"é do",trimestre_mes,"trimestre do ano")