import arcade

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480


class Ball:
    def __init__(self, position_x, position_y, radius, color):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x,
                                  self.position_y,
                                  self.radius,
                                  self.color)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        # Call the parent class's init function
        super().__init__(width, height, title)
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.ASH_GREY)

        # Create our ball
        self.ball = Ball(50, 50, 15, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        self.clear()
        self.ball.draw()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        self.ball.position_x = x
        self.ball.position_y = y

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        print(x, y, button, modifiers)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W:
            self.ball.position_y += 50
        elif symbol == arcade.key.S:
            self.ball.position_y -= 50
        elif symbol == arcade.key.A:
            self.ball.position_x -= 50
        elif symbol == arcade.key.D:
            self.ball.position_x += 50

def main():
    window = MyGame(640, 480, "Drawing Example")
    arcade.run()


main()
