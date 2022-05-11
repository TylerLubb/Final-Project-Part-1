def one(n):
    """
    Function to take a positive integer and returns the sum of the integer and all positive integers leading up to it
    from 1
    :param n: positive integer
    :return: sum of n + (n - 1)
    """
    try:
        if type(n) == int:
            if n > 0:
                if n == 1:
                    return n
                else:
                    return n + one(n - 1)
            else:
                raise ValueError('Negative')
        else:
            raise TypeError('Non-int input')
    except ValueError as e:
        print(f'Error = {e}')
    except TypeError as e:
        print(f'Error = {e}')


def two(num, pow):
    """
    Function to take two positive integers and raise one to the power of the other
    :param num: positive integer representing the base number
    :param pow: positive integer representing the exponent
    :return: num to the pow power
    """
    try:
        if type(num) == int and type(pow) == int:
            if pow == 1:
                return num
            elif pow > 1:
                return num * two(num, pow - 1)
            else:
                raise ValueError('Negative')
        else:
            raise TypeError('Non-int input')
    except ValueError as e:
        print(f'Error = {e}')
    except TypeError as e:
        print(f'Error = {e}')


def three(n):
    """
    Function that takes a positive integer and prints all numbers from that number down to 1
    :param n: positive integer
    :return: [n, n-1]
    """
    try:
        letter = ''
        if type(n) == int:
            if n >= 1:
                for i in range(n, 0, -1):
                    letter += (str(n) + ' ')
                    n = n - 1
                return letter
            elif n <= 0:
                return
            else:
                raise ValueError('Negative')
        else:
            raise TypeError('Non-int input')
    except ValueError as e:
        print(f'Error = {e}')
    except TypeError as e:
        print(f'Error = {e}')

