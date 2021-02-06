from django.urls import path
# from .views import Http, Demo, Top
from .views import apiOverviews, getAllProduct



urlpatterns = [
    # path('', Top),    # http://localhost:8000
    path('api', apiOverviews),    # http://localhost:8000/api
    path('api/products', getAllProduct),    # http://localhost:8000/api/products

    # path('api/demo', Demo),    # http://localhost:8000/api/demo
    
]
