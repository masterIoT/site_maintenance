from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def maintenance():
    return send_from_directory('.', 'maintenance.html')  # Renvoie le fichier HTML

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)  # Écoute sur toutes les interfaces sur le port 5002
