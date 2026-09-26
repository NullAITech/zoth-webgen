import json
import subprocess
import sys
import tempfile
from pathlib import Path
import pytest

from webgen_engine import TEMPLATES, generate_site, generate_master_artifacts
from mcp_server import handle_request

def test_templates_catalog():
    expected = [
        "saas-dashboard",
        "cyberpunk-portfolio",
        "ai-swarm-console",
        "documentation-hub",
        "solana-web3-mint",
        "biomorphic-neuro-shop"
    ]
    for key in expected:
        assert key in TEMPLATES
    for name, data in TEMPLATES.items():
        assert "html" in data
        assert "title" in data
        assert "<!DOCTYPE html>" in data["html"]
        # Sovereign theme token verification
        assert "#08080B" in data["html"] or "#050508" in data["html"]
        assert "#D4AF37" in data["html"] or "#00F0FF" in data["html"]

def test_generate_site():
    with tempfile.TemporaryDirectory() as tmpdir:
        out_file = Path(tmpdir) / "test_site" / "index.html"
        generate_site("saas-dashboard", str(out_file))
        assert out_file.exists()
        content = out_file.read_text(encoding="utf-8")
        assert "Sovereign SaaS Dashboard" in content
        assert "ZERO-EGRESS" in content

def test_generate_master_artifacts():
    with tempfile.TemporaryDirectory() as tmpdir:
        res = generate_master_artifacts("ai-swarm-console", framework="astro", theme="gold", output_dir=tmpdir)
        assert Path(res["master_prompt"]).exists()
        assert Path(res["master_instructions"]).exists()
        assert Path(res["master_blueprint"]).exists()
        assert Path(res["llms_txt"]).exists()

        prompt_txt = Path(res["master_prompt"]).read_text(encoding="utf-8")
        assert "SOVEREIGN AUTONOMOUS MASTER PROMPT" in prompt_txt

        bp_json = json.loads(Path(res["master_blueprint"]).read_text(encoding="utf-8"))
        assert bp_json["project"] == "ai-swarm-console"
        assert bp_json["frameworkTarget"] == "astro"

def test_cli_execution():
    with tempfile.TemporaryDirectory() as tmpdir:
        out_file = Path(tmpdir) / "cli_out.html"
        cmd = [sys.executable, "webgen_engine.py", "--template", "cyberpunk-portfolio", "--out", str(out_file)]
        res = subprocess.run(cmd, cwd=Path(__file__).parent.parent, capture_output=True, text=True)
        assert res.returncode == 0
        assert out_file.exists()
        content = out_file.read_text(encoding="utf-8")
        assert "Cyberpunk Portfolio" in content

def test_mcp_server_initialize():
    req = {"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}
    res = handle_request(req)
    assert res["id"] == 1
    assert res["result"]["serverInfo"]["name"] == "zoth-webgen-mcp"

def test_mcp_server_tools_list():
    req = {"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}}
    res = handle_request(req)
    assert res["id"] == 2
    tool_names = [t["name"] for t in res["result"]["tools"]]
    assert "webgen_list_templates" in tool_names
    assert "webgen_generate_site" in tool_names
    assert "webgen_generate_master_artifacts" in tool_names

def test_mcp_server_generate_site_call():
    with tempfile.TemporaryDirectory() as tmpdir:
        out_file = Path(tmpdir) / "mcp_site.html"
        req = {
            "jsonrpc": "2.0",
            "id": 3,
            "method": "tools/call",
            "params": {
                "name": "webgen_generate_site",
                "arguments": {
                    "template": "saas-dashboard",
                    "output_path": str(out_file)
                }
            }
        }
        res = handle_request(req)
        assert res["id"] == 3
        assert "isError" not in res
        assert out_file.exists()

def test_mcp_server_master_artifacts_call():
    with tempfile.TemporaryDirectory() as tmpdir:
        req = {
            "jsonrpc": "2.0",
            "id": 4,
            "method": "tools/call",
            "params": {
                "name": "webgen_generate_master_artifacts",
                "arguments": {
                    "template": "solana-web3-mint",
                    "output_dir": tmpdir
                }
            }
        }
        res = handle_request(req)
        assert res["id"] == 4
        assert "isError" not in res
        assert (Path(tmpdir) / "master-blueprint.json").exists()

def test_server_endpoints():
    import urllib.request
    import threading
    from server import run_server
    from http.server import ThreadingHTTPServer
    from server import WebGenHandler

    server = ThreadingHTTPServer(('127.0.0.1', 0), WebGenHandler)
    port = server.server_port
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()

    try:
        with urllib.request.urlopen(f"http://127.0.0.1:{port}/api/health") as res:
            assert res.status == 200
            data = json.loads(res.read().decode('utf-8'))
            assert data["status"] == "healthy"
            assert data["zero_egress"] is True

        with urllib.request.urlopen(f"http://127.0.0.1:{port}/api/templates") as res:
            assert res.status == 200
            data = json.loads(res.read().decode('utf-8'))
            assert "saas-dashboard" in data

        with urllib.request.urlopen(f"http://127.0.0.1:{port}/index.html") as res:
            assert res.status == 200
            html = res.read().decode('utf-8')
            assert "Zoth WebGen" in html
    finally:
        server.shutdown()
        server.server_close()

