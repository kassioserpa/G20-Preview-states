from flask import Flask, jsonify, render_template

app = Flask(__name__)

g20_data = [
    {"pais": "Alemanha", "pib": 4.2, "inflacao": 2.1, "divida_pib": 70, "populacao": 83},
    {"pais": "Arábia Saudita", "pib": 1.0, "inflacao": 2.5, "divida_pib": 30, "populacao": 35},
    {"pais": "Argentina", "pib": 0.6, "inflacao": 50.0, "divida_pib": 90, "populacao": 45},
    {"pais": "Austrália", "pib": 1.6, "inflacao": 3.0, "divida_pib": 45, "populacao": 26},
    {"pais": "Brasil", "pib": 2.1, "inflacao": 4.5, "divida_pib": 78, "populacao": 215},
    {"pais": "Canadá", "pib": 2.0, "inflacao": 3.2, "divida_pib": 90, "populacao": 39},
    {"pais": "China", "pib": 18.5, "inflacao": 2.8, "divida_pib": 60, "populacao": 1440},
    {"pais": "Coreia do Sul", "pib": 1.8, "inflacao": 2.0, "divida_pib": 45, "populacao": 52},
    {"pais": "EUA", "pib": 25.0, "inflacao": 3.2, "divida_pib": 105, "populacao": 331},
    {"pais": "França", "pib": 3.0, "inflacao": 2.5, "divida_pib": 98, "populacao": 67},
    {"pais": "Índia", "pib": 3.5, "inflacao": 5.0, "divida_pib": 70, "populacao": 1400},
    {"pais": "Indonésia", "pib": 1.2, "inflacao": 3.5, "divida_pib": 40, "populacao": 275},
    {"pais": "Itália", "pib": 2.1, "inflacao": 2.0, "divida_pib": 150, "populacao": 60},
    {"pais": "Japão", "pib": 5.0, "inflacao": 1.9, "divida_pib": 240, "populacao": 126},
    {"pais": "México", "pib": 1.3, "inflacao": 4.0, "divida_pib": 55, "populacao": 126},
    {"pais": "Reino Unido", "pib": 3.1, "inflacao": 3.0, "divida_pib": 100, "populacao": 67},
    {"pais": "Rússia", "pib": 1.7, "inflacao": 6.0, "divida_pib": 20, "populacao": 145},
    {"pais": "África do Sul", "pib": 0.4, "inflacao": 5.5, "divida_pib": 70, "populacao": 60},
    {"pais": "Turquia", "pib": 0.9, "inflacao": 60.0, "divida_pib": 40, "populacao": 85},
    {"pais": "União Europeia", "pib": 16.0, "inflacao": 3.0, "divida_pib": 90, "populacao": 450}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/g20")
def api_g20():
    return jsonify(g20_data)

if __name__ == "__main__":
    app.run(debug=True)

