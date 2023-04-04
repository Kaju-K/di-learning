# Exercise 1

class Test:
    """This is just a test. You can do nothing with this class"""

    def __init__(self, num) -> None:
        self.num = num

    def __abs__(self):
        if self.num < 0:
            self.num *= -1
        return self

    def __int__(self):
        return self.num
    
print(Test.__doc__)

# Exercise 2

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency.lower()
        self.amount = amount

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise ValueError("You cannot add different currencies")
            return Currency(self.currency, self.amount + other.amount)
        if isinstance(other, int) or isinstance(other, float):
            return Currency(self.currency, self.amount + other)
        raise ValueError("You cannot add these two objects")

        
    def __iadd__(self, other):
        if isinstance(other, Currency):
            self.amount += other.amount
            return self
        elif isinstance(other, int) or isinstance(other, float):
            self.amount += other
            return self
        else:
            raise ValueError("You cannot add this to your account")
    
    def __str__(self):
        if self.amount > 1:
            return f"{self.amount} {self.currency}s"
        return f"{self.amount} {self.currency}"
        
    
    def __repr__(self):
        if self.amount > 1:
            return f"{self.amount} {self.currency}s"
        return f"{self.amount} {self.currency}"
    
    def __int__(self):
        return self.amount
    
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
# '5 dollars'

print(int(c1))
# 5

print(repr(c1))
# '5 dollars'

print(c1 + 5)
# 10

print(c1 + c2)
# 15

print(c1)
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

# print(c1 + c3)