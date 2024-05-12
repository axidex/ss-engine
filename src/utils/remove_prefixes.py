def remove_prefixes(value: str, prefixes: list[str]) -> str:
    """"""

    for prefix in prefixes:
        value = value.removeprefix(prefix)

    return value
