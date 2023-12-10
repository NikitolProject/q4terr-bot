from abc import ABC
from typing import Final
import os


class Env(ABC):
    TOKEN: Final = os.environ.get('TOKEN', 'define me!')
