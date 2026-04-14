from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from .extensions import db
from .models import User, Category, Transaction, AuditLog

# Blueprints
auth_bp = Blueprint('auth', __name__)
dashboard_bp = Blueprint('dashboard', __name__)
categories_bp = Blueprint('categories', __name__)
transactions_bp = Blueprint('transactions', __name__)

# ============================================================================
# AUTENTICAÇÃO
# ============================================================================

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """Rota para registro de novo usuário."""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # Validações
        if not username or not email or not password:
            flash('Todos os campos são obrigatórios', 'error')
            return redirect(url_for('auth.register'))
        
        # Verificar se usuário já existe
        if User.query.filter_by(username=username).first():
            flash('Usuário já existe', 'error')
            return redirect(url_for('auth.register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email já cadastrado', 'error')
            return redirect(url_for('auth.register'))
        
        # Criar novo usuário
        user = User(
            username=username,
            email=email,
            password=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()
        
        flash('Usuário registrado com sucesso! Faça login.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """Rota para login de usuário."""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash(f'Bem-vindo, {user.username}!', 'success')
            return redirect(url_for('dashboard.index'))
        else:
            flash('Usuário ou senha inválidos', 'error')
    
    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    """Rota para logout de usuário."""
    session.clear()
    flash('Você foi desconectado', 'success')
    return redirect(url_for('auth.login'))


def login_required(f):
    """Decorator para proteger rotas que requerem autenticação."""
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('Você precisa fazer login', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function


# ============================================================================
# DASHBOARD
# ============================================================================

@dashboard_bp.route('/')
@login_required
def index():
    """Rota principal - Dashboard com resumo financeiro."""
    user_id = session['user_id']
    
    # Calcular totais
    total_entrada = db.session.query(db.func.sum(Transaction.value)).filter(
        Transaction.user_id == user_id,
        Transaction.type == 'entrada'
    ).scalar() or 0
    
    total_saida = db.session.query(db.func.sum(Transaction.value)).filter(
        Transaction.user_id == user_id,
        Transaction.type == 'saída'
    ).scalar() or 0
    
    saldo = total_entrada - total_saida
    
    # Últimas transações
    transactions = Transaction.query.filter_by(user_id=user_id).order_by(
        Transaction.date.desc()
    ).limit(10).all()
    
    return render_template('dashboard.html', 
                         total_entrada=total_entrada,
                         total_saida=total_saida,
                         saldo=saldo,
                         transactions=transactions)


# ============================================================================
# CATEGORIAS
# ============================================================================

@categories_bp.route('/categories')
@login_required
def list_categories():
    """Rota para listar categorias."""
    user_id = session['user_id']
    categories = Category.query.filter_by(user_id=user_id).all()
    return render_template('categories.html', categories=categories)


@categories_bp.route('/categories/create', methods=['GET', 'POST'])
@login_required
def create_category():
    """Rota para criar nova categoria."""
    if request.method == 'POST':
        name = request.form.get('name')
        type_ = request.form.get('type')
        user_id = session['user_id']
        
        # Validações
        if not name or not type_:
            flash('Nome e tipo são obrigatórios', 'error')
            return redirect(url_for('categories.create_category'))
        
        if type_ not in ['entrada', 'saída']:
            flash('Tipo inválido', 'error')
            return redirect(url_for('categories.create_category'))
        
        # Criar categoria
        category = Category(name=name, type=type_, user_id=user_id)
        db.session.add(category)
        db.session.commit()
        
        # Log de auditoria
        log = AuditLog(
            user_id=user_id,
            action='CREATE',
            entity_type='category',
            entity_id=category.id,
            new_value=f'name={name}, type={type_}'
        )
        db.session.add(log)
        db.session.commit()
        
        flash('Categoria criada com sucesso', 'success')
        return redirect(url_for('categories.list_categories'))
    
    return render_template('create_category.html')


@categories_bp.route('/categories/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_category(id):
    """Rota para editar categoria."""
    user_id = session['user_id']
    category = Category.query.filter_by(id=id, user_id=user_id).first_or_404()
    
    if request.method == 'POST':
        old_name = category.name
        old_type = category.type
        
        category.name = request.form.get('name')
        category.type = request.form.get('type')
        
        # Validações
        if not category.name or not category.type:
            flash('Nome e tipo são obrigatórios', 'error')
            return redirect(url_for('categories.edit_category', id=id))
        
        if category.type not in ['entrada', 'saída']:
            flash('Tipo inválido', 'error')
            return redirect(url_for('categories.edit_category', id=id))
        
        db.session.commit()
        
        # Log de auditoria
        log = AuditLog(
            user_id=user_id,
            action='UPDATE',
            entity_type='category',
            entity_id=id,
            old_value=f'name={old_name}, type={old_type}',
            new_value=f'name={category.name}, type={category.type}'
        )
        db.session.add(log)
        db.session.commit()
        
        flash('Categoria atualizada com sucesso', 'success')
        return redirect(url_for('categories.list_categories'))
    
    return render_template('edit_category.html', category=category)


@categories_bp.route('/categories/<int:id>/delete', methods=['POST'])
@login_required
def delete_category(id):
    """Rota para deletar categoria."""
    user_id = session['user_id']
    category = Category.query.filter_by(id=id, user_id=user_id).first_or_404()
    
    # Log de auditoria
    log = AuditLog(
        user_id=user_id,
        action='DELETE',
        entity_type='category',
        entity_id=id,
        old_value=f'name={category.name}, type={category.type}'
    )
    db.session.add(log)
    db.session.delete(category)
    db.session.commit()
    
    flash('Categoria deletada com sucesso', 'success')
    return redirect(url_for('categories.list_categories'))


# ============================================================================
# LANÇAMENTOS
# ============================================================================

@transactions_bp.route('/transactions')
@login_required
def list_transactions():
    """Rota para listar lançamentos com filtros."""
    user_id = session['user_id']
    
    # Filtros
    type_filter = request.args.get('type')
    category_filter = request.args.get('category')
    
    query = Transaction.query.filter_by(user_id=user_id)
    
    if type_filter and type_filter in ['entrada', 'saída']:
        query = query.filter_by(type=type_filter)
    
    if category_filter:
        query = query.filter_by(category_id=int(category_filter))
    
    transactions = query.order_by(Transaction.date.desc()).all()
    categories = Category.query.filter_by(user_id=user_id).all()
    
    return render_template('transactions.html', 
                         transactions=transactions,
                         categories=categories,
                         type_filter=type_filter,
                         category_filter=category_filter)


@transactions_bp.route('/transactions/create', methods=['GET', 'POST'])
@login_required
def create_transaction():
    """Rota para criar novo lançamento."""
    user_id = session['user_id']
    
    if request.method == 'POST':
        category_id = request.form.get('category_id')
        value = request.form.get('value')
        description = request.form.get('description')
        type_ = request.form.get('type')
        date_str = request.form.get('date')
        
        # Validações
        if not category_id or not value or not type_:
            flash('Categoria, valor e tipo são obrigatórios', 'error')
            return redirect(url_for('transactions.create_transaction'))
        
        try:
            value = float(value)
            if value <= 0:
                flash('O valor deve ser positivo', 'error')
                return redirect(url_for('transactions.create_transaction'))
        except ValueError:
            flash('Valor inválido', 'error')
            return redirect(url_for('transactions.create_transaction'))
        
        if type_ not in ['entrada', 'saída']:
            flash('Tipo inválido', 'error')
            return redirect(url_for('transactions.create_transaction'))
        
        # Verificar se categoria pertence ao usuário
        category = Category.query.filter_by(id=int(category_id), user_id=user_id).first()
        if not category:
            flash('Categoria inválida', 'error')
            return redirect(url_for('transactions.create_transaction'))
        
        # Criar lançamento
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d') if date_str else datetime.utcnow()
        except ValueError:
            date_obj = datetime.utcnow()
        
        transaction = Transaction(
            user_id=user_id,
            category_id=int(category_id),
            value=value,
            description=description,
            type=type_,
            date=date_obj
        )
        db.session.add(transaction)
        db.session.commit()
        
        # Log de auditoria
        log = AuditLog(
            user_id=user_id,
            action='CREATE',
            entity_type='transaction',
            entity_id=transaction.id,
            new_value=f'value={value}, type={type_}, category_id={category_id}'
        )
        db.session.add(log)
        db.session.commit()
        
        flash('Lançamento criado com sucesso', 'success')
        return redirect(url_for('transactions.list_transactions'))
    
    categories = Category.query.filter_by(user_id=user_id).all()
    return render_template('create_transaction.html', categories=categories)


@transactions_bp.route('/transactions/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_transaction(id):
    """Rota para editar lançamento."""
    user_id = session['user_id']
    transaction = Transaction.query.filter_by(id=id, user_id=user_id).first_or_404()
    
    if request.method == 'POST':
        old_value = transaction.value
        old_type = transaction.type
        old_category_id = transaction.category_id
        
        transaction.category_id = int(request.form.get('category_id'))
        transaction.value = float(request.form.get('value'))
        transaction.description = request.form.get('description')
        transaction.type = request.form.get('type')
        
        # Validações
        if transaction.value <= 0:
            flash('O valor deve ser positivo', 'error')
            return redirect(url_for('transactions.edit_transaction', id=id))
        
        if transaction.type not in ['entrada', 'saída']:
            flash('Tipo inválido', 'error')
            return redirect(url_for('transactions.edit_transaction', id=id))
        
        db.session.commit()
        
        # Log de auditoria
        log = AuditLog(
            user_id=user_id,
            action='UPDATE',
            entity_type='transaction',
            entity_id=id,
            old_value=f'value={old_value}, type={old_type}, category_id={old_category_id}',
            new_value=f'value={transaction.value}, type={transaction.type}, category_id={transaction.category_id}'
        )
        db.session.add(log)
        db.session.commit()
        
        flash('Lançamento atualizado com sucesso', 'success')
        return redirect(url_for('transactions.list_transactions'))
    
    categories = Category.query.filter_by(user_id=user_id).all()
    return render_template('edit_transaction.html', transaction=transaction, categories=categories)


@transactions_bp.route('/transactions/<int:id>/delete', methods=['POST'])
@login_required
def delete_transaction(id):
    """Rota para deletar lançamento."""
    user_id = session['user_id']
    transaction = Transaction.query.filter_by(id=id, user_id=user_id).first_or_404()
    
    # Log de auditoria
    log = AuditLog(
        user_id=user_id,
        action='DELETE',
        entity_type='transaction',
        entity_id=id,
        old_value=f'value={transaction.value}, type={transaction.type}'
    )
    db.session.add(log)
    db.session.delete(transaction)
    db.session.commit()
    
    flash('Lançamento deletado com sucesso', 'success')
    return redirect(url_for('transactions.list_transactions'))
