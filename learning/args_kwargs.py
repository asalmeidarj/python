'''
    Explorando o uso de *args e **kwargs
'''

def produto(produto, *args):
    '''função exibi o nome do produto e seus preços'''
    print(f'O produto {produto}:')
    i = 0
    for arg in args:
        i += 1
        print(f'Preço {i}: {arg}')

def valor1(arg, **kwargs): 
    '''Função retorna o valor com taxas e desconto caso haja
     Exemplo1: valor(100, **{'taxa': 0.1, 'desconto': 15})
     Exemplo2: valor(100, taxa=0.1, desconto=10)
    '''
    valor = arg
    taxa = kwargs.get('taxa')
    desconto = kwargs.get('desconto')
    if taxa:
        valor = valor * (1 + taxa)
    if desconto:
        valor = valor - desconto
    print(valor)

def valor2(arg, **kwargs): 
    '''Função retorna o valor com taxas e desconto caso haja.
     Exemplo1: valor(100, **{'taxa': 0.1, 'desconto': 15})
     Exemplo2: valor(100, taxa=0.1, desconto=15)
    '''
    valor = arg
    for k, v in kwargs.items():
        if k=='taxa':
            valor = valor * (1 + v)
        if k=='desconto':
            valor = valor - v
    print(valor)

    
#####################      FIM      #########################
