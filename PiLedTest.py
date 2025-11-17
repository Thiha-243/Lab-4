import time
from hal import hal_led as led
from hal import hal_input_switch as sw

def main():
    led.init()
    sw.init()

    while True:
        switch_value = sw.read_slide_switch()

        if switch_value == 0:
            led.set_output(0, 1)
            time.sleep(0.1)
            led.set_output(0, 0)
            time.sleep(0.1)

        else:
            start = time.time()

            while time.time() - start < 5:
                led.set_output(0, 1)
                time.sleep(0.05)
                led.set_output(0, 0)
                time.sleep(0.05)

            led.set_output(0, 0)
            time.sleep(0.1)

if __name__ == "__main__":
    main()
