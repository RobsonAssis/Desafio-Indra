#language: pt

Funcionalidade: Remover item de carrinho de compras
    Cenário: Carrinho de compras
        Dado um item adicionado no carrinho
        E dentro do carrinho
        Quando removo este item
        Então uma solicitação será enviada
        