from CGComponents import *

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300


def clip_test(p, q, u1, u2):
    result = True
    if p < 0.0:
        r = q / p
        if r > u2:
            result = False
        elif r > u1:
            u1 = r
    elif p > 0.0:
        r = q / p
        if r < u1:
            result = False
        elif r < u2:
            u2 = r
    elif q < 0.0:
        result = False

    return u1, u2, result


def liang_barsky(point_bottom_left, point_top_right, line):
    u1 = 0.0
    u2 = 1.0

    x_min = point_bottom_left.x
    x_max = point_top_right.x
    y_min = point_bottom_left.y
    y_max = point_top_right.y

    dx = line.p2.x - line.p1.x
    dy = line.p2.y - line.p1.y

    u1, u2, result = clip_test(-dx, line.p1.x - x_min, u1, u2)
    if result:
        u1, u2, result = clip_test(dx, x_max - line.p1.x, u1, u2)
        if result:
            u1, u2, result = clip_test(-dy, line.p1.y - y_min, u1, u2)
            if result:
                u1, u2, result = clip_test(dy, y_max - line.p1.y, u1, u2)
                if result:
                    if u2 < 1.0:
                        line.p2.x = line.p1.x + (u2 * dx)
                        line.p2.y = line.p1.y + (u2 * dy)
                    if u1 > 0.0:
                        line.p1.x = line.p1.x + (u1 * dx)
                        line.p1.y = line.p1.y + (u1 * dy)
                    print('x1:{0}   y1:{1}  x2:{2}  y2:{3}'.format(line.p1.x, line.p1.y, line.p2.x, line.p2.y))


def main():
    rect_bottom_left = Point2D(0, 0)
    rect_top_right = Point2D(10, 10)

    line_1 = Line2D(Point2D(-5, 3), Point2D(15, 9))
    liang_barsky(rect_bottom_left, rect_top_right, line_1)

    input('Press <enter> to close')


if __name__ == "__main__":
    main()
