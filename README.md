# Sistema Financeiro 

Um sistema web elegante e completo para controle de finanças pessoais, desenvolvido em **Python + Flask** com banco de dados SQLite.

## Descrição do Sistema

O Sistema Financeiro Simplificado é uma aplicação que permite aos usuários gerenciar suas finanças pessoais de forma simples e eficiente. Através de uma interface intuitiva, os usuários podem:

- **Registrar entradas e saídas** de dinheiro
- **Organizar lançamentos por categorias** personalizadas
- **Visualizar resumo financeiro** em tempo real
- **Filtrar e consultar** histórico de transações
- **Rastrear ações** através de logs de auditoria

## Arquitetura Técnica

### Stack Tecnológico

| Componente | Tecnologia |
|-----------|-----------|
| **Backend** | Python 3.11 + Flask 3.1.3 |
| **ORM** | SQLAlchemy 2.0.49 |
| **Banco de Dados** | SQLite 3 |
| **Frontend** | HTML5 + CSS3 + Jinja2 |
| **Gerenciamento de Dependências** | pip + venv |

### Estrutura de Diretórios

```
sistema_financeiro_flask/
├── src/
│   ├── __init__.py           # Factory da aplicação Flask
│   ├── config.py             # Configurações (dev, prod, test)
│   ├── extensions.py         # Inicialização do SQLAlchemy
│   ├── models.py             # Modelos de dados (ORM)
│   ├── routes.py             # Todas as rotas da aplicação
│   ├── templates/            # Templates HTML Jinja2
│   │   ├── base.html         # Template base
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   ├── categories.html
│   │   ├── create_category.html
│   │   ├── edit_category.html
│   │   ├── transactions.html
│   │   ├── create_transaction.html
│   │   └── edit_transaction.html
│   └── static/               # Arquivos estáticos (CSS, JS)
├── venv/                     # Ambiente virtual Python
├── run.py                    # Ponto de entrada da aplicação
├── .env                      # Variáveis de ambiente
├── .gitignore                # Configuração Git
└── README.md                 # Este arquivo
```

## Banco de Dados

### Tabelas

#### 1. **users** - Usuários do sistema
Armazena informações de autenticação e perfil dos usuários.

| Campo | Tipo | Restrições | Descrição |
|-------|------|-----------|-----------|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Identificador único |
| username | VARCHAR(100) | UNIQUE, NOT NULL | Nome de usuário |
| email | VARCHAR(120) | UNIQUE, NOT NULL | Email do usuário |
| password | VARCHAR(255) | NOT NULL | Senha (hash) |
| created_at | DATETIME | NOT NULL, DEFAULT NOW | Data de criação |
| updated_at | DATETIME | NOT NULL, DEFAULT NOW | Data de atualização |

#### 2. **categories** - Categorias financeiras
Define as categorias para classificar lançamentos (entrada ou saída).

| Campo | Tipo | Restrições | Descrição |
|-------|------|-----------|-----------|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Identificador único |
| user_id | INTEGER | FOREIGN KEY (users.id), NOT NULL | Usuário proprietário |
| name | VARCHAR(100) | NOT NULL | Nome da categoria |
| type | VARCHAR(10) | NOT NULL | Tipo: 'entrada' ou 'saída' |
| created_at | DATETIME | NOT NULL, DEFAULT NOW | Data de criação |
| updated_at | DATETIME | NOT NULL, DEFAULT NOW | Data de atualização |

#### 3. **transactions** - Lançamentos financeiros
Registra todas as entradas e saídas de dinheiro.

| Campo | Tipo | Restrições | Descrição |
|-------|------|-----------|-----------|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Identificador único |
| user_id | INTEGER | FOREIGN KEY (users.id), NOT NULL | Usuário proprietário |
| category_id | INTEGER | FOREIGN KEY (categories.id), NOT NULL | Categoria do lançamento |
| value | FLOAT | NOT NULL | Valor da transação |
| description | VARCHAR(255) | NULL | Descrição opcional |
| type | VARCHAR(10) | NOT NULL | Tipo: 'entrada' ou 'saída' |
| date | DATETIME | NOT NULL, DEFAULT NOW | Data do lançamento |
| created_at | DATETIME | NOT NULL, DEFAULT NOW | Data de criação |
| updated_at | DATETIME | NOT NULL, DEFAULT NOW | Data de atualização |

#### 4. **audit_logs** - Histórico de ações
Rastreia todas as operações (CREATE, UPDATE, DELETE) para auditoria.

| Campo | Tipo | Restrições | Descrição |
|-------|------|-----------|-----------|
| id | INTEGER | PRIMARY KEY, AUTO_INCREMENT | Identificador único |
| user_id | INTEGER | FOREIGN KEY (users.id), NOT NULL | Usuário que realizou ação |
| action | VARCHAR(100) | NOT NULL | Tipo de ação (CREATE, UPDATE, DELETE) |
| entity_type | VARCHAR(50) | NOT NULL | Tipo de entidade (category, transaction) |
| entity_id | INTEGER | NOT NULL | ID da entidade modificada |
| old_value | TEXT | NULL | Valor anterior (para UPDATE) |
| new_value | TEXT | NULL | Novo valor (para CREATE/UPDATE) |
| timestamp | DATETIME | NOT NULL, DEFAULT NOW | Data/hora da ação |

### Relacionamentos

```
users (1) ──────→ (N) categories
users (1) ──────→ (N) transactions
users (1) ──────→ (N) audit_logs
categories (1) ──→ (N) transactions
```

## Rotas da Aplicação

### Autenticação

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/register` | Página de registro |
| POST | `/register` | Criar novo usuário |
| GET | `/login` | Página de login |
| POST | `/login` | Autenticar usuário |
| GET | `/logout` | Desconectar usuário |

### Dashboard

| Método | Rota | Descrição | Autenticação |
|--------|------|-----------|--------------|
| GET | `/` | Dashboard com resumo financeiro |  Obrigatória |

### Categorias

| Método | Rota | Descrição | Autenticação |
|--------|------|-----------|--------------|
| GET | `/categories` | Listar todas as categorias |  Obrigatória |
| GET | `/categories/create` | Formulário de criação |  Obrigatória |
| POST | `/categories/create` | Criar nova categoria |  Obrigatória |
| GET | `/categories/<id>/edit` | Formulário de edição |  Obrigatória |
| POST | `/categories/<id>/edit` | Atualizar categoria |  Obrigatória |
| POST | `/categories/<id>/delete` | Deletar categoria |  Obrigatória |

### Lançamentos

| Método | Rota | Descrição | Autenticação |
|--------|------|-----------|--------------|
| GET | `/transactions` | Listar lançamentos (com filtros) |  Obrigatória |
| GET | `/transactions/create` | Formulário de criação |  Obrigatória |
| POST | `/transactions/create` | Criar novo lançamento |  Obrigatória |
| GET | `/transactions/<id>/edit` | Formulário de edição |  Obrigatória |
| POST | `/transactions/<id>/edit` | Atualizar lançamento |  Obrigatória |
| POST | `/transactions/<id>/delete` | Deletar lançamento |  Obrigatória |

**Parâmetros de Filtro (GET `/transactions`):**
- `type`: Filtrar por tipo ('entrada' ou 'saída')
- `category`: Filtrar por ID da categoria

## Regras de Negócio

### 1. Validação de Usuário
- **Regra**: Cada usuário deve ter username e email únicos
- **Implementação**: Verificação no banco antes de criar usuário
- **Erro**: "Usuário já existe" ou "Email já cadastrado"

### 2. Isolamento de Dados
- **Regra**: Usuários só podem acessar suas próprias categorias e lançamentos
- **Implementação**: Filtro `user_id` em todas as queries
- **Segurança**: Proteção contra acesso não autorizado

### 3. Validação de Categoria
- **Regra**: Tipo deve ser 'entrada' ou 'saída'
- **Implementação**: Validação no backend antes de salvar
- **Erro**: "Tipo inválido"

### 4. Validação de Lançamento - Valor Positivo
- **Regra**: O valor do lançamento deve ser **sempre positivo** (> 0)
- **Implementação**: Validação `if value <= 0: error`
- **Erro**: "O valor deve ser positivo"
- **Justificativa**: O tipo (entrada/saída) define se é positivo ou negativo, não o valor

### 5. Validação de Lançamento - Categoria Obrigatória
- **Regra**: Todo lançamento deve ter uma categoria associada
- **Implementação**: Campo `category_id` NOT NULL + validação
- **Erro**: "Categoria inválida" ou "Categoria é obrigatória"

### 6. Validação de Lançamento - Tipo Válido
- **Regra**: Tipo deve ser 'entrada' ou 'saída'
- **Implementação**: Validação `if type not in ['entrada', 'saída']: error`
- **Erro**: "Tipo inválido"

### 7. Filtros de Lançamento
- **Regra**: Permitir filtrar por tipo e categoria
- **Implementação**: Parâmetros GET com queries dinâmicas
- **Funcionalidade**: Filtro por tipo (entrada/saída) e/ou por categoria

### 8. Dashboard - Resumo Financeiro
- **Regra**: Calcular automaticamente total de entradas, saídas e saldo
- **Implementação**: Queries com SUM agregado
- **Fórmula**: `Saldo = Total Entradas - Total Saídas`

### 9. Auditoria - Histórico de Ações
- **Regra**: Registrar todas as operações (CREATE, UPDATE, DELETE)
- **Implementação**: Log automático em `audit_logs` após cada operação
- **Rastreabilidade**: Identificar quem fez o quê e quando

## Como Executar o Projeto

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clonar ou extrair o projeto**
   ```bash
   cd sistema_financeiro_flask
   ```

2. **Criar ambiente virtual**
   ```bash
   python3 -m venv venv
   ```

3. **Ativar ambiente virtual**
   - **Linux/macOS:**
     ```bash
     source venv/bin/activate
     ```
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```

4. **Instalar dependências**
   ```bash
   pip install -r requirements.txt
   ```

5. **Executar a aplicação**
   ```bash
   python run.py
   ```

6. **Acessar no navegador**
   ```
   http://localhost:5000
   ```

### Primeira Execução

Ao iniciar a aplicação pela primeira vez:
1. O banco de dados SQLite será criado automaticamente (`sistema_financeiro.db`)
2. Todas as tabelas serão criadas automaticamente
3. Você será redirecionado para a página de login
4. Clique em "Registrar" para criar uma nova conta
5. Faça login com suas credenciais
6. Comece a usar o sistema!

## Dependências

```
Flask==3.1.3
Flask-SQLAlchemy==3.1.1
SQLAlchemy==2.0.49
python-dotenv==1.2.2
Werkzeug==3.0.0
```

Instale todas com:
```bash
pip install -r requirements.txt
```

## Segurança

- **Senhas**: Armazenadas com hash (werkzeug.security)
- **Sessões**: Gerenciadas pelo Flask com SECRET_KEY
- **Autenticação**: Decorator `@login_required` protege rotas
- **Isolamento**: Cada usuário acessa apenas seus dados
- **Validação**: Todas as entradas são validadas no backend

## Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
FLASK_APP=run.py
FLASK_ENV=development
DATABASE_URL=sqlite:///sistema_financeiro.db
SECRET_KEY=sua-chave-secreta-aqui-mude-em-producao
```

**Nota**: Para produção, altere `FLASK_ENV` para `production` e use uma `SECRET_KEY` forte.

## Funcionalidades Principais

 **Autenticação de Usuários**
- Registro de novos usuários
- Login seguro com hash de senha
- Logout e gerenciamento de sessão

 **Gestão de Categorias**
- Criar categorias personalizadas
- Definir tipo (entrada ou saída)
- Editar e deletar categorias
- Isolamento por usuário

 **Registro de Lançamentos**
- Criar entradas e saídas
- Associar a uma categoria
- Adicionar descrição opcional
- Definir data do lançamento
- Editar e deletar lançamentos

 **Dashboard Financeiro**
- Resumo de entradas totais
- Resumo de saídas totais
- Cálculo automático de saldo
- Últimos lançamentos registrados

 **Filtros Avançados**
- Filtrar por tipo (entrada/saída)
- Filtrar por categoria
- Combinar múltiplos filtros

 **Auditoria e Histórico**
- Log de todas as operações
- Rastreamento de quem fez o quê
- Histórico completo de mudanças

## Interface

A aplicação possui uma interface elegante e intuitiva com:
- Design responsivo
- Cores sofisticadas (gradiente roxo)
- Navegação clara e simples
- Formulários validados
- Mensagens de feedback (sucesso/erro)
- Tabelas organizadas com ações

## Exemplo de Uso

1. **Registrar usuário**: Acesse `/register` e crie uma conta
2. **Criar categorias**: Vá para "Categorias" e crie "Salário" (entrada) e "Alimentação" (saída)
3. **Registrar lançamento**: Clique em "+ Novo Lançamento" e registre uma entrada de R$ 3000 (Salário)
4. **Ver dashboard**: Volte ao dashboard e veja o saldo atualizado
5. **Filtrar**: Use os filtros para visualizar apenas entradas ou apenas uma categoria

## Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'flask'"
**Solução**: Ative o ambiente virtual e instale as dependências
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Erro: "Banco de dados bloqueado"
**Solução**: Feche outras instâncias da aplicação e tente novamente

### Erro: "Porta 5000 já está em uso"
**Solução**: Altere a porta em `run.py` ou libere a porta 5000

## Referências

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Werkzeug Security](https://werkzeug.palletsprojects.com/security/)





