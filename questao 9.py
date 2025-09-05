vendedor = str(input("Digite o seu nome:  "))
salario = float(input("Digite o valor do seu salario:  "))
vendas = float(input("Digite o valor das suas vendas:  "))
percentual = float(input("Digite o percentual de vendas total:  "))
resultado = salario + (percentual/100) * vendas
print (f"Olá {vendedor} ,o seu salario fixo é {salario} e o total é:  {resultado}")