# 💸 Calculadora de Investimentos com Aporte Mensal

Sistema simples em Python que calcula projeções de investimentos usando:

- Juros Simples
- Juros Compostos
- Valor Futuro com Aportes Mensais

Ideal para simular crescimento de patrimônio ao longo do tempo.

## 🚀 Como usar

1. Clone o repositório:
```bash
git clone https://github.com/seuusuario/calculadora-investimentos.git
cd calculadora-investimentos
```

2. Execute no terminal:
```bash
python calculadora_investimentos.py
```

3. Insira os dados:
- Capital inicial
- Valor do aporte mensal
- Taxa de juros (decimal)
- Número de meses

## 📦 Exemplo de entrada

```
Capital inicial (R$): 1000  
Aporte mensal (R$): 500  
Taxa de juros mensal: 0.01  
Número de meses: 12
```

## 📊 Exemplo de saída

```
Montante sobre capital inicial: R$1126.83  
Acumulado dos aportes mensais: R$6370.88  
Valor futuro total: R$7497.71
```

## 🧠 Fórmulas aplicadas

- Juros Simples: `J = C * i * t`
- Juros Compostos: `M = C * (1 + i)^t`
- Valor Futuro com Aporte: `VF = P * [(1 + i)^n - 1] / i`

---

## 📁 Estrutura do projeto

```
📦 calculadora-investimentos
┣ 📜 calculadora_investimentos.py
┗ 📄 README.md
```

---

## 👨‍💻 Autor

Feito por **Dev Dogarpe** – projeto didático para estudos de Python e finanças pessoais.