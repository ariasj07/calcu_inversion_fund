from flask import Flask, render_template, request, send_file

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)


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
        a = 1
        years_total = []
        for x in range(1, self.years + 1):
            gained = (initial * (self.annual_interest / 100))
            gained_list.append(round(float(gained), 2))
            years_list.append(x)
            final_list.append(round(float(initial + gained), 2))
            years_total.append(a)
            a += 1
            initial += gained
        
        data = pd.DataFrame({"Años": years_list, "Monto ganado": gained_list, "Monto año a año": final_list})
        data.to_excel("data.xlsx")
        return initial, gained_list, final_list, years_total


@app.route('/data', methods=["GET", "POST"])
def get_data():
    plazo = request.form.get("plazo")
    plazo = int(plazo)
    monto = request.form.get("monto")
    monto = monto.replace(",", "")
    monto = float(monto)
    interes = request.form.get("interes")
    interes = interes.replace(",", ".")
    interes = float(interes)
    calculator = InterestCalculator(monto, interes, plazo)
    result, gainer_per_year, final_amount, years_amount = calculator.calculate()
    result = f"{round(result,2):,}" 
    return render_template('index.html', result=result, gainer_per_year=[f"{gain:,}" for gain in gainer_per_year], final_amount=[f"{final:,}" for final in final_amount], years_amount=years_amount)


@app.route("/download_file", methods=["GET"])
def download_file():
    return send_file("./data.xlsx", as_attachment=True)
