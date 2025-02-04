import random

class SimpleStockAgent:
    def __init__(self, initial_cash, stock_prices):
        self.cash = initial_cash
        self.stock_prices = stock_prices  
        self.shares = 0
        self.current_day = 0

    def buy(self):
        if self.cash >= self.stock_prices[self.current_day]:
            self.shares = self.cash // self.stock_prices[self.current_day]
            self.cash -= self.shares * self.stock_prices[self.current_day]
            print(f"Day {self.current_day}: Bought {self.shares} shares at {self.stock_prices[self.current_day]}")

    def sell(self):
        if self.shares > 0:
            self.cash += self.shares * self.stock_prices[self.current_day]
            print(f"Day {self.current_day}: Sold {self.shares} shares at {self.stock_prices[self.current_day]}")
            self.shares = 0

    def hold(self):
        print(f"Day {self.current_day}: Holding")

    def step(self):
        if self.current_day < len(self.stock_prices) - 1:
            self.current_day += 1
            if self.shares == 0 and self.cash >= self.stock_prices[self.current_day]:
                self.buy()
            elif self.shares > 0 and self.stock_prices[self.current_day] > self.stock_prices[self.current_day - 1]:
                self.sell()
            else:
                self.hold()

    def run(self):
        while self.current_day < len(self.stock_prices) - 1:
            self.step()
        total_value = self.cash + (self.shares * self.stock_prices[-1])
        print(f"Final portfolio value: {total_value}")

random.seed(42)
stock_prices = [random.randint(90, 110) for _ in range(10)]
tag = SimpleStockAgent(initial_cash=1000, stock_prices=stock_prices)
tag.run()
