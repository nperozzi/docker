import re
import serial

PORT = "COM7"
BAUD = 115200

trigger = "Answer quick:"
pattern = re.compile(r'(\d+)\s*\+\s*(\d+)')

def extract_numbers(text: str):
    m = pattern.search(text)
    if not m:
        return None
    return int(m.group(1)), int(m.group(2))

with serial.Serial(PORT, BAUD, timeout=1) as ser:
    # Send initial number before listening
    ser.write(b"51966\n")

    print("Listening on COM7...")

    while True:
        line = ser.readline().decode(errors="ignore").strip()
        if not line:
            continue

        # Only react to the trigger line
        if trigger not in line:
            continue

        nums = extract_numbers(line)
        if not nums:
            continue

        a, b = nums
        result = a + b

        # Send result back over serial
        ser.write(f"{result}\n".encode())

        # Print whatever comes back after sending
        response = ser.readline().decode(errors="ignore").strip()
        if response:
            print(response)
