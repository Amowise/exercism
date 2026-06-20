def is_divisible(num: int, divisor: int) -> bool:
    '''Checks whether a number is divisible by the specified divisor.'''
    return num % divisor == 0


def leap_year(year: int) -> bool:
    ''' Checks wether the given year is a leap year'''
    if is_divisible(year, 4):
        if is_divisible(year, 100):
            if is_divisible(year, 400):
                return True
            return False
        return True
    return False
        
