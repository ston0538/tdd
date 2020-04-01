# class Test:
#     def __init__(self, amount):
#         self.amount = amount


class Dollar:
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier: int):
        return Dollar(self.amount * multiplier)

    def equals(self, other) -> bool:
        return self.amount == other.amount
