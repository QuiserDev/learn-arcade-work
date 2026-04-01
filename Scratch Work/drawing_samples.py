import arcade

arcade.open_window(600, 600, "Drawing Samples")

# 背景，蓝天
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

arcade.start_render()

# 草地
arcade.draw_lrbt_rectangle_filled(0, 599, 0, 300, arcade.csscolor.GREEN)

# 树干和树顶
arcade.draw_rect_filled(arcade.XYWH(100, 320, 20, 60), arcade.csscolor.SIENNA)
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)

# 空心树干和椭圆树顶
arcade.draw_rect_outline(
    arcade.XYWH(200, 320, 20, 60), arcade.csscolor.SIENNA, border_width=5
)
arcade.draw_ellipse_filled(200, 370, 60, 80, arcade.csscolor.DARK_GREEN)

# 画弧形树顶
arcade.draw_rect_filled(arcade.XYWH(300, 320, 20, 60), arcade.csscolor.SIENNA)
arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_GREEN, -10, 190)

# 三角形树顶，需要三个点坐标
arcade.draw_rect_filled(arcade.XYWH(400, 320, 20, 60), arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)

# 多边形
arcade.draw_rect_filled(arcade.XYWH(500, 320, 20, 60), arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(
    ((500, 400), (480, 360), (470, 320), (530, 320), (520, 360)),
    arcade.csscolor.DARK_GREEN,
)

# sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)
arcade.draw_line(500 - 60, 550, 500 + 60, 550, arcade.color.YELLOW, line_width=3)
arcade.draw_line(500, 550 - 60, 500, 550 + 60, arcade.color.YELLOW, line_width=3)
arcade.draw_line(
    500 - 40, 550 + 40, 500 + 40, 550 - 40, arcade.color.YELLOW, line_width=3
)
arcade.draw_line(
    500 - 40, 550 - 40, 500 + 40, 550 + 40, arcade.color.YELLOW, line_width=3
)

arcade.draw_text("Hello Arcade, Plant some trees!", 100, 230, arcade.color.BLACK, 24)


arcade.finish_render()

arcade.run()
