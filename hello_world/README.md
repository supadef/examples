# example-hello-world
## Example: Hello world!
Must keep with tradition 🤪

This example builds a simple app that takes a name, and says hello to that name :)

Decorators used:```@compose```, ```@text_input```, ```@button```, ```@card```

```python
from supadef import compose, text_input, button, card

@compose(
    text_input('name'),
    button('Hello'),
    returns=card
)
def hello_world(name: str):
    return f'Hello, {name}'
```

