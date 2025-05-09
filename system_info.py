from flask import Flask, jsonify
import platform
import psutil

app = Flask(__name__)

@app.route("/sysinfo")
def sysinfo():
    info = {
        "os": platform.platform(),
        "cpu": platform.processor(),
        "cpu_cores": psutil.cpu_count(logical=True),
        "ram_gb": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "architecture": platform.architecture(),
        "machine": platform.machine(),
        "python_version": platform.python_version()
    }
    return jsonify(info)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
