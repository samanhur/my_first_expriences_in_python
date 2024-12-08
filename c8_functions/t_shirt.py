def make_shirt(size, text):
    """Making a T-shirt with specific size and text on it."""
    print(f"\nThe size of T-shirt should be: {size.upper()}")
    print(f"And the text should be: {text.title()}")


make_shirt("xl", '"just a little more..."')
make_shirt(text='"jordan"', size="xxl")
