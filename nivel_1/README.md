# PDV — Sistema de Descontos

## 1. O que o código faz

Este programa implementa a lógica de um **PDV (Ponto de Venda)**. O sistema recebe o valor de uma compra e a idade do cliente, aplica descontos de acordo com as regras estabelecidas, registra cada compra em uma lista e, quando o usuário encerra o programa, apresenta um resumo do dia com a quantidade de compras, o total bruto, o total de descontos concedidos e o total final das compras.

---

## 2. Regras de desconto

O programa possui duas regras de desconto:

### Desconto por idade

Se o cliente tiver **65 anos ou mais**, é aplicado um desconto de **20%** sobre o valor da compra.

```text
valor × 0.80
```

### Desconto por valor

Depois de aplicar o desconto por idade, o programa verifica o novo valor.

Se o valor já descontado for **maior que R$ 100,00**, é aplicado mais um desconto de **10%**.

```text
valor_final × 0.90
```

A ordem das regras é importante. O desconto de 10% é aplicado sobre o valor que já recebeu o desconto de idade, quando houver.

---

## 3. Como o programa funciona

O funcionamento do programa ocorre da seguinte forma:

1. O programa exibe uma mensagem de boas-vindas.
2. É criada uma lista chamada `compras` para armazenar o histórico das compras.
3. O programa entra em um loop utilizando `while True`.
4. O usuário informa o valor da compra.
5. Se o valor informado for `0`, o programa encerra o loop.
6. Se o valor for negativo, o programa exibe uma mensagem de aviso e utiliza `continue` para solicitar uma nova compra.
7. O usuário informa a idade do cliente.
8. Se a idade for negativa, o programa exibe uma mensagem de aviso e solicita uma nova compra.
9. O valor original é armazenado na variável `valor`.
10. A variável `valor_final` recebe inicialmente o valor da compra.
11. Se a idade for maior ou igual a 65 anos, são aplicados 20% de desconto.
12. Depois, o programa verifica se o valor já descontado é maior que R$ 100,00.
13. Se for maior que R$ 100,00, são aplicados mais 10% de desconto.
14. O desconto total é calculado pela diferença entre o valor original e o valor final.
15. Os dados da compra são armazenados na lista `compras` utilizando `.append()`.
16. O valor final é exibido no console com duas casas decimais.
17. Quando o usuário digita `0`, o loop termina.
18. O programa percorre a lista de compras utilizando um `for`.
19. Ao final, são calculados e exibidos:
    - quantidade de compras;
    - total bruto;
    - total de descontos concedidos;
    - total final.

---

## 4. Estrutura utilizada

Cada compra é armazenada na lista `compras` como um dicionário:

```python
compras.append({
    "valor": valor,
    "desconto_aplicado": desconto,
    "valor_final": valor_final
})
```

Dessa forma, cada registro possui três informações:

- `valor`: valor original da compra;
- `desconto_aplicado`: valor total descontado;
- `valor_final`: valor que o cliente deverá pagar.

---

## 5. Loop de compras

O programa permite registrar várias compras seguidas.

O loop é controlado por:

```python
while True:
```

Para encerrar o programa, o usuário deve informar:

```text
0
```

Quando isso acontece:

```python
if valor == 0:
    break
```

O comando `break` encerra o loop e o programa passa para a etapa do resumo final.

---

## 6. Validação dos dados

O programa verifica se o valor da compra ou a idade são negativos.

```python
if valor < 0 or idade < 0:
    print("Valor ou idade não podem ser negativos.")
    continue
```

Caso um valor negativo seja informado, uma mensagem de aviso é exibida e o `continue` faz o programa voltar para o início do loop, permitindo uma nova entrada.

---

## 7. Resumo do dia

Depois que o usuário encerra o programa, a lista `compras` é percorrida:

```python
for compra in compras:
```

Durante esse processo são calculados:

### Quantidade de compras

```python
quantidade = len(compras)
```

### Total bruto

É a soma de todos os valores originais das compras.

### Total de descontos

É a soma dos descontos concedidos em todas as compras.

### Total final

É a soma dos valores finais que deverão ser pagos.

---

## 8. Casos de teste

Os seguintes casos foram utilizados para validar o funcionamento do programa:

| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---|---:|---:|---:|---:|---:|
| 1 | 50.00 | 30 | 0% | 0% | **R$ 50.00** |
| 2 | 100.00 | 30 | 0% | 0% | **R$ 100.00** |
| 3 | 80.00 | 65 | 20% | 0% | **R$ 64.00** |
| 4 | 100.00 | 70 | 20% | 0% | **R$ 80.00** |
| 5 | 125.00 | 70 | 20% | 0% | **R$ 100.00** |
| 6 | 200.00 | 30 | 0% | 10% | **R$ 180.00** |
| 7 | 101.00 | 30 | 0% | 10% | **R$ 90.90** |
| 8 | 200.00 | 65 | 20% | 10% | **R$ 144.00** |
| 9 | 1000.00 | 80 | 20% | 10% | **R$ 720.00** |
| 10 | 200.00 | 64 | 0% | 10% | **R$ 180.00** |

### Casos-limite importantes

**Caso 5 — R$ 125,00 e idade 70**

Primeiro é aplicado o desconto de 20%:

```text
125 × 0.80 = 100
```

Como o resultado é exatamente `100`, e a regra exige que seja **maior que 100**, o desconto adicional de 10% não é aplicado.

Resultado:

```text
R$ 100.00
```

**Caso 7 — R$ 101,00 e idade 30**

Não há desconto por idade. Como `101` é maior que `100`, aplica-se 10%:

```text
101 × 0.90 = 90.90
```

Resultado:

```text
R$ 90.90
```

**Caso 10 — R$ 200,00 e idade 64**

O cliente tem menos de 65 anos, portanto não recebe o desconto de idade.

Como o valor é maior que R$ 100,00, recebe apenas 10%:

```text
200 × 0.90 = 180
```

Resultado:

```text
R$ 180.00
```

---

## 9. Como executar

Entre na pasta `nivel_1` e execute:

```bash
python pdv.py
```

Depois, informe o valor da compra e a idade do cliente conforme solicitado pelo programa.

Para encerrar o cadastro de compras, informe:

```text
0
```

---

## 10. Estrutura da atividade

```text
nivel_1/
├── pdv.py
└── README.md
```

- `pdv.py` → código do sistema PDV.
- `README.md` → documentação da atividade.

---

## 11. Resultado

O programa atende aos requisitos propostos para o exercício:

- aplicação correta dos dois descontos;
- validação dos 10 casos de teste;
- loop para várias compras;
- encerramento utilizando `0`;
- armazenamento das compras em uma lista;
- utilização de `.append()`;
- cálculo do resumo final;
- validação de valores negativos;
- documentação da solução no `README.md`.

---

## Autor

<a href="https://github.com/joaobatistamedeiroscf">
  <img src="https://github.com/joaobatistamedeiroscf.png" width="120" alt="Foto de perfil de João Batista Medeiros" />
</a>

[João Batista Medeiros](https://github.com/joaobatistamedeiroscf)