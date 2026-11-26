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


if __name__ == "__main__":
    print("=== Garden Temperature Check ===\n")
    print("Input data is '25'")
    test_temperature("25")
    print("Input data is 'abc'")
    test_temperature("abc")
    print("Input data is '100'")
    test_temperature("100")
    print("Input data is '-50'")
    test_temperature("-50")
    print("All tests completed - program didn't crash!")
