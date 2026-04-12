
from flask_login import LoginManager
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.config['SECRET_KEY'] = 'lab4-secret-key-2026'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'          # страница для неавторизованных
login_manager.login_message = 'Пожалуйста, авторизуйтесь для доступа к этой странице'
login_manager.login_message_category = 'error'

#Модель пользователя
class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

#Загружаем пользовтаеля по id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#Создание бд 
with app.app_context():
    db.create_all()
    print("База данных и таблицы созданы")



#Главная страница для авторизованных пользователей
@app.route('/')
@login_required
def index():
    return render_template('index.html', user=current_user)

#Страница входа
@app.route('/login', methods=['GET', 'POST'])
def login():
    #если пользователь авторизован, перенаправление на главную 
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not email or not password:
            flash('Пожалуйста, заполните все поля', 'error')
            return redirect(url_for('login'))
        
        #Поиск пользователя по email
        user = User.query.filter_by(email=email).first()
        
        if not user:
            flash('Пользователь с таким email не найден', 'error')
            return redirect(url_for('login'))
        
        if not check_password_hash(user.password, password):
            flash('Неверный пароль', 'error')
            return redirect(url_for('login'))
        
        login_user(user)
        flash(f'Добро пожаловать, {user.name}!', 'success')
        return redirect(url_for('index'))
    
    return render_template('login.html')

#Страница регистрации
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        if not name or not email or not password:
            flash('Пожалуйста, заполните все поля', 'error')
            return redirect(url_for('signup'))
        
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Пользователь с таким email уже существует', 'error')
            return redirect(url_for('signup'))
        
        hashed_password = generate_password_hash(password)
        
        new_user = User(
            name=name,
            email=email,
            password=hashed_password
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Регистрация прошла успешно! Теперь вы можете войти в систему.', 'success')
        return redirect(url_for('login'))
    
    return render_template('signup.html')

#Выход
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы успешно вышли из системы', 'info')
    return redirect(url_for('login'))




if __name__ == '__main__':
    app.run(debug=True)