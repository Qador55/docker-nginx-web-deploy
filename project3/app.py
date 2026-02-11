from flask import Flask, render_template_string, request, redirect, url_for
import redis

app = Flask(__name__)
# الاتصال بـ Redis
cache = redis.Redis(host='redis', port=6379, decode_responses=True)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Docker Decor Counter</title>
    <style>
        body { font-family: sans-serif; background: #f4f7f9; text-align: center; padding-top: 50px; }
        .card { background: white; padding: 30px; border-radius: 15px; display: inline-block; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        .whale { font-size: 50px; margin-bottom: 10px; }
        .btn { background: #007bff; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; font-size: 16px; }
        .btn:hover { background: #0056b3; }
        .message-list { list-style: none; padding: 0; margin-top: 20px; text-align: left; }
        .message-item { background: #e9ecef; padding: 8px; margin-bottom: 5px; border-radius: 4px; font-size: 14px; }
    </style>
</head>
<body>
    <div class="card">
        <div class="whale">🐳</div>
        <h2>Docker Enthusiasts Counter</h2>
        <p>Total Messages: <strong>{{ count }}</strong></p>
        
        <form action="/add" method="post">
            <button type="submit" class="btn">Click to Add: "Hello Docker Decor Enthusiasts!"</button>
        </form>

        <ul class="message-list">
            {% for msg in messages %}
                <li class="message-item">{{ msg }}</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    count = cache.incr('hits')
    # جلب آخر 5 رسائل من Redis
    messages = cache.lrange('decor_messages', 0, 4)
    return render_template_string(HTML_TEMPLATE, count=count, messages=messages)

@app.route('/add', method=['POST'])
def add_message():
    cache.lpush('decor_messages', "Hello to Docker Decor Enthusiasts! 🚀")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
