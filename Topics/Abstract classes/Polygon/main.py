from abc import ABC, abstractmethod


class EquilateralPolygon(ABC):
    def __init__(self, side):
        self.side = side

    @abstractmethod
    def get_area(self):
        ...


# create Square