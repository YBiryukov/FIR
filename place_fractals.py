from .images.0-9 import digits


def fractal_n(p_x, p_y, img):
    """ if possible, place pixel's N fractal on image """
    if (
        # N
        ((p_y - 1) >= 0 and img[p_y - 1][p_x] != "1") and
        # NW
        ((p_x - 1) >= 0 and img[p_y - 1][p_x - 1] != "1") and
        # W
        img[p_y][p_x - 1] != "1" and
        # NE
        ((p_x + 1) < len(img) and img[p_y - 1][p_x + 1] != "1") and
        # E
        img[p_y][p_x + 1] != "1"
    ):
        img[p_y - 1][p_x] = "N"

def fractal_e(p_x, p_y, img):
    """ if possible, place pixel's E fractal on image """
    if (
        # N
        ((p_y - 1) >= 0 and img[p_y - 1][p_x] != "1") and
        # NE
        ((p_x + 1) < len(img) and img[p_y - 1][p_x + 1] != "1") and
        # E
        img[p_y][p_x + 1] != "1" and
        # S
        ((p_y + 1) < len(img) and img[p_y + 1][p_x] != "1") and
        # SE
        img[p_y + 1][p_x + 1] != "1"
    ):
        img[p_y][p_x + 1] = "E"

def fractal_s(p_x, p_y, img):
    """ if possible, place pixel's S fractal on image """
    if (
        # S
        ((p_y + 1) < len(img) and img[p_y + 1][p_x] != "1") and
        # SE
        ((p_x + 1) < len(img) and img[p_y + 1][p_x + 1] != "1") and
        # E
        img[p_y][p_x + 1] != "1" and
        # W
        ((p_x - 1) >= 0 and img[p_y][p_x - 1] != "1") and
        # SW
        img[p_y + 1][p_x - 1] != "1"
    ):
        img[p_y + 1][p_x] = "S"

def fractal_w(p_x, p_y, img):
    """ if possible, place pixel's W fractal on image """
    if (
        # N
        ((p_y - 1) >= 0 and img[p_y - 1][p_x] != "1") and
        # NW
        ((p_x - 1) >= 0 and img[p_y - 1][p_x - 1] != "1") and
        # W
        img[p_y][p_x - 1] != "1" and
        # SW
        ((p_y + 1) < len(img) and img[p_y + 1][p_x - 1] != "1") and
        # S
        img[p_y + 1][p_x] != "1"
    ):
        img[p_y][p_x - 1] = "W"

def fractal_ne(p_x, p_y, img):
    """ if possible, place pixel's NE fractal on image """
    if (
        # N
        ((p_y - 1) >= 0 and img[p_y - 1][p_x] != "1") and
        # NW
        ((p_x - 1) >= 0 and img[p_y - 1][p_x - 1] != "1") and
        # NE
        ((p_x + 1) < len(img) and img[p_y - 1][p_x + 1] != "1") and
        # SE
        ((p_y + 1) < len(img) and img[p_y + 1][p_x + 1] != "1") and
        # E
        img[p_y][p_x + 1] != "1"
    ):
        img[p_y - 1][p_x + 1] = "NE"

def fractal_se(p_x, p_y, img):
    """ if possible, place pixel's SE fractal on image """
    if (
        # S
        ((p_y + 1) < len(img) and img[p_y + 1][p_x] != "1") and
        # SW
        ((p_x - 1) >= 0 and img[p_y + 1][p_x - 1] != "1") and
        # E
        ((p_x + 1) < len(img) and img[p_y][p_x + 1] != "1") and
        # NE
        ((p_y - 1) >= 0 and img[p_y - 1][p_x + 1] != "1") and
        # SE
        img[p_y + 1][p_x + 1] != "1"
    ):
        img[p_y + 1][p_x + 1] = "SE"

def fractal_sw(p_x, p_y, img):
    """ if possible, place pixel's SW fractal on image """
    if (
        # S
        ((p_y + 1) < len(img) and img[p_y + 1][p_x] != "1") and
        # SW
        ((p_x - 1) >= 0 and img[p_y + 1][p_x - 1] != "1") and
        # W
        img[p_y][p_x - 1] != "1" and
        # NW
        ((p_y - 1) >= 0 and img[p_y - 1][p_x - 1] != "1") and
        # SE
        ((p_x + 1) < len(img) and img[p_y + 1][p_x + 1] != "1")
    ):
        img[p_y + 1][p_x - 1] = "SW"

def fractal_nw(p_x, p_y, img):
    """ if possible, place pixel's NW fractal on image """
    if (
        # N
        ((p_y - 1) >= 0 and img[p_y - 1][p_x] != "1") and
        # NE
        ((p_x + 1) < len(img) and img[p_y - 1][p_x + 1] != "1") and
        # NW
        ((p_x - 1) >= 0 and img[p_y - 1][p_x - 1] != "1") and
        # SW
        ((p_y + 1) < len(img) and img[p_y + 1][p_x - 1] != "1") and
        # W
        img[p_y][p_x - 1] != "1"
    ):
        img[p_y - 1][p_x - 1] = "NW"

def place_fractals(img):
    """ place fractals on image """
    for y in range(len(img)):
        for x in range(len(img[y])):
            if img[y][x] == "1":
                fractal_n(x, y, img)
                fractal_ne(x, y, img)
                fractal_e(x, y, img)
                fractal_se(x, y, img)
                fractal_s(x, y, img)
                fractal_sw(x, y, img)
                fractal_w(x, y, img)
                fractal_nw(x, y, img)


for digit in digits:
    # prepare image
    img = []
    for row in digit:
        img.append(row.split())
    # place fractals on prepared image
    place_fractals(img)
    print(img)
