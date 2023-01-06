import sys

import time
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


# https://www.programiz.com/python-programming/examples/factorial
def calculate_factorial(num: int, delay: int) -> int:
    logging.info(f"Input Value: {num}")
    factorial = 1
    if num < 0:
        raise ValueError("Sorry, cannot calculate factorial for negative numbers")
    elif num == 0:
        return 1
    else:
        for i in range(1, num + 1):
            time.sleep(delay)  # Change to test delays
            factorial = factorial * i
        logging.info(f"The factorial of {num} is {factorial}")
        return factorial
