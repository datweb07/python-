# Danh sách dữ liệu khách hàng
customers = [
    {"name": "K1", "purchases": 4, "spending": 150},
    {"name": "K2", "purchases": 2, "spending": 80},
    {"name": "K3", "purchases": 6, "spending": 200},
    {"name": "K4", "purchases": 3, "spending": 120},
    {"name": "K5", "purchases": 7, "spending": 220},
    {"name": "K6", "purchases": 5, "spending": 170},
    {"name": "K7", "purchases": 2, "spending": 90},
    {"name": "K8", "purchases": 1, "spending": 50},
    {"name": "K9", "purchases": 4, "spending": 160},
    {"name": "K10", "purchases": 3, "spending": 110},
]


# Hàm phân loại
def classify_customer(purchases, spending):
    if purchases > 5:
        purchase_category = "Nhiều"
    elif 3 <= purchases <= 5:
        purchase_category = "Trung bình"
    else:
        purchase_category = "Ít"

    if spending > 150:
        spending_category = "Cao"
    elif 100 <= spending <= 150:
        spending_category = "Trung bình"
    else:
        spending_category = "Thấp"

    return purchase_category, spending_category


# Phân loại khách hàng và tìm khách hàng tiềm năng nhất
potential_customers = []
for customer in customers:
    purchase_category, spending_category = classify_customer(customer["purchases"], customer["spending"])
    print(f"Khách hàng {customer['name']}: Số lần mua hàng - {purchase_category}, Tổng chi tiêu - {spending_category}")

    # Lọc khách hàng tiềm năng (Mua nhiều và chi tiêu cao)
    if purchase_category == "Nhiều" and spending_category == "Cao":
        potential_customers.append(customer["name"])

print("\nKhách hàng tiềm năng nhất:", potential_customers)
