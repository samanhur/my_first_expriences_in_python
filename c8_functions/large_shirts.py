def make_shirt(size="large", text='"I love Python"'):
    """making a T-shirt with specific size and text on it."""
    print(f"\nThe size of T-shirt should be: {size.upper()}")
    print(f"And the text should be: {text.title()}")


make_shirt()
make_shirt(size="medium")
make_shirt("small", "new york")
