from click import group, pass_context, option, INT
from pkg_resources import iter_entry_points
from click_plugins import with_plugins

from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from wsgiref.simple_server import make_server


app = Flask(__name__)


@with_plugins(iter_entry_points("click_command_tree"))
@group()
@pass_context
def main(context):
    """
    main entry point for salesforce exporter
    """
    pass


def health(env, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    return [b"OK"]


def home(env, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    return [b"<h1> Salesforce Exporter (SFDC) </h1>"]


@main.command("start-server")
@pass_context
@option("--port", default=3000, type=INT)
def server(context, port):
    """
    Starting wsgi server for prometheus exporter.
    """

    app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {"/": home, "/health": health})

    httpd = make_server(host="", port=port, app=app)
    httpd.serve_forever()
