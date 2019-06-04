import datetime
import time
from typing import Callable


class TimerPrints:

    @staticmethod
    def highlight(msg) -> None:
        print("** " + msg)

    @staticmethod
    def mute(msg) -> None:
        pass


class Timer(TimerPrints):

    @staticmethod
    def _get_current_time() -> float:
        return time.clock()

    def __init__(self, title: str = '', f_print: Callable[[str], None] = TimerPrints.highlight):
        self._print = f_print
        self.title = title

    def __enter__(self) -> object:
        self.start = self._get_current_time()
        self._print(f'{self.title} started at {time.strftime("%H:%M:%S", time.localtime())}')
        return self

    def __exit__(self, *args) -> None:
        self.end = self._get_current_time()
        self.interval = self.end - self.start
        self._print(f'{self.title} took {str(datetime.timedelta(seconds=int(self.interval)))}')
