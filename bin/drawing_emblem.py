from ast import main
from audioop import add
from turtle import *
import math
from time import sleep

WIDTH = 1300
HEIGHT = 1300
UNIT = 100
UNIT=UNIT*1.3
setup(WIDTH,HEIGHT)
title("My Emblem")

def draw_circle(radius, deg):
    circle(radius, deg)

def main_circle(radius):
    """
    Draw the center circle
    """
    penup()
    home()
    setposition(radius, 0)
    setheading(90)
    fillcolor("purple")
    begin_fill()
    pendown()
    draw_circle(radius, 360)
    end_fill()

def overlay_circle(main_radius, offset):
    penup()
    setposition(0, main_radius)
    setheading(180)
    Radius = main_radius - offset
    fillcolor("gray")
    begin_fill()
    pendown()
    draw_circle(Radius, 360)
    end_fill()

def draw_crest_body(width, height, center_radius, arc, flanges):
    def outer_polygon_indeces(y1, y2, side):
        m = ((0-(-height))/((0.5 * width) - 0))
        if side == 'right':
            m = -m
        b = -height
        x1 = (y1 - b) / m
        x2 = (y2 - b) / m
        return x1, x2

    def inner_polygon_indeces(y1, y2, side):
        m = ((0-(-height))/((0.5 * width) - 0))
        if side == 'right':
            m = -m
        b = -(height * 3 / 4)
        x1 = (y1 - b) / m
        x2 = (y2 - b) / m
        return x1, x2

    def calculate_angle_direction(y1, y2, side, inner_outer):
        if inner_outer == 'outer':
            x1, x2 = outer_polygon_indeces(y1, y2, side)
        elif inner_outer == 'inner':
            x1, x2 = inner_polygon_indeces(y1, y2, side)
        elif inner_outer == 'between':
            x1, _ = outer_polygon_indeces(y1, y2, side)
            _, x2 = inner_polygon_indeces(y1, y2, side)
        Y = y2 - y1
        X = x2 - x1
        diff_angle = math.degrees(math.atan(( Y / X )))
        angle = abs(diff_angle)
        distance = math.sqrt(Y**2 + X**2)
        return angle, distance

    def perform_cutin(y1, y2, left_right):
        y_prime = (y2 - y1) / 2 + y1
        if left_right == 'right':
            deg_out, length_out = calculate_angle_direction(y1, y_prime, left_right, 'outer')
            if left_right == 'right':
                setheading(180 + deg_out)
            elif left_right == 'left':
                setheading(180 - deg_out)
            fd(length_out)

        # Step 2
        _, length_between = calculate_angle_direction(y_prime, y_prime, left_right, 'between')
        if left_right == 'right':
            setheading(180)
        elif left_right == 'left':
            setheading(0)
        fd(length_between)

        # Step 3
        deg_in, length_in = calculate_angle_direction(y_prime, y2, left_right, 'inner')
        if left_right == 'right':
            setheading(180 + deg_in)
        elif left_right == 'left':
            setheading(180 - deg_in)
        fd(length_in)

        # Step 4
        _, length_between = calculate_angle_direction(y2, y2, left_right, 'between')
        if left_right == 'right':
            setheading(0)
        elif left_right == 'left':
            setheading(180)
        fd(length_between)

        # Step 5
        if left_right == 'left':
            deg_out, length_out = calculate_angle_direction(y1, y_prime, left_right, 'outer')
            if left_right == 'right':
                setheading(180 + deg_out)
            elif left_right == 'left':
                setheading(180 - deg_out)
            fd(length_out)

    penup()
    fillcolor("gold")
    begin_fill()
    setposition(-width/2, 0)
    setheading(0)
    pendown()
    fd((width/2) - center_radius)
    rt(90)
    draw_circle(center_radius, 180)
    setheading(0)
    fd((width/2) - pos()[0])

    height_unit = height/flanges
    for _ in range(flanges-2):
        '''Right side'''
        _, y = pos()
        target_y = y-height_unit
        perform_cutin(y1=y, y2=target_y, left_right='right')
    _, y = pos()
    deg, length = calculate_angle_direction(y1=y, y2=-height, side='right', inner_outer='outer')
    setheading(180 + deg)
    fd(length)
    deg, length = calculate_angle_direction(y1=y, y2=-height, side='left', inner_outer='outer')
    setheading(180 - deg)
    fd(length)

    for _ in range(flanges-2):
        '''Left side'''
        x, y = pos()
        target_y = y+height_unit
        perform_cutin(y1=y, y2=target_y, left_right='left')
    end_fill()

# def draw_crest_body_v3(width, height, center_radius, arc, flanges):
#     print(width, height)
#     # def outer_polygon_indeces(y1, y2, side):
#     #     m = ((0-(-height))/((0.5 * width) - 0))
#     #     if side == 'right':
#     #         m = -m
#     #     b = -height
#     #     x1 = (y1 - b) / m
#     #     x2 = (y2 - b) / m
#     #     return x1, x2

#     def outer_polygon_indeces_v2(y1, y2, side):
#         A = 387.5 / 810_000
#         B = 1 / 8
#         C = -500
#         def calc_x(y):
#             x = (math.sqrt(-4*A*C + 4*A*y + B**2) + B) / (2*A)
#             return x
#         x1 = calc_x(y1)
#         x2 = calc_x(y2)
#         return x1, x2
#     #     # m = ((0-(-height))/((0.5 * width) - 0))
#     #     # if side == 'right':
#     #     #     m = -m
#     #     # b = -height
#     #     # x1 = (y1 - b) / m
#     #     # x2 = (y2 - b) / m
#     #     return x1, x2
#     y1 = 0
#     y2 = -height
#     print((y1, y2))
#     sleep(2)
#     print((y1, y2), outer_polygon_indeces_v2(y1,y2,'right'))

#     # def inner_polygon_indeces(y1, y2, side):
#     #     m = ((0-(-height))/((0.5 * width) - 0))
#     #     if side == 'right':
#     #         m = -m
#     #     b = -(height * 3 / 4)
#     #     x1 = (y1 - b) / m
#     #     x2 = (y2 - b) / m
#     #     return x1, x2

#     # def calculate_angle_direction(y1, y2, side, inner_outer):
#     #     if inner_outer == 'outer':
#     #         x1, x2 = outer_polygon_indeces(y1, y2, side)
#     #     elif inner_outer == 'inner':
#     #         x1, x2 = inner_polygon_indeces(y1, y2, side)
#     #     elif inner_outer == 'between':
#     #         x1, _ = outer_polygon_indeces(y1, y2, side)
#     #         _, x2 = inner_polygon_indeces(y1, y2, side)
#     #     Y = y2 - y1
#     #     X = x2 - x1
#     #     diff_angle = math.degrees(math.atan(( Y / X )))
#     #     angle = abs(diff_angle)
#     #     distance = math.sqrt(Y**2 + X**2)
#     #     return angle, distance

#     # def perform_cutin(y1, y2, left_right):
#     #     y_prime = (y2 - y1) / 2 + y1
#     #     if left_right == 'right':
#     #         deg_out, length_out = calculate_angle_direction(y1, y_prime, left_right, 'outer')
#     #         if left_right == 'right':
#     #             setheading(180 + deg_out)
#     #         elif left_right == 'left':
#     #             setheading(180 - deg_out)
#     #         fd(length_out)

#     #     # Step 2
#     #     _, length_between = calculate_angle_direction(y_prime, y_prime, left_right, 'between')
#     #     if left_right == 'right':
#     #         setheading(180)
#     #     elif left_right == 'left':
#     #         setheading(0)
#     #     fd(length_between)

#     #     # Step 3
#     #     deg_in, length_in = calculate_angle_direction(y_prime, y2, left_right, 'inner')
#     #     if left_right == 'right':
#     #         setheading(180 + deg_in)
#     #     elif left_right == 'left':
#     #         setheading(180 - deg_in)
#     #     fd(length_in)

#     #     # Step 4
#     #     _, length_between = calculate_angle_direction(y2, y2, left_right, 'between')
#     #     if left_right == 'right':
#     #         setheading(0)
#     #     elif left_right == 'left':
#     #         setheading(180)
#     #     fd(length_between)

#     #     # Step 5
#     #     if left_right == 'left':
#     #         deg_out, length_out = calculate_angle_direction(y1, y_prime, left_right, 'outer')
#     #         if left_right == 'right':
#     #             setheading(180 + deg_out)
#     #         elif left_right == 'left':
#     #             setheading(180 - deg_out)
#     #         fd(length_out)

#     # penup()
#     # fillcolor("gold")
#     # begin_fill()
#     # setposition(-width/2, 0)
#     # setheading(0)
#     # pendown()
#     # fd((width/2) - center_radius)
#     # rt(90)
#     # draw_circle(center_radius, 180)
#     # setheading(0)
#     # fd((width/2) - pos()[0])

#     # height_unit = height/flanges
#     # for _ in range(flanges-2):
#     #     '''Right side'''
#     #     _, y = pos()
#     #     target_y = y-height_unit
#     #     perform_cutin(y1=y, y2=target_y, left_right='right')
#     # _, y = pos()
#     # deg, length = calculate_angle_direction(y1=y, y2=-height, side='right', inner_outer='outer')
#     # setheading(180 + deg)
#     # fd(length)
#     # deg, length = calculate_angle_direction(y1=y, y2=-height, side='left', inner_outer='outer')
#     # setheading(180 - deg)
#     # fd(length)

#     # for _ in range(flanges-2):
#     #     '''Left side'''
#     #     x, y = pos()
#     #     target_y = y+height_unit
#     #     perform_cutin(y1=y, y2=target_y, left_right='left')
#     # end_fill()

def draw_crest_sperit_base(width, height, center_radius, semicircle_width, circle_offset):
    def calcualte_circle():
        A = center_radius + semicircle_width
        B = circle_offset
        deg = math.degrees(math.atan(A / B)) * 2
        x, _ = pos()
        r2 = math.sqrt(x**2 + (circle_offset)**2)
        return r2, deg

    penup()
    fillcolor("green")
    begin_fill()
    setposition(center_radius, 0)
    setheading(90)
    pendown()
    draw_circle(center_radius, 180)
    rt(90)
    fd(semicircle_width)
    rt(90)
    radius, deg = calcualte_circle()
    tilt_angle = 90 - math.degrees(math.atan(circle_offset / (center_radius + semicircle_width)))
    setheading(tilt_angle)
    draw_circle(-radius, deg)
    setheading(180)
    fd(semicircle_width)
    end_fill()
    return radius

def draw_crest_sperit_crown(crest_top_radius, circle_offset, flange_length):
    def calculate_arc(x):
        y = math.sqrt(crest_top_radius**2 - x**2)
        theta = 90 - math.degrees(math.atan(y/x))
        phi = theta * 2
        tilt_angle = 90 - math.degrees(math.atan(y/x))
        return y, phi, tilt_angle

    def add_flange(up_down, distance):
        if up_down == 'up':
            fd(distance)
            rt(90)
            fd(distance)
            lt(90)
            fd(distance)
            lt(90)
            fd(distance)
            rt(90)
        elif up_down == 'down':
            rt(90)
            fd(distance)
            lt(90)
            fd(distance)
            lt(90)
            fd(distance)
            rt(90)
            fd(distance)

    penup()
    fillcolor("green")
    begin_fill()
    x = flange_length / 2
    y, phi, tilt_angle = calculate_arc(x=x)
    setposition(-x, (y - circle_offset))
    setheading(tilt_angle)
    pendown()
    draw_circle(-crest_top_radius, phi)

    # Up
    setheading(90)
    add_flange('up', flange_length)
    add_flange('up', flange_length)

    # Across
    fd(flange_length)
    lt(90)
    fd(flange_length)
    lt(90)
    fd(flange_length)

    # Down
    add_flange('down', flange_length)
    add_flange('down', flange_length)

    end_fill()

crest_top_radius = 300
main_circle(radius=UNIT*1.8)
overlay_circle(main_radius=UNIT*1.8, offset=UNIT/4)
crest_top_radius = draw_crest_sperit_base(width=UNIT*9, height=UNIT*5, center_radius=UNIT*2, semicircle_width=UNIT, circle_offset=UNIT*1.2)
draw_crest_sperit_crown(crest_top_radius=crest_top_radius, circle_offset=UNIT*1.2, flange_length=UNIT/2)
draw_crest_body(width=UNIT*9, height=UNIT*5, center_radius=UNIT*2, arc='squared', flanges=6)
# draw_crest_body_v3(width=UNIT*9, height=UNIT*5, center_radius=UNIT*2, arc='squared', flanges=6)

hideturtle()
mainloop()
