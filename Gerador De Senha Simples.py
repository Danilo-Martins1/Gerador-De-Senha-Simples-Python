import string
from random import choice

tamanho_senha = int(input('Digitos Da Senha: '))
caracteres = string.ascii_letters + string.digits + string.punctuation
senha = ''

for i in range(tamanho_senha):
    senha += choice(caracteres)

print('Nova Senha Gerada: ', senha)
