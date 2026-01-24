def parse_and_calculate(data, operator):
    """
    Attempts to convert a list of stringified numbers into integers,
    then applies the specified arithmetic operator sequentially.

    Parameters:
    - data (list of str): String representations of numbers.
    - operator (str): Arithmetic operator ('+', '-', '//', '%').

    Returns:
    - int: The result of the arithmetic operation if successful.

    Raises:
    - NumberConversionError: If any string in data cannot be converted to an integer.
    - OperatorNotSupportedError: If the operator is not one of '+', '-', '//', '%'.
    """
    try:
        assert len(data) >= 2
        match operator:
            case "+":
                res = 0
                for i in data:
                    res += int(i)
                return res
            case "-":
                res = int(data[0])
                for i in data[1:]:
                    res -= int(i)
                return res
            case "//":
                res = int(data[0])
                for i in data[1:]:
                    res = res // int(i)
                return res
            case "%":
                res = int(data[0])
                for i in data[1:]:
                    res = res % int(i)
                return res
            case _:
                raise OperatorNotSupportedError("Operator not supported. Valid operators are '+', '-', '//', '%'.")
    except ZeroDivisionError:
        print("Cannot perform integer division or modulo by zero.")
        return None
    except ValueError:
        raise NumberConversionError("Failed to parse one or more strings into integers.")
    except AssertionError:
        raise AssertionError("There must be at least 2 operands")
        
class NumberConversionError(Exception):
    pass

class OperatorNotSupportedError(Exception):
    pass