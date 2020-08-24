from CGComponents import *

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300


def draw_pixel(p):
    if p.x < 0 or p.x > SCREEN_WIDTH or p.y < 0 or p.y > SCREEN_HEIGHT:
        raise Exception('Point out of screen bounds')

    print('x:{0}    y:{1}'.format(p.x, p.y))


INSIDE = 0  # 0000
LEFT = 1  # 0001
RIGHT = 2  # 0010
BOTTOM = 4  # 0100
TOP = 8  # 1000


def find_code(p, x_min, x_max, y_min, y_max):
    code = INSIDE
    if p.x < x_min:
        code |= LEFT
    elif p.x > x_max:
        code |= RIGHT
    if p.y < y_min:
        code |= BOTTOM
    elif p.y > y_max:
        code |= TOP

    return code


def cohenSutherlandClip(point_bottom_left, point_top_right, line):
    x_min = point_bottom_left.x
    x_max = point_top_right.x
    y_min = point_top_right.y
    y_max = point_bottom_left.y

    while True:
        code_1 = find_code(line.p1, x_min, x_max, y_min, y_max)
        code_2 = find_code(line.p2, x_min, x_max, y_min, y_max)

        if code_1 == 0 and code_2 == 0:
            # line is fully INSIDE the given rectangle
            accept = True
            break
        elif code_1 & code_2 != 0:
            # line is fully OUTSIDE the given rectangle
            accept = False
            break
        else:
            # line is partially INSIDE the given rectangle
            code_out = code_1 if code_1 != 0 else code_2

            if code_out & TOP:
                x = line.p1.x + (line.p2.x - line.p1.x) * (y_max - line.p1.y) / (line.p2.y - line.p1.y)
                y = y_max
            elif code_out & BOTTOM:
                x = line.p1.x + (line.p2.x - line.p1.x) * (y_min - line.p1.y) / (line.p2.y - line.p1.y)
                y = y_min
            elif code_out & RIGHT:
                y = line.p1.y + (line.p2.y - line.p1.y) * (x_max - line.p1.x) / (line.p2.x - line.p1.x)
                x = x_max
            elif code_out & LEFT:
                y = line.p1.y + (line.p2.y - line.p1.y) * (x_min - line.p1.x) / (line.p2.x - line.p1.x)
                x = x_min

            if code_out == code_1:
                line.p1 = Point2D(x, y)
                code_1 = find_code(line.p1, x_min, x_max, y_min, y_max)
            else:
                line.p2 = Point2D(x, y)
                code_2 = find_code(line.p2, x_min, x_max, y_min, y_max)

    if accept:
        print('Line accepted from [{0}, {1}] to [{2}, {3}]'.format(line.p1.x, line.p1.y, line.p2.x, line.p2.y))
    else:
        print('Line rejected!')


def main():
    rect_bottom_left = Point2D(-1, 8)
    rect_top_right = Point2D(6, 4)

    line_1 = Line2D(Point2D(1, 10), Point2D(4, 2))
    cohenSutherlandClip(rect_bottom_left, rect_top_right, line_1)

    line_2 = Line2D(Point2D(1, 10), Point2D(0, 3))
    cohenSutherlandClip(rect_bottom_left, rect_top_right, line_2)

    input('Press <enter> to close')


if __name__ == "__main__":
    main()
