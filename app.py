from datetime import datetime

from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    """Úvodní strana s analogovým ciferníkem zobrazujícím čas serveru."""
    now = datetime.now()
    # Server pošle aktuální čas; JS ciferník pak tiká klientem a znovu
    # se synchronizuje přes /time.
    return render_template("index.html", now=now)


@app.route("/time")
def time():
    """aktuální čas serveru ve formátu ISO (pro synchronizaci ciferníku)."""
    return jsonify(iso=datetime.now().isoformat())


if __name__ == "__main__":
    app.run(debug=True)
