# 1 Em uma instrução print, o que acontece se você omitir um dos parênteses ou ambos?
receberá um erro de sintaxe 
print ola mundo 
#exemplo 

#Se estiver tentando imprimir uma string, o que acontece se omitir uma das aspas ou ambas?
receberá um erro de sintaxe
print (ola mundo!)
print ("ola mundo!) 
#exemplo 

       
#Você pode usar um sinal de menos para fazer um número negativo como -2. O que acontece se puser um sinal de mais antes de um número? E se escrever assim: 2++2?
 Não muda nada porém se você colocAR 2++2 O  python pode interpretar como um sinal de soma e somar 2+2 =4  mas é preciso ter uma operação valida, senão ocorrerá novamente um erro de sintaxe



#Na notação matemática, zeros à esquerda são aceitáveis, como em 02. O que acontece se você tentar usar isso no Python?
 em python pelo que pesquisei zeros à esquerda em literais inteiros são interpretados como números octais (base 8). Portanto, 02 é interpretado como o número octal, desse jeito pode levar a resultados inesperados se essa nao for a intenção.

#O que acontece se você tiver dois valores sem nenhum operador entre eles?
 erro de sintaxe 
#exemplo 
a = 5
b = 10
c = a b
