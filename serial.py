"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    
    def __init__(self, start):
        "Create a serial generator starting from initial value of 'start'"
        self.start = start
        self.original = start

    def generate(self):
        "Returns original starting number first time function is called, and then adds one each time function is called and returns the new number"
        self.start +=1 
        if self.start == self.original + 1:
            print(self.original)
            return self.original
        else: 
            print(self.start-1)
            return self.start-1

    def reset(self):
        "Resets self.start to the original starting number."
        self.start = self.original


serial = SerialGenerator(start=15)
serial.generate()
serial.generate()
serial.generate()
serial.reset()
serial.generate()