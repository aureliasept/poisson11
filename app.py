from flask import Flask, request, render_template # type: ignore
import math

app = Flask(__name__)

def poisson_probability(lmbda, k):
    return (lmbda**k * math.exp(-lmbda)) / math.factorial(k)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            lmbda = float(request.form['lambda'])
            max_k = int(request.form['max_k'])
            probabilities = [
                {'k': k, 'probability': poisson_probability(lmbda, k), 'percentage': poisson_probability(lmbda, k) * 100}
                for k in range(max_k + 1)
            ]
            return render_template('index.html', lmbda=lmbda, max_k=max_k, probabilities=probabilities)

        except (ValueError, KeyError):
            return render_template('index.html', error="Input tidak valid. Masukkan nilai numerik.")

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
