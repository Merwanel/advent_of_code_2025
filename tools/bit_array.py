class BitArray:
    def __init__(self, size=0, value=0):
        self.size = size
        self.value = value

    def set(self, i: int, val: bool) -> None:
        if val:
            self.value |= (1 << i)
        else:
            self.value &= ~(1 << i)

    def toggle(self, i: int) -> None:
        self.value ^= (1 << i)

    def get(self, i: int) -> bool:
        return bool((self.value >> i) & 1)

    def __eq__(self, other):
        if isinstance(other, BitArray):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)

    def copy(self):
        return BitArray(self.size, self.value)

    def __repr__(self):
        repr = bin(self.value)[2:][::-1]
        repr = "0" * (self.size - len(repr)) + repr
        return repr
