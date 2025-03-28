import json

with open("products.json", "r", encoding="utf-8") as f:
    product_data = json.load(f)

print("Dữ liệu sản phẩm:", product_data)  # Kiểm tra JSON có nạp đúng không
