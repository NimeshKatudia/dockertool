from flask import Flask, render_template
import psutil

app = Flask(__name__)

@app.route('/')
def index():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent

    # Update your HTML template with the machine statistics
    html = f"""
    <html>
    <head><title>Machine Statistics</title></head>
    <body>
    <h1>Machine Statistics</h1>
    <p>CPU Usage: {cpu_percent}%</p>
    <p>Memory Usage: {memory_percent}%</p>
    </body>
    </html>
    """

    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)