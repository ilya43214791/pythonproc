import time
import logging


class TimerContext:
    def __enter__(self):
        self.time = time.time()

    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.time
        logging.info(f"Час виконання: {self.time} секунд", elapsed_time)


# Set up logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

with TimerContext():
    time.sleep(2)
