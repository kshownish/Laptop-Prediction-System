from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__, template_folder='templates')

# Load the DataFrame and model
df = pickle.load(open('df.pkl', 'rb'))
pipe = pickle.load(open('pipe.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    # Get unique values for dropdowns
    companies = sorted(df['Company'].unique())
    cpus = sorted(df['Cpu brand'].unique())
    rams = sorted(df['Ram'].unique())

    price = None
    if request.method == 'POST':
        # Get form data
        company = request.form['company']
        cpu = request.form['cpu']
        ram = int(request.form['ram'])

        # Create input DataFrame
        input_data = pd.DataFrame([[company, ram, cpu]], 
                                 columns=['Company', 'Ram', 'Cpu brand'])

        # Predict price
        price = pipe.predict(input_data)[0]
        price = round(price, 2)

    return render_template('index.html', 
                         companies=companies, 
                         cpus=cpus, 
                         rams=rams, 
                         price=price)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)