from application.login import routes as login_routes
from application.dashboard import routes as dashboard_routes
from application.api import routes as api_routes

login_bp = login_routes.login_bp
dashboard_bp = dashboard_routes.dashboard_bp
api_bp = api_routes.api_bp
