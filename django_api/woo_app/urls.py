
# from django.urls import path
# from .views import  get_products,get_productById,create_product,  update_product, delete_product

# urlpatterns = [
#     path('products/', get_products, name="get_products"),
#     path('products/<int:product_id>/', get_productById, name="get_products"),
#     path('products/create/', create_product, name="create_product"),
#     path('products/update/<int:product_id>/', update_product, name="update_product"),
#     path('products/delete/<int:product_id>/', delete_product, name="delete_product"),
# ]


from django.urls import path
from .views import  get_products, create_product, delete_product, update_product, get_product_by_id

urlpatterns = [
    path('products/<int:product_id>/', get_product_by_id, name="get_products"),
    path('products/', get_products, name="get_products"),
    path('products/create/', create_product, name="create_products"),
    path('products/update/<int:product_id>/', update_product, name="update_product"),
    path('products/delete/<int:product_id>/', delete_product, name="delete_product"),
]
