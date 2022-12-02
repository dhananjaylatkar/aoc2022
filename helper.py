def get_input(day):
    inp = []

    with open(f"input/day_{0 if day < 10 else ''}{day}", "r") as f:
        inp = f.readlines()

    return [x.strip() for x in inp]
