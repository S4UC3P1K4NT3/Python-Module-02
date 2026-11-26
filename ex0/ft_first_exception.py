def input_temperature(temp_str: str):
    try:
        result = int(temp_str)
        return result
    except ValueError:
        print(f"wrong statement given (\"{temp_str}\").")


if __name__ == "__main__":
    input_temperature("15g7")
