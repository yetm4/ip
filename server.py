from flask import Flask, render_template, redirect
from ip import get_ip
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def ip_display():
    ip_data = get_ip()
    return render_template("index.html", 
                           ip = ip_data['ip_address'], 
                           country = ip_data['country'], 
                           city = ip_data['city'], 
                           currency = ip_data["currency"]['currency_name'], 
                           vpn = ip_data["security"]['is_vpn'],
                           flag = ip_data["flag"]["png"])

if __name__ == "__main__":
    serve(app, host = "0.0.0.0", port=8000)