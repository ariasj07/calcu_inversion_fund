import pandas as pd

class InterestCalculator:
    def __init__(self, initial_amount, annual_interest, years):
        self.initial_amount = initial_amount
        self.annual_interest = annual_interest
        self.years = years
    
    def calculate(self):
        initial = self.initial_amount
        gained_list = []
        years_list = []
        final_list = []
        
        for x in range(1, self.years + 1):
            gained = (initial * (self.annual_interest / 100))
            gained_list.append(round(float(gained), 2))
            years_list.append(x)
            final_list.append(round(float(initial + gained), 2))
            initial += gained
        
        data = pd.DataFrame({"Años": years_list, "Monto ganado": gained_list, "Monto año a año": final_list})


calculator = InterestCalculator(500000, 6, 5)
print(calculator.calculate())