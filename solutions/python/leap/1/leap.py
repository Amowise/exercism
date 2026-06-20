def is_divisible(num, divisor):
    return num % divisor == 0


def leap_year(year: int) -> bool:
    if is_divisible(year, 4):
        if is_divisible(year, 100):
            if is_divisible(year, 400):
                return True
            return False
        return True
    return False
        
