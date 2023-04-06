from supadef import compose, text_input, button, card


@compose(
    text_input('name'),
    button('Hello'),
    returns=card
)
def hello_world(name: str):
    return f'Hello, {name}'

