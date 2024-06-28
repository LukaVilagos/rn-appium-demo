import os
from flask import render_template, request, redirect, url_for, Flask, send_from_directory
from database.models import Report, Test, Screenshot
import subprocess
import base64
import platform
from pony.orm import db_session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/screenshots')
@db_session
def screenshots():
    screenshots_folder = "static/screenshots"
    if not os.path.exists(screenshots_folder):
        os.makedirs(screenshots_folder)
    screenshots = []
    
    for filename in os.listdir(screenshots_folder):
        if filename.endswith('.png'):
            with open(os.path.join(screenshots_folder, filename), 'rb') as f:
                image_path = os.path.join(screenshots_folder, filename)
                screenshots.append([filename, image_path])
                
    return render_template('screenshots.html', screenshots=screenshots)

@app.route('/reports')
@db_session
def reports():
    reports_folder = "reports"
    if not os.path.exists(reports_folder):
        os.makedirs(reports_folder)
    reports = []
    
    for filename in os.listdir(reports_folder):
        if filename.endswith('.html'):
            reports.append([filename, filename])  # Only need the filename, not the full path
    
    return render_template('reports.html', reports=reports)

@app.route('/reports/<path:filename>')
def download_report(filename):
    reports_folder = "reports"
    return send_from_directory(reports_folder, filename)

@app.route('/tests', methods=['GET', 'POST'])
@db_session
def tests():
    tests_folder = "tests"
    if not os.path.exists(tests_folder):
        os.makedirs(tests_folder)
    test_files = []
    
    for filename in os.listdir(tests_folder):
        if filename.endswith('.py'):
            test_files.append([filename, filename])  # Only need the filename, not the full path
    
    return render_template('tests.html', test_files=test_files)

@app.route('/tests/<path:filename>')
def download_test_file(filename):
    tests_folder = "tests"
    return send_from_directory(tests_folder, filename)

@app.route('/run_test', methods=['POST'])
def run_test():
    test_file = request.form['test_file']
    test_command = f"pytest tests/{test_file}"
    
    if platform.system() == "Windows":
        subprocess.run(["start", "cmd", "/k", test_command], shell=True, cwd=os.getcwd())
    else:
        subprocess.run(["gnome-terminal", "--", "bash", "-c", f"{test_command}; exec bash"], cwd=os.getcwd())
    
    return redirect(url_for('tests'))
        
if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0", debug=True)
