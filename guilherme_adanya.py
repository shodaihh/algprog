#**************************************************
# *
# * Guilherme Hideki Adanya
# * Trabalho 1
# * Professor: Marco Aurelio Stefanes
# *



#!/usr/bin/env python
# -*- coding: utf-8 -*-


def valor_carta(carta):
  valores = {'J' : 11, 'Q': 12 , 'K' :13, 'A':14}
  if carta.isdigit():
    return int(carta)
  else:
    return valores[carta]
    
def naipe(carta):
  return carta[-1]
  
def verificar_mao(cartas):
  valores = [valor_carta(carta) for carta in cartas]
  naipes = [naipe(carta) for carta in cartas]
  
  if len(set(naipes)) == 1:
    return 'Flush'

  valores.sort()
  
  if valores == list(range(valores[0] , valores [0] + 5 )):
    return 'Sequência'
    
  for valor in set(valores):
    if valores.count(valor) == 4:
      return 'Quadra'
    elif valores.count(valor) == 3: 
      if 2 in set(valores):
        return 'Full House'
      else:
        return 'Trinca'
    elif valores.count(valor) == 2: 
      if len(set(valores)) == 3:
        return 'Dois Pares'
      else:
        return 'Par'
     
  return 'Carta mais alta'
  
def comparar_maos(mao1 , mao2):
  maos = ['Flush' , 'Sequencia' , 'Quadra' , 'Full House' , 'Trinca' , 'Dois Pares' , 'Par', 'Carta mais alta']
  if maos.index(mao1) > maos.index(mao2) :
    return 1 
  elif maos.index(mao1) < maos.index(mao2):
    return 2 
  else:
    return 'E'
    
def resolver_jogo(casos_teste):
    for _ in range(casos_teste):
        cartas1 = input().split()
        cartas2 = input().split()

        mao1 = verificar_mao(cartas1)
        mao2 = verificar_mao(cartas2)

        resultado = comparar_maos(mao1, mao2)
        print(resultado)
        
exit(0)
    
    