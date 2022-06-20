from flask import render_template
from app import create_app
from dotenv import dotenv_values

env = dotenv_values('.env')
app = create_app(env["FLASK_ENV"] or 'default')

from app.routes import ui_routes, product_routes, auth_routes 

app.register_blueprint(ui_routes.ui, url_prefix = "/")
app.register_blueprint(product_routes.api_products, url_prefix = "/api/products")
app.register_blueprint(auth_routes.api_auth, url_prefix = "/api/auth")

@app.errorhandler(404) 
def invalid_route(e): 
    return render_template('404.html')
