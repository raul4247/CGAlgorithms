from CGComponents import *

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300


def draw_pixel(p):
    if p.x < 0 or p.x > SCREEN_WIDTH or p.y < 0 or p.y > SCREEN_HEIGHT:
        raise Exception('Point out of screen bounds')

    print('x:{0}    y:{1}'.format(p.x, p.y))


def dda(p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    if steps == 0:
        raise Exception('Same points')

    x_increase = dx / steps
    y_increase = dy / steps

    x = p1.x
    y = p1.y

    for i in range(steps + 1):
        draw_pixel(Point2D(round(x), round(y)))
        x += x_increase
        y += y_increase


def main():
    dda(Point2D(30, 150), Point2D(200, 180))
    dda(Point2D(300, 180), Point2D(30, 200))
    dda(Point2D(150, 150), Point2D(150, 250))

    input('Press <enter> to close')


if __name__ == "__main__":
    main()
