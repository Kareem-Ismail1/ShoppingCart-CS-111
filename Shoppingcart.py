# Product data for testing
products = {
    "ABC": {
        "categories": ["food", "electronics"],
        "name": "laptop",
        "weight": 5.0,
        "price": 650.00,
        "currency": "USD",
        "notes": "lots of features"
    },
    "DEF": {
        "categories": ["electronics"],
        "name": "TV",
        "weight": 15.0,
        "price": 550.00,
        "currency": "USD",
        "notes": "lots of features"
    }
}


def getProductsBySearch(products, searchTerm):
    """
    Searches product name and notes for searchTerm.
    Search is case-insensitive.
    Returns a list of product codes or an empty list.
    """
    matchingProducts = []
    searchTerm = searchTerm.lower()

    for productCode, productInfo in products.items():
        name = productInfo["name"].lower()
        notes = productInfo["notes"].lower()

        if searchTerm in name or searchTerm in notes:
            matchingProducts.append(productCode)

    return matchingProducts


def getProductsByCategory(products, categoryName):
    """
    Returns a list of product codes for the category name.
    Returns an empty list if no matches are found.
    """
    matchingProducts = []
    categoryName = categoryName.lower()

    for productCode, productInfo in products.items():
        categories = [category.lower() for category in productInfo["categories"]]

        if categoryName in categories:
            matchingProducts.append(productCode)

    return matchingProducts


def getProductCategories(products):
    """
    Returns a sorted list of all unique category names.
    """
    categories = set()

    for productInfo in products.values():
        for category in productInfo["categories"]:
            categories.add(category)

    return sorted(categories)


def getProductPrice(products, productCode):
    """
    Returns product price in USD as a float.
    """
    if productCode in products:
        return float(products[productCode]["price"])

    return None


# ---------------- TESTING ----------------
print(getProductsBySearch(products, "lap"))          # ['ABC']
print(getProductsBySearch(products, "features"))     # ['ABC', 'DEF']

print(getProductsByCategory(products, "electronics"))  # ['ABC', 'DEF']
print(getProductsByCategory(products, "food"))         # ['ABC']

print(getProductCategories(products))  # ['electronics', 'food']

print(getProductPrice(products, "ABC"))  # 650.0
print(getProductPrice(products, "DEF"))  # 550.0