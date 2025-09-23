def run(a: int, b: int, c: int) -> tuple:
    x1 = (-b + ((b**2 - 4 * a * c)**0.5)) / (2 * a)
    x2= (-b - ((b**2 - 4 * a * c)**0.5)) / (2 * a)

    return x1, x2


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
