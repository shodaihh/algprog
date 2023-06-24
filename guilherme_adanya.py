#**************************************************
# *
# * Guilherme Hideki Adanya
# * Trabalho 2
# * Professor: Marco Aurélio 
# *



#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Postagem:
    def __init__(self, conteudo, hashtags):
        self.conteudo = conteudo
        self.hashtags = hashtags

class RedeSocial:
    def __init__(self):
        self.postagens = []  # Lista de postagens
        self.hashtags = {}  # Dicionário de hashtags e suas contagens

    def inserir_postagem(self, conteudo):
        hashtags = self.extract_hashtags(conteudo)  # Extrai as hashtags do conteúdo da postagem
        postagem = Postagem(conteudo, hashtags)  # Cria um objeto Postagem com o conteúdo e as hashtags
        self.postagens.append(postagem)  # Adiciona a postagem à lista de postagens

        for hashtag in hashtags:
            if hashtag in self.hashtags:
                self.hashtags[hashtag] += 1  # Incrementa a contagem se a hashtag já existe no dicionário
            else:
                self.hashtags[hashtag] = 1  # Adiciona a hashtag com contagem 1 ao dicionário se for a primeira ocorrência

    def numero_hashtags(self, conteudo):
        hashtags = []
        words = conteudo.split()
        for word in words:
            if word.startswith("#"):
                hashtags.append(word[1:])  # Remove o "#" e adiciona a hashtag à lista
        return hashtags

    def listar_hashtags(self):
        for hashtag, count in sorted(self.hashtags.items()):  # Ordena as hashtags em ordem alfabética
            print(f'#{hashtag} {count}')  # Imprime a hashtag e sua contagem

    def post_hashtag(self, hashtag):
        for postagem in self.postagens:
            if hashtag in postagem.hashtags:
                print(postagem.conteudo)  # Imprime o conteúdo da postagem se a hashtag estiver presente

    def teste(self):
        self.postagens = []  # Limpa a lista de postagens
        self.hashtags = {}  # Limpa o dicionário de hashtags e suas contagens


rede_social = RedeSocial()

casos_teste = int(input())

for i in range(casos_teste):
    while True:
        entrada = input().split()
        operaçao = entrada[0]

        if operaçao == "I":
            conteudo = ' '.join(entrada[1:])
            rede_social.inserir_postagem(conteudo)

        elif operaçao == "L":
            rede_social.listar_hashtags()

        elif operaçao == "P":
            hashtag = entrada[1]
            rede_social.post_hashtag(hashtag)

        elif operacao == "F":
            rede_social.caso_de_teste()
            print()  
            break
exit(0)


    
    
