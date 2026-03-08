# product_analytics.py
# Day 9 PM – Part A: Product Analytics Tool (Tuples & Sets)

from collections import namedtuple

# ─────────────────────────────────────────────
# 1. Named Tuple Definition
# ─────────────────────────────────────────────
Product = namedtuple("Product", ["id", "name", "category", "price"])

# ─────────────────────────────────────────────
# 2. Product Catalog (15+ products, 4 categories)
# ─────────────────────────────────────────────
catalog = [
    # Electronics
    Product(1,  "Laptop",           "Electronics", 75000),
    Product(2,  "Smartphone",       "Electronics", 45000),
    Product(3,  "Wireless Earbuds", "Electronics", 3500),
    Product(4,  "Smart Watch",      "Electronics", 12000),
    Product(5,  "Tablet",           "Electronics", 30000),
    # Clothing
    Product(6,  "Running Shoes",    "Clothing",    2500),
    Product(7,  "Denim Jacket",     "Clothing",    1800),
    Product(8,  "Sports T-Shirt",   "Clothing",    699),
    Product(9,  "Formal Trousers",  "Clothing",    1200),
    # Books
    Product(10, "Clean Code",       "Books",       699),
    Product(11, "Python Crash Course","Books",     499),
    Product(12, "Atomic Habits",    "Books",       399),
    Product(13, "The Pragmatic Programmer","Books",799),
    # Home
    Product(14, "Air Purifier",     "Home",        8999),
    Product(15, "Electric Kettle",  "Home",        1299),
    Product(16, "LED Desk Lamp",    "Home",        599),
]

# Quick lookup by id
catalog_by_id = {p.id: p for p in catalog}

# ─────────────────────────────────────────────
# 3. Customer Cart Sets
# ─────────────────────────────────────────────
p = catalog_by_id   # shorthand

customer_1_cart = {p[1], p[2],  p[10], p[14], p[6]}
customer_2_cart = {p[1], p[3],  p[11], p[15], p[7]}
customer_3_cart = {p[1], p[4],  p[10], p[12], p[8]}
customer_4_cart = {p[1], p[5],  p[11], p[13], p[16]}
customer_5_cart = {p[1], p[2],  p[12], p[14], p[9]}

all_carts = [
    customer_1_cart,
    customer_2_cart,
    customer_3_cart,
    customer_4_cart,
    customer_5_cart,
]

# ─────────────────────────────────────────────
# 4. Shopping Behaviour Analysis
# ─────────────────────────────────────────────

# (a) Bestsellers — products in ALL carts
def bestsellers() -> set:
    """Products appearing in every customer's cart — set intersection."""
    result = all_carts[0].copy()
    for cart in all_carts[1:]:
        result = result.intersection(cart)
    return result


# (b) Catalog Reach — products in ANY cart
def catalog_reach() -> set:
    """All products purchased by at least one customer — set union."""
    result = set()
    for cart in all_carts:
        result = result.union(cart)
    return result


# (c) Exclusive Purchases — only customer_1 bought
def exclusive_purchases(cart: set, other_carts: list) -> set:
    """Products bought only by this customer — set difference against all others."""
    others_combined = set()
    for c in other_carts:
        others_combined = others_combined.union(c)
    return cart - others_combined


# ─────────────────────────────────────────────
# 5. Product Recommendation
# ─────────────────────────────────────────────
def recommend_products(customer_cart: set, all_carts: list) -> set:
    """
    Suggest products other customers bought but this customer hasn't.
    Uses set difference: (union of all other carts) - customer_cart
    """
    others = set()
    for cart in all_carts:
        if cart != customer_cart:
            others = others.union(cart)
    return others - customer_cart


# ─────────────────────────────────────────────
# 6. Category Summary
# ─────────────────────────────────────────────
def category_summary() -> dict:
    """
    Return a dict mapping each category to a set of product names.
    Uses set comprehension.
    """
    categories = {p.category for p in catalog}   # set comprehension for unique categories
    return {
        cat: {p.name for p in catalog if p.category == cat}
        for cat in categories
    }


# ─────────────────────────────────────────────
# Display Helpers
# ─────────────────────────────────────────────
def format_products(products: set) -> str:
    if not products:
        return "  (none)"
    return "\n".join(f"    • [{p.id:02}] {p.name:<30} ₹{p.price:,}" for p in sorted(products, key=lambda x: x.id))


# ─────────────────────────────────────────────
# Main Demo
# ─────────────────────────────────────────────
if __name__ == "__main__":
    print("=" * 55)
    print("  🛒  E-Commerce Product Analytics Tool")
    print("=" * 55)

    print("\n📦  Catalog size:", len(catalog), "products")

    print("\n🏆  Bestsellers (in ALL carts):")
    print(format_products(bestsellers()))

    print("\n🌐  Catalog Reach (in ANY cart):")
    print(format_products(catalog_reach()))

    print("\n🎯  Exclusive to Customer 1:")
    others = [customer_2_cart, customer_3_cart, customer_4_cart, customer_5_cart]
    print(format_products(exclusive_purchases(customer_1_cart, others)))

    print("\n💡  Recommendations for Customer 1:")
    recs = recommend_products(customer_1_cart, all_carts)
    print(format_products(recs))

    print("\n📂  Category Summary:")
    for cat, names in sorted(category_summary().items()):
        print(f"    {cat}: {names}")
