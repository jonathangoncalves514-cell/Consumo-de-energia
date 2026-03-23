#programa para calculo de consumo de energia
#entrada

aparelho=input("Olá,qual o nome do aparelho?" )
potencia=float(input("informe a potência do aparelho em watts(w): "))
horasdia=float(input("Qual o tempo médio de uso diário em horas do aparelho? "))

#processamento
#calculo

consumomensal=(potencia* horasdia* 30) / 1000

#valor do kwh
valor_kwh=0.75

#cálculo do custo
custo=consumomensal* valor_kwh

print("aparelho=",aparelho)
print("consumo estimado é de=", round(consumomensal),"kwh/mês")
print("custo estimado e de R$", round(custo,2))