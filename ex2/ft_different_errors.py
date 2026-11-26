def input_temperature(temp_str: str) -> int:
    result = int(temp_str)
    if result > 40:
        raise Exception(f" {temp_str}°C is too hot for plants (max 40°C)")
    if result < 0:
        raise Exception(f"{temp_str}°C is too cold for plants (min 0°C)")
    return result


def test_temperature(strtotest: str) -> None:
    try:
        print(f"Temperature is now {input_temperature(strtotest)}°C\n")
    except ValueError as err:
        print("Caught input_temperature error: "
              f"{err}\n")
    except Exception as err:
        print("Caught input_temperature error: "
              f"{err}\n")


def garden_operations(operation_number: int) -> None:
    if operation_number == 0:
        operation_number = int("abc")
    elif operation_number == 1:
        operation_number = 1 / 0
    elif operation_number == 2:
        operation_number = open("/non/existent/file", "r")
    elif operation_number == 3:
        operation_number = "abc" + 67
    else:
        print("Operation completed successfully")


def test_error_types(operation: int) -> None:
    try:
        garden_operations(operation)
    except ValueError as err:
        print(f"Caught ValueError: {err}")
    except ZeroDivisionError as err:
        print(f"Caught ZeroDivisionError: {err}")
    except FileNotFoundError as err:
        print(f"Caught FileNotFoundError: {err}")
    except TypeError as err:
        print(f"Caught TypeError: {err}")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    print("Testing operation 0...")
    test_error_types(0)
    print("Testing operation 1...")
    test_error_types(1)
    print("Testing operation 2...")
    test_error_types(2)
    print("Testing operation 3...")
    test_error_types(3)
    print("Testing operation 4...")
    test_error_types(4)
    print("\nAll error types tested successfully!")
