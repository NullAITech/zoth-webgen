#!/usr/bin/env python3
"""
Zoth WebGen — Lightweight HTTP Server & API Daemon
Provides zero-egress local UI serving and compilation endpoints on port 8092.
"""

import os
import sys
import json
import argparse
from pathlib import Path
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

ROOT_DIR = Path(__file__).resolve().parent

class WebGenHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT_DIR), **kwargs)

    def do_GET(self):
        if self.path in ('/api/health', '/health'):
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({
                "status": "healthy",
                "service": "zoth-webgen",
                "version": "2.4.0",
                "zero_egress": True
            }).encode('utf-8'))
            return
        elif self.path == '/api/templates':
            from webgen_engine import TEMPLATES
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            summary = {k: {"title": v["title"], "category": v.get("category", "SOVEREIGN"), "description": v["description"]} for k, v in TEMPLATES.items()}
            self.wfile.write(json.dumps(summary).encode('utf-8'))
            return
        return super().do_GET()

    def log_message(self, format, *args):
        # Quiet logging
        pass

def run_server(host: str = "127.0.0.1", port: int = 8092) -> None:
    server = ThreadingHTTPServer((host, port), WebGenHandler)
    print(f"⚡ Zoth WebGen Server listening on http://{host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        server.server_close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Zoth WebGen HTTP Server")
    parser.add_argument("--host", default="127.0.0.1", help="Host interface")
    parser.add_argument("--port", type=int, default=8092, help="Port to listen on (default: 8092)")
    args = parser.parse_args()
    run_server(args.host, args.port)
