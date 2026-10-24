import logging
import os

from flask import Flask, Response, render_template_string

from abhishek.config import Config
from abhishek.extensions import db
from abhishek.routes import main_bp


def create_app(config_class: type[Config] = Config) -> Flask:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s [%(name)s] %(message)s",
    )

    app = Flask(__name__)

    os.makedirs(app.instance_path, exist_ok=True)

    app.config.from_object(config_class)

    if config_class is Config:
        Config.validate()

    db.init_app(app)

    from abhishek.commands import seed_command

    app.cli.add_command(seed_command)

    app.register_blueprint(main_bp)

    @app.errorhandler(404)
    def page_not_found(error: Exception) -> tuple[str, int]:
        app.logger.warning("Page not found: %s", error)
        return (
            render_template_string(
                "<h1>Page not found</h1>"
                "<p>Sorry, the page you requested does not exist.</p>"
            ),
            404,
        )

    @app.errorhandler(500)
    def internal_server_error(error: Exception) -> tuple[str, int]:
        app.logger.error("Internal server error: %s", error)
        return (
            render_template_string(
                "<h1>Something went wrong</h1>"
                "<p>Sorry, an unexpected error occurred. Please try again later.</p>"
            ),
            500,
        )

    @app.after_request
    def add_security_headers(response: Response) -> Response:
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; "
            "object-src 'none'; "
            "frame-ancestors 'none'; "
            "base-uri 'self'"
        )
        response.headers["Permissions-Policy"] = (
            "camera=(), microphone=(), geolocation=()"
        )

        return response

    return app
