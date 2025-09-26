import math
def run(arc_A: float) -> float:
    radio = ((4*arc_A)/(2*round(math.pi,2)))
    area = round(radio**2, 10)
    return area


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
