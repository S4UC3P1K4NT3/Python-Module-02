def input_temperature(temp_str: str) -> int:
    result = int(temp_str)
    return result


def test_temperature(strtotest: str) -> None:
    try:
        print(f"Temperature is now {input_temperature(strtotest)}°C\n")
    except ValueError:
        print("Caught input_temperature error: invalid"
              f" literal for int() with base 10: '{strtotest}'\n")


if __name__ == "__main__":
    print("=== Garden Temperature ===\n")
    print("Input data is '25'")
    test_temperature("25")
    print("Input data is 'abc'")
    test_temperature("abc")
    print("All tests completed - program didn't crash!")
