import serial
import time

# Replace 'COM3' with your actual port (e.g., '/dev/ttyACM0', '/dev/ttyUSB0', or 'COM5'),
# and match the baud rate with what your Arduino sketch uses (e.g., 9600, 115200).
ARDUINO_PORT = 'COM3'
BAUD_RATE = 115200

# Global variable to hold the serial connection (if you want one persistent connection)
arduino_serial = None

def initialize_connection(port=ARDUINO_PORT, baud=BAUD_RATE):
    """
    Initializes and returns a serial connection to the Arduino.
    This function can be called once at the start of your application.
    """
    global arduino_serial
    try:
        arduino_serial = serial.Serial(port, baud, timeout=1)
        # Give Arduino a little time to reset (2 seconds is often enough)
        time.sleep(2)
        print(f"[INFO] Connected to Arduino on {port} at {baud} baud.")
        return arduino_serial
    except serial.SerialException as e:
        raise RuntimeError(f"Failed to connect to Arduino on port {port}: {e}")


def send_command(command):
    """
    Sends a textual command (bytes) to the Arduino and optionally reads any response.
    Make sure your Arduino sketch is coded to receive these text-based commands 
    and perform the desired actions.
    """
    global arduino_serial
    if not arduino_serial or not arduino_serial.is_open:
        raise RuntimeError("Arduino serial connection is not open. Call initialize_connection() first.")

    # Write the command, followed by a newline for Arduino to parse it easily
    cmd_bytes = f"{command}\n".encode('utf-8')
    arduino_serial.write(cmd_bytes)
    arduino_serial.flush()

    # (Optional) read back a response, if your Arduino code sends one
    # response = arduino_serial.readline().decode('utf-8').strip()
    # print(f"[Arduino] {response}")


def start_treadmill():
    """
    Activates a stepper motor to move a conveyor belt (treadmill).
    Requires the Arduino to interpret "START_TREADMILL" and run the stepper.
    """
    # Example command recognized by the Arduino code
    send_command("START_TREADMILL")


def stop_treadmill():
    """
    Deactivates the stepper motor, halting the treadmill.
    Requires the Arduino to interpret "STOP_TREADMILL" and stop the stepper.
    """
    send_command("STOP_TREADMILL")


def rotate_arm_left():
    """
    Commands the servo motor to rotate counterclockwise (up to 360°).
    The Arduino code must handle how to move the servo CCW to direct trash to the bin.
    """
    send_command("ROTATE_ARM_LEFT")


def rotate_arm_right():
    """
    Commands the servo motor to rotate clockwise (up to 360°).
    The Arduino code must handle how to move the servo CW to direct trash to the bin.
    """
    send_command("ROTATE_ARM_RIGHT")


def close_connection():
    """
    Closes the serial connection to the Arduino.
    You can call this when your application shuts down.
    """
    global arduino_serial
    if arduino_serial and arduino_serial.is_open:
        arduino_serial.close()
        print("[INFO] Arduino serial connection closed.")
        arduino_serial = None
