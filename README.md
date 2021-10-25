# desafio_zax

Requer: Python3

A solução assume uma distribuição determinística dos pedidos, dando prioridado aos motoboys de número menor, mas respeitando a prioridade dada pela exclusividade a lojas.

A solução também assume que a pergunta "De qual loja é?" refere-se aos pedidos, dado que um motoboy pode entregar para múltiplas lojas (portanto, a pergunta deveria ter "loja" no plural, apesar de que a interpretação de que se refere aos pedidos pede o verbo no plural) e que as lojas pelas quais cada motoboy entrega é sabido de antemão.

Ainda, a solução toma a ausência de parâmetros de usuário para a invocação do programa como uma instrução para exibir as informações requeridas de todos os motoboys, pois a alternativa pensável seria a de não exibir a informação de nenhum motoboy, o que seria inútil.

Assim, o programa deve ser invocado por uma linha de comando da seguinte forma:

`$ python3 main.py [numero_do_motoboy]`