def read_value(prompt, converter=str, default_value=None):
    try:
        return converter(input(prompt))
    except:
        return default_value