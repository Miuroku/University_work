from django.shortcuts import render
from django.contrib.auth.models import User
from first_app.models import Product
from recommendations.models import StatisticsItem
import numpy as np
from django.contrib import messages

from recommendations.recommendations_logic.predictions_logic import get_recommendations, DEBUG, Independent_Prediction_Element
from recommendations.adapter import Recomendations_Django_Adapter, product_with_prediction
import logging

logger = logging.getLogger(__name__)

def recommendations(request):
    
    # 1) Convert data to valid format.
    users = User.objects.all()
    current_user = request.user
    products = Product.objects.all()

    # Using adapter here for correct converting data form django DB to recommendations app and back.
    adapter = Recomendations_Django_Adapter()
    current_user_index = -1
    data_new = adapter.from_users_products_statistics_to_matrix(users=users, current_user=current_user, products=products, current_user_index=current_user_index)    

    try:
        product_recommendations = get_recommendations(data_new, current_user_index, k=2)
    except Exception as ex:
        logger.error('recommendations was not get')
        messages.error(request, 'error: ' + str(ex))

    if DEBUG:
        logger.info('Recommendations geted !')            

    # Gettin related products.
    products_recommended = adapter.from_predictions_to_django(product_recommendations=product_recommendations, products=products)

    if DEBUG:
        try:
            logger.debug(f'PRODUCTS RECOMMENDED: {products_recommended[0].pred_obj.prediction}')            
        except:
            logger.warning('THERE IS NO PRODUCTS FOR RECOMMENDATION!')         

    context = {'pe': product_recommendations, 'products': products_recommended}
    return render(request, 'recommendations/recommendations.html', context=context)