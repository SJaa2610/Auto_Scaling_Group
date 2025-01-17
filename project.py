from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    # HTML con estilo para el mensaje de bienvenida
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; background-color: #f9f9f9; }
            .welcome { color: #333; font-size: 20px; margin: 20px auto; padding: 10px; border: 1px solid #ccc; border-radius: 10px; display: inline-block; background-color: #ffffff; }
            a { color: #007BFF; text-decoration: none; font-weight: bold; }
            a:hover { text-decoration: underline; }
        </style>
    </head>
    <body>
        <div class="welcome">
            Welcome to My Business Card API! <br>
            Go to <a href="/api/card" target="_blank">/api/card</a> to view the card.
        </div>
    </body>
    </html>
    """

@app.route('/api/card', methods=['GET'])
def get_card():
    # Datos de la tarjeta en formato JSON
    card = {
        "name": "Sarahi",
        "profession": "Student",
        "email": "sarahi@gmail.com",
        "phone": "+123456789",
        "website": "https://sarahi.dev"
    }
    return jsonify(card)

@app.route('/favicon.ico')
def favicon():
    # Evita errores de favicon en navegadores
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
