from CGComponents import *

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300


def draw_pixel(p):
    if p.x < 0 or p.x > SCREEN_WIDTH or p.y < 0 or p.y > SCREEN_HEIGHT:
        raise Exception('Point out of screen bounds')

    print('x:{0}    y:{1}'.format(p.x, p.y))


def bresenham(p1, p2):
    dx = abs(p1.x - p2.x)
    dy = abs(p1.y - p2.y)
    p = (2 * dy) - dx

    steps = abs(p1.y - p2.y) if p1.x == p2.x else abs(p1.x - p2.x)
    if p2.x - p1.x > 0:
        x_increase = 1
    elif p2.x - p1.x < 0:
        x_increase = -1
    else:
        x_increase = 0

    if p2.y - p1.y > 0:
        y_increase = 1
    elif p2.y - p1.y < 0:
        y_increase = -1
    else:
        y_increase = 0

    if x_increase == 0 and y_increase == 0:
        raise Exception('Same points')

    x = p1.x
    y = p1.y

    for i in range(steps + 1):
        draw_pixel(Point2D(x, y))
        x += x_increase
        if p < 0:
            p = p + (2 * dy)
        else:
            y += y_increase
            p = p + (2 * dy) - (2 * dx)


def main():
    bresenham(Point2D(30, 150), Point2D(200, 180))
    bresenham(Point2D(300, 180), Point2D(30, 200))
    bresenham(Point2D(150, 150), Point2D(150, 250))

    input('Press <enter> to close')


if __name__ == "__main__":
    main()
