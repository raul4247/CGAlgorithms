from CGComponents import *

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300


def draw_pixel(p):
    if p.x < 0 or p.x > SCREEN_WIDTH or p.y < 0 or p.y > SCREEN_HEIGHT:
        raise Exception('Point out of screen bounds')

    print('x:{0}    y:{1}'.format(p.x, p.y))


def draw_point_in_each_octant(point, origin):
    draw_pixel(Point2D(point.x + origin.x, point.y + origin.y))
    draw_pixel(Point2D(point.x - origin.x, point.y + origin.y))
    draw_pixel(Point2D(point.x + origin.x, point.y - origin.y))
    draw_pixel(Point2D(point.x - origin.x, point.y - origin.y))
    draw_pixel(Point2D(point.x + origin.y, point.y + origin.x))
    draw_pixel(Point2D(point.x - origin.y, point.y + origin.x))
    draw_pixel(Point2D(point.x + origin.y, point.y - origin.x))
    draw_pixel(Point2D(point.x - origin.y, point.y - origin.x))


def bresenham_circle(center, radius):
    x = 0
    y = radius
    d = 3 - (2 * radius)

    draw_point_in_each_octant(center, Point2D(x, y))

    while y >= x:
        x += 1

        if d > 0:
            y -= 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6

        draw_point_in_each_octant(center, Point2D(x, y))


def main():
    bresenham_circle(Point2D(150, 150), 100)
    bresenham_circle(Point2D(100, 100), 50)
    bresenham_circle(Point2D(100, 200), 50)
    bresenham_circle(Point2D(200, 100), 50)
    bresenham_circle(Point2D(200, 200), 50)
    input('Press <enter> to close')


if __name__ == "__main__":
    main()
