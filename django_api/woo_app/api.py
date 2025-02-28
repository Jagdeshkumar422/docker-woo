from woocommerce import API
from django.conf import settings

# WooCommerce API Configuration
wcapi = API(
    url="http://localhost:8080/wp-json/wc/v3/",  # Replace with your store URL
    consumer_key="ck_3474f59a6495b14f73cac05d4e76e9cdc8340f84",       # Replace with your WooCommerce API Key
    consumer_secret="cs_505d0bd853db8f3a93cc20ea1bede30607731aa6", # Replace with your WooCommerce Secret Key
    version="wc/v3"
)
