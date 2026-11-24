
# Exibição do painel final
print("\n" + "=" * 45)
print("       PAINEL DE BÔNUS - ARKET")
# ==========================================
# SISTEMA DE CÁLCULO DE BÔNUS - ARKETECH
# Bônus de Boas-Vindas: 15%
# ==========================================

# Entrada de dados
nome = input("Digite o nome do funcionário: ")
cargo = input("Digite o cargo do funcionário: ")

# Conversão do salário para número decimal (float)
salario_base = float(input("Digite o salário base (use ponto, ex: 1500.50): "))

# Cálculo do bônus de 15%
bonus = salario_base * 0.15

# Cálculo do salário total do primeiro mês
salario_total = salario_base + bonusECH")
print("=" * 45)

print(f"Funcionário:       {nome}")
print(f"Cargo:             {cargo}")
print(f"Salário original:  R$ {salario_base:.2f}")
print(f"Bônus (15%):       R$ {bonus:.2f}")
print("-" * 45)
print(f"TOTAL A RECEBER:   R$ {salario_total:.2f}")

print("=" * 45)
print("Cálculo realizado com sucesso!")