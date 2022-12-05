def get_input(day, no_strip=False):
    inp = []

    with open(f"input/day_{0 if day < 10 else ''}{day}", "r") as f:
        inp = f.readlines()

    if no_strip:
        return inp
    return [x.strip() for x in inp]
