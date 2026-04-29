# 2. Crie uma função capaz de calcular o Imposto de Renda:

# Leia as regras em:
# https://www.gov.br/receitafederal/pt-br/assuntos/meu-imposto-de-renda/tabelas/2026
import math

def calcular_desconto_inss(salario: float) -> float:
    if salario > 8475.56:
        salario = 8475.56

    if salario <= 1621.00:
        desconto = salario * 0.075

    elif salario <= 2902.84:
        desconto = (1621.00 * 0.075) + ((salario - 1621.00) * 0.09)

    elif salario <= 4190.83:
        desconto = (
            (1621.00 * 0.075) +
            ((2902.84 - 1621.00) * 0.09) +
            ((salario - 2902.84) * 0.12)
        )

    else:
        desconto = (
            (1621.00 * 0.075) +
            ((2902.84 - 1621.00) * 0.09) +
            ((4354.28 - 2902.84) * 0.12) +
            ((salario - 4354.28) * 0.14)
        )

    return desconto

def calcular_desconto_irpf(salario: float) -> float:
    dependentes = input("Dependentes: ").strip()
    if dependentes:
        dependentes = float(dependentes.replace(',', '.'))
        deducao_dependentes = dependentes * 189.59
    else:
        deducao_dependentes = 0

    outras = input("Outras deduções: ").strip()
    if outras:
        outras = float(outras.replace(',', '.'))
    else:
        outras = 0

    base = salario - deducao_dependentes - outras

    if base <= 5000:
        ir = 0

    elif base <= 7350:
        ir_base = (base * 0.275) - 896.00
        fator = (7350 - base) / (7350 - 5000)
        ir = ir_base * (1 - fator)

    else:
        ir = (base * 0.275) - 896.00

    if ir < 0:
        ir = 0

    return ir

print ("\n\n")
salario_bruto = float(input("digite o salário bruto total: "))

desconto_inss = calcular_desconto_inss(salario_bruto)

desconto_irpf = calcular_desconto_irpf(salario_bruto - desconto_inss)

print(f"{salario_bruto - desconto_inss:.2f}")

print ("\n\n")
print (f"Salário: \t{salario_bruto:.2f}")
print (f"(-) INSS: \t{desconto_inss:.2f}")
print (f"(-) IRPF: \t{desconto_irpf:.2f}")

salario_liquido = salario_bruto - desconto_inss - desconto_irpf

print (f"Salário líquido: {salario_liquido:.2f}")