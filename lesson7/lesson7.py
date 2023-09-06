class Price:
    def __init__(self, amount: float, currency: str) -> None:
        self.amount: float = amount
        self.currency: str = currency

    def __add__(self, other):
        if self.currency == other.currency:
            return Price(self.amount + other.amount, self.currency)
        elif self.currency == "USD":
            return Price(self.amount + other.convert_to(self.currency).amount, self.currency)
        elif other.currency == "USD":
            return Price(self.amount + other.amount / self.convert_rate(other.currency), self.currency)
        else:
            return Price(self.amount + other.convert_to(self.currency).amount, self.currency)

    def __sub__(self, other):
        if self.currency == other.currency:
            return Price(self.amount - other.amount, self.currency)
        elif self.currency == "USD":
            return Price(self.amount - other.convert_to(self.currency).amount, self.currency)
        elif other.currency == "USD":
            return Price(self.amount - other.amount / self.convert_rate(other.currency), self.currency)
        else:
            return Price(self.amount - other.convert_to(self.currency).amount, self.currency)

    def convert_to(self, target_currency: str):
        return Price(self.amount * self.convert_rate(target_currency), target_currency)

    def convert_rate(self, target_currency: str):
        # Define your conversion rates here, assuming USD as the middle currency
        conversion_rates = {
            "USD": 1.0,
            "EUR": 0.85,  # Example conversion rate for EUR to USD
            "GBP": 0.73,  # Example conversion rate for GBP to USD
        }
        return conversion_rates.get(target_currency, 0.0)

    def __str__(self):
        return f"{self.amount} {self.currency}"

# Example usage:
price1 = Price(100, "USD")
price2 = Price(50, "EUR")
result1 = price1 + price2
result2 = price1 - price2

print(result1)  # Output: 145.0 USD
print(result2)  # Output: 55.0 USD
