from django.shortcuts import render
from django.contrib.auth.models import User
from first_app.models import Product
from recommendations.models import StatisticsItem
import numpy as np
from django.contrib import messages

from recommendations.recommendations_logic.predictions_logic import get_recommendations, DEBUG, Independent_Prediction_Element

def recommendations(request):
    
    # 1) Convert data to valid format.
    users = User.objects.all()
    current_user = request.user
    products = Product.objects.all()
    
    data = []

    if DEBUG:
        print('USERS:')
    current_user_index = -1
    for i in range(len(users)):
        new_line = []
        # вычисляем индекс текущего пользователя.
        if users[i] == current_user:
            current_user_index = i
        for j in range(len(products)):
            new_element = StatisticsItem.objects.get(user=users[i], product=products[j])
            new_line.append(new_element.clicks)
        if DEBUG:
            print(f'users[{i}] = (name: {users[i].username}); (id: {users[i].id})')
        data.append(new_line)
    data_new = np.copy(data)
    if DEBUG:
        print('PRODUCTS:')  
        for i in range(len(products)):
            print(f'products[{i}] = (name: {products[i].title}); (id: {products[i].id})')
        print(f'CURRENT_USER_INDEX: {current_user_index}')

    try:
        product_recommendations = get_recommendations(data_new, current_user_index, k=2)
    except Exception as ex:
        messages.error(request, 'error: ' + str(ex))

    if DEBUG:
        print('RECOMMENDETIONS GETED.')

    # Gettin related products.
    products_recommended = []
    for i in range(len(product_recommendations)):
        index = product_recommendations[i].j_product
        current_product = products[index]
        test_object = product_with_prediction(product_recommendations[i], current_product)
        products_recommended.append(test_object)

    if DEBUG:
        try:
            print(f'PRODUCTS RECOMMENDED: {products_recommended[0].pred_obj.prediction}')
        except:
            print(f'kek')

    context = {'pe': product_recommendations, 'products': products_recommended}
    return render(request, 'recommendations/recommendations.html', context=context)

class product_with_prediction(object):
    def __init__(self, prediction_obj, product):
        self.pred_obj = prediction_obj
        self.product = product