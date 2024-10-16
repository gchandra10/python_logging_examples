import logging

# Configure the logging
logging.basicConfig(
    filename='try_except_error.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def divide_numbers(a, b):
    try:
        result = a / b
        logging.info(f"Division successful: {a} / {b} = {result}")
        return result
    except ZeroDivisionError as e:
        # Adding exc_info captures full exception trackback
        logging.error("Attempted to divide by zero.", exc_info=True)
        return None
    except Exception as e:
        logging.critical("An unexpected error occurred.", exc_info=True)
        return None

# Example usage
divide_numbers(10, 2)  # Successful division
divide_numbers(10, 0)  # Division by zero error
