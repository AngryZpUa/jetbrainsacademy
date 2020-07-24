def heading(text, count=1):
    if count < 1:
        count = 1
    if count > 6:
        count = 6
    return "{0} {1}".format("#" * count, text)
