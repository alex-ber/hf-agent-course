from unit015_tool import tool, Tool


def calculator(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b


calc_tool = Tool(name=calculator.__name__,
                 description=calculator.__doc__,
                 func=calculator,
                 arguments=[('a', 'int'), ('b', 'int')],
                 outputs='int',
                 )

print(calc_tool.to_string())


@tool
def calculator(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b


print(calculator.to_string())
