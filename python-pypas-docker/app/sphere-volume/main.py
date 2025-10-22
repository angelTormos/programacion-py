import math
def run(radius: float) -> float:
    volume = (4 / 3) * round(math.pi, 2) * radius**3
    return volume


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
