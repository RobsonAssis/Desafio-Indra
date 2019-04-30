@given(u'que o usuario está no site')
def step_impl(context):
    context.Submarino_page.go_home()

@when(u'Realiza uma pesquisa de Motorola')
def step_impl(context):
    context.Submarino_page.pesquisar_c()

@when(u'Seleciona um Celular')
def step_impl(context):
    context.Submarino_page.selecionar_c()


@when(u'Calcular o cep')
def step_impl(context):
    context.Submarino_page.calcular_cep()

@then(u'prosseguir para a pagina de compra')
def step_impl(context):
    context.Submarino_page.comprar()
    context.Submarino_page.continuar()