from time import sleep

@given(u'a tela inicial do submarino')
def step_impl(context):
    context.submarino.go_inicial()
    sleep(5)

@when(u'e selecionado o botao mais informacoes')
def step_impl(context):
    context.submarino.mais_info()
    sleep(5)

@then(u'e selecionada a opcao hoteis')
def step_impl(context):
    context.submarino.link_hoteis()
    sleep(10)


