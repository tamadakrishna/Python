# Custom Exception Handling

# Without custom exceptions, we might use generic exceptions with string messages.
def check_sensor(temp):
    if temp > 100:
        raise RuntimeError("TOO_HOT")
    if temp < 0:
        raise RuntimeError("TOO_COLD")

try:
    check_sensor(120)
except RuntimeError as e:
    # We are forced to compare string values
    if str(e) == "TOO_HOT":
        print("Turning on the fan...")
    elif str(e) == "TOO_COLD":
        print("Turning on the heater...")





# With custom exceptions, we can create specific exception classes.
class OverheatingError(Exception): pass
class FreezingError(Exception): pass

def check_sensor(temp):
    if temp > 100:
        raise OverheatingError()
    if temp < 0:
        raise FreezingError()

try:
    check_sensor(-5)
except OverheatingError:
    print("Turning on the fan...")
except FreezingError:
    print("Turning on the heater...")