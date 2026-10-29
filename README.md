Há algum tempo, venho tendo interesse em aprender mais sobre Machine Learning. Com isso, resolvi ir atrás de um pequeno projeto para entender, na prática, como um algoritmo consegue aprender com seus próprios erros.

Foi assim que descobri o **Perceptron**, um dos algoritmos mais simples de aprendizado supervisionado, utilizado para classificação binária. Basicamente, utilizando apenas valores de 0 e 1, consegui criar um pequeno neurônio artificial capaz de aprender uma regra a partir de exemplos.

```python
dados = [
    ((0, 0), 0),
    ((0, 1), 0),
    ((1, 0), 0),
    ((1, 1), 1),
]
```

Para o projeto, utilizei uma situação bem simples: **a irrigação de um solo**.

Imagine que temos duas condições:
- **Solo seco:** se estiver seco, recebe `1`; caso contrário, `0`.
- **Dia quente:** se estiver quente, recebe `1`; caso contrário, `0`.

A ideia é que o algoritmo aprenda a irrigar apenas quando as duas condições forem verdadeiras, ou seja, quando ambas receberem o valor `1`.

O interessante é que, em nenhum momento, precisei dizer diretamente ao algoritmo qual condição ele deveria seguir. Em vez disso, forneci exemplos com suas respectivas respostas e deixei que ele fosse ajustando seus pesos a cada erro cometido.

**É justamente essa a parte que mais me chamou a atenção:** o algoritmo começa sem conhecer a regra e, conforme erra, ajusta seus parâmetros até conseguir reproduzir o comportamento esperado.

Claro, é um exemplo bastante simplificado e até um pouco metafórico, afinal, irrigar um solo envolve muito mais fatores do que apenas temperatura e umidade. Mas acredito que atribuir situações do cotidiano ao que estamos estudando é uma ótima maneira de compreender conceitos que, inicialmente, parecem complicados.

Esse foi meu primeiro contato prático com Machine Learning em muito tempo (já tive prática com alguns algoritmos na faculdade, mas faz tempo). É um projeto pequeno, mas que me ajudou a entender um pouco melhor como uma máquina pode aprender a partir dos próprios erros, sem que cada decisão precise ser programada manualmente.