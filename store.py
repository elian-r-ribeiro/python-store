produtos = [
    ('Mouse Redragon Cobra Chroma', 99.99, 243),
    ('Teclado mecânico Razer BlackWidow', 1499.99, 224),
    ('Monitor Samsung Odyssey G9', 9605.55, 30),
    ('Gabinete Gamer Rise Mode Galaxy Glass', 799.99, 124),
    ('Pny Geforce RTX 4090 24GB GDDR6X', 11999.99, 3)
]

formas_pagamento = [
    ('PIX'),
    ('Cartão de crédito'),
    ('Boleto bancário'),
    ('Cartão de débito')
]

def mercado():
    print("Produtos disponíveis:")
    for i, produto in enumerate(produtos):
        print(f"================================ \n[{i+1}] Produto: {produto[0]} \nR${produto[1]:.2f} \nEstoque: {produto[2]}")
    print("================================")
    
    while True:
        escolha_produto = int(input("Digite o número do produto que deseja comprar: "))
        
        if escolha_produto > len(produtos):
            print('Produto inválido, por favor digite novamente')
        else:
            produto_escolhido = produtos[escolha_produto - 1]
            valor_produto_uni = produto_escolhido[1]
            break
        
    quantidade_estoque = produto_escolhido[2]
    
    while True:
        escolha_quantidade = int(input("Digite quantos produtos deseja comprar do mesmo: "))
        if escolha_quantidade > quantidade_estoque:
            print('Quantidade desejada maior que quantidade em estoque, tente novamente')
        else:
            valor_final = valor_produto_uni * escolha_quantidade
            print(f"Você comprou {escolha_quantidade} unidades do produto {produto_escolhido[0]}. \nValor final: R${valor_final:.2f}")
            break
    
    metodo_pagamento = int(input('Qual a forma de pagamento? \n'))
    
if __name__ == '__main__':
    mercado()
