from application.auth import routes as auth_routes
from application.dashboard import routes as dashboard_routes
from application.api import routes as api_routes

auth_bp = auth_routes.auth_bp
dashboard_bp = dashboard_routes.dashboard_bp
api_bp = api_routes.api_bp
