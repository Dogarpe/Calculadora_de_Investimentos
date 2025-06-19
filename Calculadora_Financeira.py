def juros_simples(capital, taxa, tempo):
    return capital * taxa * tempo

def juros_compostos(capital, taxa, tempo):
    return capital * (1 + taxa) ** tempo

def valor_presente(fv, taxa, n):
    return fv / (1 + taxa) ** n

def valor_futuro_aporte(aporte_mensal, taxa, n):
    return aporte_mensal * (((1 + taxa) ** n - 1) / taxa)

def main():
    print("Calculadora Financeira")
    capital_inicial = float(input("Capital inicial (R$): "))
    aporte_mensal = float(input("Aporte Mensal (R$): "))
    taxa = float(input("taxa de juros mensal (ex 0.01 para 1%): "))
    tempo = int(input("Número de meses "))

    jc = juros_compostos(capital_inicial, taxa, tempo)
    vf_aporte = valor_futuro_aporte(aporte_mensal, taxa, tempo)
    total = jc + vf_aporte

    print(f"\nMontante sobre capital inicial: R${jc:.2f}")
    print(f"Acumulado dos aportes mensais: R${vf_aporte:.2f}")
    print(f"Valor futuro total: R${total:.2f}")

if __name__ == "__main__":
    main()