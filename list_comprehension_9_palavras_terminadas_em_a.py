"""
Dada uma lista de palavras, crie uma nova lista contendo apenas as palavras
que terminam com a letra "a".

palavras = ["banana", "maçã", "uva", "abacaxi", "laranja", "melancia", "kiwi", "pêra"]

Requisito: Utilize list comprehension para gerar a nova lista.

palavra.endswith('a')
"""

palavras = ["banana", "maçã", "uva", "abacaxi", "laranja", "melancia", "kiwi", "pêra"]

terminadas_em_a = [palavra for palavra in palavras if palavra.endswith(('a', 'á', 'à', 'ã', 'â'))]

print(terminadas_em_a)