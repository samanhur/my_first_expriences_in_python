def sandwich_orders(*items):
    """Making sandwich with given items."""
    print(f"\nI'll make your sandwich: ")
    for item in items:
        print(f"\t adding {item} to your sandwich.")
    print("Your sandwich is ready!")


sandwich_orders("cheese", "mushrooms", "hotdog")
sandwich_orders("hamburger")
sandwich_orders("falafel", "sausage")
