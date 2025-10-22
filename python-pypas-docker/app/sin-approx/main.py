def run(x: float) -> float:
    sin = (4 * x * (180 - x) / (40500 - x * (180 - x)))
    return sin


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
