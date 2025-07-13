from flask import Flask, request
from flask_babel import Babel
from routes import routes  # Import blueprint
import json

app = Flask(__name__)
app.register_blueprint(routes)

# Cấu hình Flask-Babel
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'vi']
app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

# Hàm chọn ngôn ngữ
def select_locale():
    return request.args.get('lang') or request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

# Khởi tạo Babel (cho Flask-Babel >= 3.x)
babel = Babel()
babel.init_app(app, locale_selector=select_locale)
    
if __name__ == '__main__':
    app.run(debug=True)
