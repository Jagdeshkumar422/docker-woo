# from django.db import models

# class ProductMetaLookup(models.Model):
#     product_id = models.BigIntegerField(primary_key=True)  # Assuming product_id is the primary key
#     sku = models.CharField(max_length=255, null=True, blank=True)
#     virtual = models.BooleanField(default=False)
#     downloadable = models.BooleanField(default=False)
#     min_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     max_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     stock_quantity = models.IntegerField(null=True, blank=True)
#     stock_status = models.CharField(max_length=20, null=True, blank=True)
#     rating_count = models.IntegerField(null=True, blank=True)
#     average_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
#     total_sales = models.IntegerField(null=True, blank=True)

#     class Meta:
#         managed = False  # Prevent Django from modifying the table structure
#         db_table = 'wp_wc_product_meta_lookup'  # Exact table name in your database


from django.db import models

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)  # WooCommerce Product ID
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock_status = models.CharField(max_length=20)

    class Meta:
        db_table = 'wp_wc_product_meta_lookup'  # WooCommerce table
