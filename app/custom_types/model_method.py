
from enum import Enum


class ModelMethod(str, Enum):
    binary = 'binary'
    proba = 'proba'
    scores = 'scores'
