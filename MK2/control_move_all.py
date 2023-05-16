import signal
import time
from xbox360controller import Xbox360Controller
from move_all import Movement
from Servomotor import ServoMotor


pwm = 100
RL = [0, 0]


def axis_move(axis):
    # print('Axis {0} moved to {1} {2}'.format(axis.name, axis.x, axis.y))

    pwmL = -axis.y * pwm/2 + axis.x * pwm/2
    pwmR = -axis.y * pwm/2 - axis.x * pwm/2

    return pwmL, pwmR


if __name__ == "__main__":
    movement = Movement()
    movement.setup()
    servo = ServoMotor()
    servo_state = None
    try:
        with Xbox360Controller(0, axis_threshold=0.2) as controller:
            # controller.axis_l.when_moved = on_axis_moved
            # controller.axis_r.when_moved = on_axis_moved
            left = controller.axis_l
            while True:
                if controller.button_a.is_pressed and servo_state != 'up':
                    servo.moveUp()
                    servo_state = 'up'
                elif controller.button_y.is_pressed and servo_state != 'down':
                    servo.moveDown()
                    servo_state = 'down'
                pwmL, pwmR = axis_move(left)
                movement.move_all(pwmL, pwmR)
                time.sleep(0.01)

    except KeyboardInterrupt:
        pass
