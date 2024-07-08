def detect_collision(rect_1, rect_2)->bool:
    """_summary_

    Args:
        rect_1 (_type_): _description_
        rect_2 (_type_): _description_

    Returns:
        bool: _description_
    """
    if point_in_rect(rect_1.topleft, rect_2) or \
        point_in_rect(rect_1.topright, rect_2) or \
        point_in_rect(rect_1.bottomleft, rect_2) or \
        point_in_rect(rect_1.bottomright, rect_2):
        return True

    elif point_in_rect(rect_2.topleft, rect_1) or \
        point_in_rect(rect_2.topright, rect_1) or \
        point_in_rect(rect_2.bottomleft, rect_1) or \
        point_in_rect(rect_2.bottomright, rect_1):
        return True
    else:
        return False

def point_in_rect(point: tuple, rect)->bool:
    """_summary_

    Args:
        point (tuple): _description_
        rect (_type_): _description_

    Returns:
        bool: _description_
    """
    x, y = point
    return x >= rect.left and x <= rect.right and y >= rect.top and y <= rect.bottom



def detect_collisions_circle(rect_1, rect_2):
    distancia = distance_between_centers_rect(rect_1, rect_2)
    r1 = calculate_radius_rect(rect_1)
    r2 = calculate_radius_rect(rect_2)
    return distancia <= (r1 + r2)

def distance_between_points(point_1: tuple, point_2: tuple):
    from math import sqrt
    x1, y1 = point_1
    x2, y2 = point_2
    return sqrt((y1 - y2) ** 2 + (x1 - x2) ** 2)

def calculate_radius_rect(rect):
    return rect.width // 2

def distance_between_centers_rect(rect_1, rect_2):
    return distance_between_points(rect_1.center, rect_2.center)





