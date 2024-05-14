from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Простой список для хранения сообщений
posts = []

@app.route('/')
def index():
    """Главная страница, отображает сообщения блога"""
    return render_template('index.html', posts=posts)

@app.route('/post', methods=['GET', 'POST'])
def post():
    """Страница для добавления нового сообщения"""
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts.append({'title': title, 'content': content})
        return redirect(url_for('index'))
    return render_template('post.html')

if __name__ == '__main__':
    app.run(debug=True)
