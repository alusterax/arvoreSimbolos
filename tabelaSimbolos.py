import random
import pprint

class Simbolo:
    def __init__(self,nome,categoria,nivel,geral_A,geral_B):
        self.nome = nome
        self.categoria = categoria
        self.nivel = nivel
        self.geral_A = geral_A
        self.geral_B = geral_B

    def __repr__(self):
        return f'{self.nome}, {self.categoria}, {self.nivel}, {self.geral_A}, {self.geral_B}'

class Tabela:
    def __init__(self):
        self.tabelaHash = {}

    def inserir(self, simbolo):
        self.tabelaHash[self.horner(simbolo.nome)] = simbolo

    def delete(self, simbolo):
        self.tabelaHash.pop(self.horner(simbolo.nome), None)

    def alterar(self, nome, simbolo):
        if self.tabelaHash[self.horner(nome)] is not None:
            self.tabelaHash[self.horner(nome)] = simbolo

    def busca(self,nome):
        try:
            elemento = self.tabelaHash[self.horner(nome)]
            return elemento
        except Exception as e:
            print ('\nElemento não foi encontrado!')
    def horner(self, palavra):
        a = 37
        if len(palavra) == 1:
            return ord(palavra)
        else:
            return ord(palavra[0]) + (a * self.horner(palavra[1:]))
    def __repr__(self):
        return str(self.tabelaHash)

qtdSimbolos = 10
simbolos = []
tabela = Tabela()

## Inserir 10
print(f'-- Inserir {qtdSimbolos} simbolos --')
for i in range(qtdSimbolos):
    simbolos.append(Simbolo(f'Simbolo {i}', f'Categoria {i}', f'Nível {i}', f'geral A {i}', f'geral B {i}'))
for simbolo in simbolos:
    tabela.inserir(simbolo)
pprint.pprint(tabela.tabelaHash)

## Alterar 5
print ('\n-- Alterar 5 simbolos --')
escolhidos = []
qtdEscolhidos = 5
for i in range(qtdEscolhidos):
    escolhidos.append( simbolos[random.randint(0,len(simbolos)-1)] )
for item in escolhidos:
    item.categoria = f'{item.categoria} |alterado|'
    tabela.alterar(item.nome, item)
pprint.pprint(tabela.tabelaHash)

## Excluir 3
print ('\n-- Excluir 3 simbolos --')
escolhidos = []
qtdEscolhidos = 3
for i in range(qtdEscolhidos):
    aleatorio = random.randint(0,len(simbolos)-1)
    escolhidos.append(simbolos[aleatorio])
    simbolos.pop(aleatorio)

for item in escolhidos:
    tabela.delete(item)
pprint.pprint(tabela.tabelaHash)

## Buscar por elemento inexistente
print('\n-- Buscar Elemento Inexistente --')
tabela.busca(f'Simbolo {qtdSimbolos+1}')

## Buscar por 3 elementos que estão na tabela
print('\n-- Buscar por 3 elementos que estão na tabela --')
escolhidos = []
qtdEscolhidos = 3
for i in range(qtdEscolhidos):
    escolhidos.append( simbolos[random.randint(0,len(simbolos)-1)] )
for item in escolhidos:
    pprint.pprint(tabela.busca(item.nome))
