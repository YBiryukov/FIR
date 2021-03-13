from PIL import Image
import pandas as pd
import os
from datetime import datetime


def count_fractals(fractal_portrait, width, height):
    """ count fractals of the fractal portrait """
    fractals = get_fractal_patterns_zero_amounts()
    total_amount = 0
    for x in range(width):
        for y in range(height):
            if fractal_portrait[x][y] in fractals:
                fractals[fractal_portrait[x][y]] += 1
                total_amount += 1
    return fractals, total_amount

def create_fractal_cluster(fractals_total_amount):
    """ create cluster of fractals with the fractals_total_amount, if it doesn't exist """
    for fractal_cluster in fractal_clusters:
        if fractal_cluster["fractals_amount"] == fractals_total_amount:
            return fractal_cluster
    fractal_cluster = {
        "fractals_amount": fractals_total_amount,
        "train_fractal_portraits": []
    }
    fractal_clusters.append(fractal_cluster)
    return fractal_cluster

def create_fractal_portrait(img, width, height):
    """ create fractal portrait of the image """
    fractal_portrait = []
    for x in range(width):
        fractal_portrait.append([])
        for y in range(height):
            fractal_portrait[x].append(EMPTY_PLACE)
    return fractal_portrait

def fractal_e(fp, p_x, p_y, img, threshold, width, height):
    """ if possible, place pixel's E (East) fractal on fractal portrait """
    if (
        # NE
        ((p_x + 1) < width and (p_y - 1) >= 0 and img[p_x + 1][p_y - 1] < threshold) and
        # E
        img[p_x + 1][p_y] < threshold and
        # SE
        (p_y + 1) < height and img[p_x + 1][p_y + 1] < threshold
    ):
        fp[p_x + 1][p_y] = "E"

def fractal_n(fp, p_x, p_y, img, threshold, width, height):
    """ if possible, place pixel's N (North) fractal on fractal portrait """
    if (
        # N
        ((p_y - 1) >= 0 and img[p_x][p_y - 1] < threshold) and
        # NW
        ((p_x - 1) >= 0 and img[p_x - 1][p_y - 1] < threshold) and
        # NE
        ((p_x + 1) < width and img[p_x + 1][p_y - 1] < threshold)
    ):
        fp[p_x][p_y - 1] = "N"

def fractal_ne(fp, p_x, p_y, img, threshold, width, height):
    """ if possible, place pixel's NE (NorthEast) fractal on fractal portrait """
    if (
        # N
        ((p_y - 1) >= 0 and img[p_x][p_y - 1] < threshold) and
        # NE
        ((p_x + 1) < width and img[p_x + 1][p_y - 1] < threshold) and
        # E
        img[p_x + 1][p_y] < threshold
    ):
        fp[p_x + 1][p_y - 1] = "NE"

def fractal_nw(fp, p_x, p_y, img, threshold, width, height):
    """ if possible, place pixel's NW (NorthWest) fractal on fractal portrait """
    if (
        # N
        ((p_y - 1) >= 0 and img[p_x][p_y - 1] < threshold) and
        # NW
        ((p_x - 1) >= 0 and img[p_x - 1][p_y - 1] < threshold) and
        # W
        img[p_x - 1][p_y] < threshold
    ):
        fp[p_x - 1][p_y - 1] = "NW"

def fractal_s(fp, p_x, p_y, img, threshold, width, height):
    """ if possible, place pixel's S (South) fractal on fractal portrait """
    if (
        # S
        ((p_y + 1) < height and img[p_x][p_y + 1] < threshold) and
        # SE
        ((p_x + 1) < width and img[p_x + 1][p_y + 1] < threshold) and
        # SW
        (p_x - 1) >= 0 and img[p_x - 1][p_y + 1] < threshold
    ):
        fp[p_x][p_y + 1] = "S"

def fractal_se(fp, p_x, p_y, img, threshold, width, height):
    """ if possible, place pixel's SE (SouthEast) fractal on fractal portrait """
    if (
        # S
        ((p_y + 1) < height and img[p_x][p_y + 1] < threshold) and
        # E
        ((p_x + 1) < width and img[p_x + 1][p_y] < threshold) and
        # SE
        img[p_x + 1][p_y + 1] < threshold
    ):
        fp[p_x + 1][p_y + 1] = "SE"

def fractal_sw(fp, p_x, p_y, img, threshold, width, height):
    """ if possible, place pixel's SW (SouthWest) fractal on fractal portrait """
    if (
        # S
        ((p_y + 1) < height and img[p_x][p_y + 1] < threshold) and
        # SW
        ((p_x - 1) >= 0 and img[p_x - 1][p_y + 1] < threshold) and
        # W
        img[p_x - 1][p_y] < threshold
    ):
        fp[p_x - 1][p_y + 1] = "SW"

def fractal_w(fp, p_x, p_y, img, threshold, width, height):
    """ if possible, place pixel's W (West) fractal on fractal portrait """
    if (
        # W
        ((p_x - 1) >= 0 and img[p_x - 1][p_y] < threshold and
        # NW
        (p_y - 1) >= 0 and img[p_x - 1][p_y - 1] < threshold) and
        # SW
        ((p_y + 1) < height and img[p_x - 1][p_y + 1] < threshold)
    ):
        fp[p_x - 1][p_y] = "W"

def get_fractal_patterns_NtoS_WtoE(fractal_portrait, width, height):
    """ get all fractal patterns from fractal portrait, from North to South, from West to East """
    fractal_patterns = []
    for y in range(height):
        # single fractal pattern
        f_p = get_fractal_patterns_zero_amounts()
        for x in range(width):
            if fractal_portrait[x][y] != EMPTY_PLACE:
                f_p[fractal_portrait[x][y]] += 1
        if any(v > 0 for v in f_p.values()):
            fractal_patterns.append(f_p)
    return fractal_patterns

def get_fractal_patterns_WtoE_NtoS(fractal_portrait, width, height):
    """ get all fractal patterns from fractal portrait, from West to East, from North to South """
    fractal_patterns = []
    for x in range(width):
        # single fractal pattern
        f_p = get_fractal_patterns_zero_amounts()
        for y in range(height):
            if fractal_portrait[x][y] != EMPTY_PLACE:
                f_p[fractal_portrait[x][y]] += 1
        if any(v > 0 for v in f_p.values()):
            fractal_patterns.append(f_p)
    return fractal_patterns

def get_fractal_patterns_NtoE_WtoS(fractal_portrait, width, height):
    """ get all fractal patterns from fractal portrait, from North to East, from West to South """
    fractal_patterns = []
    x_start = width - 1
    while x_start > 0:
        x = x_start
        y = 0
        # single fractal pattern
        f_p = get_fractal_patterns_zero_amounts()
        while y < height and x < width:
            if fractal_portrait[x][y] != EMPTY_PLACE:
                f_p[fractal_portrait[x][y]] += 1
            x += 1
            y += 1
        if any(v > 0 for v in f_p.values()):
            fractal_patterns.append(f_p)
        x_start -= 1
    y_start = 0
    while y < height:
        x = x_start
        y = y_start
        while y < height and x < width:
            if fractal_portrait[x][y] != EMPTY_PLACE:
                f_p[fractal_portrait[x][y]] += 1
            x += 1
            y += 1
        if any(v > 0 for v in f_p.values()):
            fractal_patterns.append(f_p)
        y_start += 1
    return fractal_patterns

def get_fractal_patterns_NtoW_EtoS(fractal_portrait, width, height):
    """ get all fractal patterns from fractal portrait, from North to West, from East to South """
    fractal_patterns = []
    x_start = 0
    while x_start < width:
        x = x_start
        y = 0
        # single fractal pattern
        f_p = get_fractal_patterns_zero_amounts()
        while y < height and x >= 0:
            if fractal_portrait[x][y] != EMPTY_PLACE:
                f_p[fractal_portrait[x][y]] += 1
            x -= 1
            y += 1
        if any(v > 0 for v in f_p.values()):
            fractal_patterns.append(f_p)
        x_start += 1
    y_start = 1
    while y < height:
        x = x_start
        y = y_start
        while y < height and x >= 0:
            if fractal_portrait[x][y] != EMPTY_PLACE:
                f_p[fractal_portrait[x][y]] += 1
            x -= 1
            y += 1
        if any(v > 0 for v in f_p.values()):
            fractal_patterns.append(f_p)
        y_start += 1
    return fractal_patterns

def get_fractal_patterns_zero_amounts():
    """ get dict of fractal patterns with zero amounts """
    return {
        "E": 0,
        "N": 0,
        "NE": 0,
        "NW": 0,
        "S": 0,
        "SE": 0,
        "SW": 0,
        "W": 0
    }

def place_fractals(fp, img, threshold, width, height):
    """ place fractals on fractal portrait """
    for x in range(len(img)):
        for y in range(len(img[x])):
            if img[x][y] >= threshold:
                # North
                fractal_n(fp, x, y, img, threshold, width, height)
                # NortEast
                fractal_ne(fp, x, y, img, threshold, width, height)
                # East
                fractal_e(fp, x, y, img, threshold, width, height)
                # SouthEast
                fractal_se(fp, x, y, img, threshold, width, height)
                # South
                fractal_s(fp, x, y, img, threshold, width, height)
                # SouthWest
                fractal_sw(fp, x, y, img, threshold, width, height)
                # West
                fractal_w(fp, x, y, img, threshold, width, height)
                # NorthWest
                fractal_nw(fp, x, y, img, threshold, width, height)


# min value to consider pixel as non-empty
PIXEL_VALUE_THRESHOLD = 40

# character denoting empty place in a fractal portrait
EMPTY_PLACE = "."

train_master = pd.read_csv('train_master.tsv', sep='\t')

# clusters of fractals, classified by amount of fractals in a fractal portrait
fractal_clusters = []

# image width
width = 28
# image height
height = 28


i_to_print_step = 1000
i_to_print = i_to_print_step

# len_train = 10000
len_train = len(train_master['file_name'])
print(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f"))
print(f'Of {len_train}:')
for i in range(len_train):
    if (i + 1) >= i_to_print:
        print(f'    Done: {i_to_print}    {datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")}')
        i_to_print += i_to_print_step

    # get image
    image = Image.open(f'train/train_{i}.jpg')
    # image = image.resize((width, height))

    # create 2D list of pixels
    pixel_list = list(image.getdata())
    list_2d = []
    for x in range(width):
        list_2d.append([])
        for y in range(height):
            list_2d[x].append(pixel_list[width * y + x])

    # create fractal portrait of the image
    fractal_portrait = create_fractal_portrait(list_2d, width, height)
    place_fractals(fractal_portrait, list_2d, PIXEL_VALUE_THRESHOLD, width, height)
    # get West to East, North to South fractal patterns of the fractal portrait
    fractal_patterns_WtoE_NtoS = get_fractal_patterns_WtoE_NtoS(fractal_portrait, width, height)
    # get North to South, West to East fractal patterns of the fractal portrait
    fractal_patterns_NtoS_WtoE = get_fractal_patterns_NtoS_WtoE(fractal_portrait, width, height)
    # get North to West, East to South fractal patterns of the fractal portrait
    fractal_patterns_NtoW_EtoS = get_fractal_patterns_NtoW_EtoS(fractal_portrait, width, height)
    # get North to East, West to South fractal patterns of the fractal portrait
    fractal_patterns_NtoE_WtoS = get_fractal_patterns_NtoE_WtoS(fractal_portrait, width, height)

    # count fractals in the fractal portrait
    fractals_amounts, fractals_total_amount = count_fractals(fractal_portrait, width, height)

    # create and return cluster of fractals with current fractals_total_amount or
    # return existing one
    fractal_cluster = create_fractal_cluster(fractals_total_amount)

    # add data of the fractal portrait to the fractal_cluster
    fractal_cluster["train_fractal_portraits"].append({
        "digit": train_master['category_id'][i],
        "fractals_amounts": fractals_amounts,
        "fractal_patterns": {
            "WtoE_NtoS": fractal_patterns_WtoE_NtoS,
            "NtoS_WtoE": fractal_patterns_NtoS_WtoE,
            "NtoW_EtoS": fractal_patterns_NtoW_EtoS,
            "NtoE_WtoS": fractal_patterns_NtoE_WtoS
        }
    })


i_to_print_step = 100
i_to_print = i_to_print_step

if width == height:
    img_size = width

to_tsv = []

len_test = len(os.listdir("test/"))
print(datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f"))
print(f'Of {len_test}:')
for test_i in range(0, len_test):
    # get image
    image = Image.open(f'test/test_{test_i}.jpg')
    # image = image.resize((width, height))

    # create 2D list of pixels
    pixel_list = list(image.getdata())
    list_2d = []
    for x in range(width):
        list_2d.append([])
        for y in range(height):
            list_2d[x].append(pixel_list[width * y + x])

    # create fractal portrait of the image
    fractal_portrait = create_fractal_portrait(list_2d, width, height)
    place_fractals(fractal_portrait, list_2d, PIXEL_VALUE_THRESHOLD, width, height)

    # get West to East, North to South fractal patterns of the fractal portrait
    fractal_patterns_WtoE_NtoS = get_fractal_patterns_WtoE_NtoS(fractal_portrait, width, height)
    # get North to South, West to East fractal patterns of the fractal portrait
    fractal_patterns_NtoS_WtoE = get_fractal_patterns_NtoS_WtoE(fractal_portrait, width, height)
    # get North to West, East to South fractal patterns of the fractal portrait
    fractal_patterns_NtoW_EtoS = get_fractal_patterns_NtoW_EtoS(fractal_portrait, width, height)
    # get North to East, West to South fractal patterns of the fractal portrait
    fractal_patterns_NtoE_WtoS = get_fractal_patterns_NtoE_WtoS(fractal_portrait, width, height)

    # count fractals in the fractal portrait
    fractals_amounts, fractals_total_amount = count_fractals(fractal_portrait, width, height)

    # get most probable digit with similar fractal patterns
    test_fractal_portrait = {
        "fractals_amounts": fractals_amounts,
        "fractal_patterns": {
            "WtoE_NtoS": fractal_patterns_WtoE_NtoS,
            "NtoS_WtoE": fractal_patterns_NtoS_WtoE,
            "NtoW_EtoS": fractal_patterns_NtoW_EtoS,
            "NtoE_WtoS": fractal_patterns_NtoE_WtoS
        }
    }

    digit = None
    directions_len = len(test_fractal_portrait["fractal_patterns"])
    the_difference = directions_len * fractals_total_amount
    # sort fractal clusters
    fractal_clusters.sort(key = lambda x : abs(x["fractals_amount"] - fractals_total_amount))
    for fractal_cluster in fractal_clusters:
        if (abs(fractal_cluster["fractals_amount"] - fractals_total_amount) * directions_len) <= the_difference:
            for train_fractal_portrait in fractal_cluster["train_fractal_portraits"]:
                fractals_amounts_difference = 0
                for fractal_type in test_fractal_portrait["fractals_amounts"]:
                    te = fractals_amounts[fractal_type]
                    tr = train_fractal_portrait["fractals_amounts"][fractal_type]
                    fractals_amounts_difference += max(te - tr, tr - te)
                if the_difference >= (directions_len * fractals_amounts_difference):
                    difference = 0
                    for direction in test_fractal_portrait["fractal_patterns"]:
                        te = test_fractal_portrait["fractal_patterns"][direction]
                        tr = train_fractal_portrait["fractal_patterns"][direction]
                        train_direction_len = len(tr)
                        i = 0
                        while i < len(te):
                            if i < train_direction_len:
                                for fractal_type in te[i]:
                                    if te[i][fractal_type] > tr[i][fractal_type]:
                                        difference += te[i][fractal_type] - tr[i][fractal_type]
                                    elif tr[i][fractal_type] > te[i][fractal_type]:
                                        difference += tr[i][fractal_type] - te[i][fractal_type]
                            else:
                                for fractal_type in te[i]:
                                    difference += te[i][fractal_type]
                            if difference > the_difference:
                                break
                            i += 1
                        # if in tr more patterns than in te
                        while i < train_direction_len:
                            for fractal_type in tr[i]:
                                difference += tr[i][fractal_type]
                            if difference > the_difference:
                                break
                            i += 1
                if the_difference > difference:
                    the_difference = difference
                    digit = train_fractal_portrait["digit"]
                    if the_difference == 0:
                        break
    # write the image file name and the digit to tsv
    to_tsv.append([f"test_{test_i}.jpg", digit])

    if (test_i + 1) >= i_to_print:
        print(f'    Done: {i_to_print}    {datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")}')
        i_to_print += i_to_print_step
        pd.DataFrame(to_tsv).to_csv('submit.tsv', mode='a', sep='\t', index=False, header=False)
        to_tsv = []
