from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # 개발용 시크릿 키

# 기본 디렉토리 생성
os.makedirs('data', exist_ok=True)
os.makedirs('posts', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
