from rest_framework.decorators import api_view
from rest_framework.response import Response
from .api import wcapi

# ✅ Retrieve all products
@api_view(['GET'])
def get_products(request):
    response = wcapi.get("products")
    if response.status_code == 200:
        return Response(response.json())
    return Response({"error": "Failed to fetch products"}, status=400)

# ✅ Retrieve a single product by ID
@api_view(['GET'])
def get_product_by_id(request, product_id):
    response = wcapi.get(f"products/{product_id}")
    if response.status_code == 200:
        return Response(response.json())
    return Response({"error": "Product not found"}, status=404)

# ✅ Create a product with an image
@api_view(['POST'])
def create_product(request):
    data = request.data
    woo_product = {
        "name": data.get("name"),
        "type": "simple",  
        "regular_price": str(data.get("price")),  # WooCommerce requires string format
        "description": data.get("description"),
        "stock_status": data.get("stock_status"),
        "images": [{"src": data.get("image_url")}] if data.get("image_url") else []  # Adding image support
    }

    response = wcapi.post("products", woo_product)

    # Debugging - Print response from WooCommerce
    print("WooCommerce API Response:", response.status_code, response.json())

    if response.status_code == 201:
        return Response(response.json(), status=201)
    
    return Response({"error": "Failed to create product", "details": response.json()}, status=400)

# ✅ Update a product (including image)
@api_view(['PUT'])
def update_product(request, product_id):
    data = request.data
    woo_product = {
        "name": data.get("name"),
        "regular_price": str(data.get("price")),
        "description": data.get("description"),
        "stock_status": data.get("stock_status"),
        "images": [{"src": data.get("image_url")}] if data.get("image_url") else []  # Updating image if provided
    }

    response = wcapi.put(f"products/{product_id}", woo_product)

    if response.status_code == 200:
        return Response(response.json())

    return Response({"error": "Failed to update product", "details": response.json()}, status=400)

# ✅ Delete a product
@api_view(['DELETE'])
def delete_product(request, product_id):
    response = wcapi.delete(f"products/{product_id}", params={"force": True})

    if response.status_code == 200:
        return Response({"message": "Product deleted successfully!"})

    return Response({"error": "Failed to delete product"}, status=400)
