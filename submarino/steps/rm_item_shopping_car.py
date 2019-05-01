@given(u'um item adicionado no Carrinho')
def step_impl(context):
    context.sh_car.add_item()
    
@when(u'removo este item')
def step_impl(context):
    context.sh_car.remove_item()

@then(u'uma solicitação será enviada')
def step_impl(context):
    context.sh_car.reflesh()
    context.wait_seg(context.driver, 3) #Espera de três segundos
    element = context.driver.find_element_by_xpath('/html/body/div[4]/section/section/div[1]')
    inner_element = element.find_element_by_xpath('/html/body/div[4]/section/section/div[1]/section/h2')
    assert inner_element.text == 'Seu carrinho está vazio'