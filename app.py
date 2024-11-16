from flask import Flask, render_template, request

app = Flask(__name__)

# Trang chính
@app.route('/')
def home():
    return render_template('index.html')

# Trang xử lý form
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    message = request.form.get('message')
    return f"Xin chào {name}, cảm ơn bạn đã gửi lời nhắn: \"{message}\"!"

if __name__ == '__main__':
    app.run(debug=True)
