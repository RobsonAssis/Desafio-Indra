#language: pt

   Funcionalidade: Fazer login  e silumar uma compra
   Cenario: Usuario seleciona produto e simula uma compra
      Dado que o usuario está no site
      Quando Realiza uma pesquisa de Motorola
      E Seleciona um Celular 
      E Calcular o cep
      Então prosseguir para a pagina de compra
       