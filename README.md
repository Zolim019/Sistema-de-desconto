# 🛒 Sistema de Desconto Progressivo

## 📌 Sobre o projeto

Este projeto foi desenvolvido como **atividade de recuperação** do curso Técnico em Desenvolvimento de Sistemas.

O programa simula um sistema de **desconto progressivo** para uma loja online. O desconto aplicado depende do valor total da compra.

## 💰 Regras de desconto

| Valor da compra                      | Desconto |
| ------------------------------------ | -------: |
| Menor que R$ 200,00                  |       5% |
| De R$ 200,00 até menor que R$ 300,00 |      10% |
| R$ 300,00 ou mais                    |      15% |

## ⚙️ Como funciona

O programa solicita ao usuário o **valor total da compra** e verifica qual desconto deve ser aplicado.

Depois, calcula:

* 💵 Valor do desconto;
* 🧾 Valor final da compra;
* 📊 Exibição dos resultados na tela.

## 💻 Tecnologias utilizadas

* 🐍 Python
* 💻 Visual Studio Code
* 🐙 GitHub

## 🧠 Conceitos utilizados

Nesta atividade foram utilizados os seguintes conceitos:

* Variáveis;
* Entrada de dados com `input()`;
* Conversão de dados com `float()`;
* Estrutura de decisão `if`, `elif` e `else`;
* Operações matemáticas;
* `print()` para exibição dos resultados;
* Formatação de valores utilizando `f-string`.

## ▶️ Exemplo de execução

```text
Digite o valor total da compra: R$ 250

--- Resultado da compra ---
Valor da compra: R$ 250.00
Valor do desconto: R$ 25.00
Valor a pagar: R$ 225.00
```

## 📂 Estrutura do projeto

```text
desconto-progressivo/
│
├── desconto.py
└── README.md
```

## 📸 Testes realizados

O programa foi testado utilizando diferentes valores de compra para verificar as três faixas de desconto:

* 🟢 R$ 150,00 → 5% de desconto
* 🟡 R$ 250,00 → 10% de desconto
* 🔵 R$ 350,00 → 15% de desconto

## 👨‍💻 Autor

**Vitor Zolim**

Projeto desenvolvido para fins acadêmicos.
