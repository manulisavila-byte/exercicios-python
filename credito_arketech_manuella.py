# Sistema de Análise de Crédito - ArkeTech
# Entrada de dados
empresa = input("Digite o nome da empresa: ")
faturamento = float(input("Digite o faturamento mensal (R$): "))
emprestimo = float(input("Digite o valor do empréstimo solicitado (R$): "))
# Cálculo da parcela mensal (12 vezes, sem juros)
parcela = emprestimo / 12
# Árvore de decisão
print("\n===== ANÁLISE DE CRÉDITO =====")
print(f"Empresa: {empresa}")
print(f"Faturamento mensal: R$ {faturamento:.2f}")
print(f"Valor do empréstimo: R$ {emprestimo:.2f}")
print(f"Parcela mensal: R$ {parcela:.2f}")
if parcela <= faturamento * 0.30:
   print("PARECER: APROVADO")
elif parcela <= faturamento * 0.50:
   print("PARECER: EM ANÁLISE (RISCO MODERADO)")
else:
   print("PARECER: RECUSADO")