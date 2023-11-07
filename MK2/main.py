from Robot import Robot


if __name__ == "__main__":
    robot = Robot()
    movement = Movement()
    servo_state = None
    try:
        with Xbox360Controller(0, axis_threshold=0.2) as controller:
            # controller.axis_l.when_moved = on_axis_moved
            # controller.axis_r.when_moved = on_axis_moved
            left = controller.axis_l
            while True:
                if controller.button_a.is_pressed and servo_state != "up":
                    robot.move_servo_up()
                    servo_state = "up"
                elif controller.button_y.is_pressed and servo_state != "down":
                    robot.move_servo_down()
                    servo_state = "down"
                pwmL, pwmR = axis_move(left)
                robot.start_motor("left", pwmL)
                robot.start_motor("right", pwmR)
                time.sleep(0.01)

    except KeyboardInterrupt:
        pass
