@given(u'um item adicionado ao carrinho')
def step_impl(context):
    #Compra um produto
	#Buy a product
	context.product_page = product(context.driver)
	context.product_page.buy_product()

@when(u'removo este item')
def step_impl(context):
    context.sh_car.remove_item()
    pass

@then(u'uma solicitação será enviada')
def step_impl(context):
    pass