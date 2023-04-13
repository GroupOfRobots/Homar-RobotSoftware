import signal
from xbox360controller import Xbox360Controller
from move_all import Movement


pwm = 50
RL = []


def on_axis_moved(axis):
    print('Axis {0} moved to {1} {2}'.format(axis.name, axis.x, axis.y))

    pwmL = axis.x * pwm/2 + axis.y * pwm/2
    pwmR = axis.x * pwm/2 - axis.y * pwm/2
    RL[0] = pwmL
    RL[1] = pwmR


if __name__ == "__main__":
    movement = Movement()
    movement.setup()

    try:
        with Xbox360Controller(0, axis_threshold=0.2) as controller:
            controller.axis_l.when_moved = on_axis_moved
            # controller.axis_r.when_moved = on_axis_moved

            while True:
                movement.move_all(RL[0], RL[1])

    except KeyboardInterrupt:
        pass
