# Instruções de Execução - Sistema Financeiro Simplificado

## 🚀 Guia Passo a Passo

### Requisitos do Sistema

- **Python**: 3.8 ou superior
- **pip**: Gerenciador de pacotes Python
- **Navegador**: Qualquer navegador moderno (Chrome, Firefox, Safari, Edge)
- **Espaço em disco**: Mínimo 100 MB
- **RAM**: Mínimo 512 MB

### Verificar Versão do Python

```bash
python3 --version
```

Você deve ver algo como `Python 3.11.0` ou superior.

---

## 📦 Instalação Completa

### Passo 1: Extrair o Projeto

```bash
# Extrair arquivo ZIP ou clonar repositório
cd sistema_financeiro_flask
```

### Passo 2: Criar Ambiente Virtual

```bash
# Linux/macOS
python3 -m venv venv

# Windows
python -m venv venv
```

### Passo 3: Ativar Ambiente Virtual

**Linux/macOS:**
```bash
source venv/bin/activate
```

**Windows (Command Prompt):**
```bash
venv\Scripts\activate
```

**Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```

Você deve ver `(venv)` no início da linha de comando.

### Passo 4: Instalar Dependências

```bash
pip install -r requirements.txt
```

Aguarde a instalação de todos os pacotes.

### Passo 5: Executar a Aplicação

```bash
python run.py
```

Você deve ver uma mensagem como:
```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

### Passo 6: Acessar no Navegador

Abra seu navegador e acesse:
```
http://localhost:5000
```

---

## 🔑 Primeiro Acesso

1. **Página de Login**: Você será redirecionado para a página de login
2. **Registrar**: Clique em "Registre-se aqui" para criar uma conta
3. **Preencher Formulário**:
   - Username: Escolha um nome de usuário único
   - Email: Digite um email válido
   - Senha: Escolha uma senha forte
4. **Registrar**: Clique em "Registrar"
5. **Login**: Faça login com suas credenciais
6. **Dashboard**: Você será redirecionado para o dashboard

---

## 📋 Primeiros Passos no Sistema

### 1. Criar Categorias

1. Clique em "Categorias" no menu
2. Clique em "+ Nova Categoria"
3. Preencha:
   - **Nome**: Ex: "Salário", "Alimentação", "Transporte"
   - **Tipo**: Escolha "Entrada" ou "Saída"
4. Clique em "Criar Categoria"
5. Repita para criar mais categorias

**Sugestões de Categorias:**
- **Entradas**: Salário, Freelance, Investimentos, Bônus
- **Saídas**: Alimentação, Transporte, Moradia, Saúde, Lazer

### 2. Registrar Lançamentos

1. Clique em "Lançamentos" no menu
2. Clique em "+ Novo Lançamento"
3. Preencha:
   - **Tipo**: Entrada ou Saída
   - **Categoria**: Selecione uma categoria criada
   - **Valor**: Digite um valor positivo (ex: 3000.00)
   - **Descrição**: Opcional (ex: "Salário de abril")
   - **Data**: Selecione a data do lançamento
4. Clique em "Registrar Lançamento"
5. Repita para registrar mais lançamentos

### 3. Visualizar Dashboard

1. Clique em "Dashboard" no menu
2. Você verá:
   - **Total de Entradas**: Soma de todas as entradas
   - **Total de Saídas**: Soma de todas as saídas
   - **Saldo**: Entradas - Saídas
   - **Últimos Lançamentos**: Tabela com os 10 últimos registros

---

## 🔍 Usando Filtros

1. Acesse "Lançamentos"
2. Use os filtros no topo:
   - **Tipo**: Filtrar por "Entradas" ou "Saídas"
   - **Categoria**: Filtrar por uma categoria específica
3. Clique em "Filtrar" para aplicar
4. Clique em "Limpar" para remover filtros

---

## ✏️ Editar e Deletar

### Editar um Lançamento

1. Acesse "Lançamentos"
2. Encontre o lançamento que deseja editar
3. Clique em "Editar"
4. Modifique os campos desejados
5. Clique em "Atualizar Lançamento"

### Deletar um Lançamento

1. Acesse "Lançamentos"
2. Encontre o lançamento que deseja deletar
3. Clique em "Deletar"
4. Confirme a deleção
5. O lançamento será removido

### Editar uma Categoria

1. Acesse "Categorias"
2. Encontre a categoria que deseja editar
3. Clique em "Editar"
4. Modifique os campos
5. Clique em "Atualizar Categoria"

### Deletar uma Categoria

1. Acesse "Categorias"
2. Encontre a categoria que deseja deletar
3. Clique em "Deletar"
4. Confirme a deleção
5. A categoria será removida (se não tiver lançamentos associados)

---

## 🛑 Parar a Aplicação

Para parar a aplicação:

1. Volte para o terminal onde está rodando
2. Pressione `CTRL+C`
3. A aplicação será encerrada

---

## 🔄 Reiniciar a Aplicação

Para reiniciar após parar:

```bash
# Certifique-se de estar no diretório correto
cd sistema_financeiro_flask

# Ative o ambiente virtual (se não estiver ativado)
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate  # Windows

# Execute novamente
python run.py
```

---

## 🗑️ Limpar Dados

### Resetar o Banco de Dados

Se quiser começar do zero e remover todos os dados:

1. Parar a aplicação (CTRL+C)
2. Deletar o arquivo do banco de dados:
   ```bash
   rm sistema_financeiro.db  # Linux/macOS
   # ou
   del sistema_financeiro.db  # Windows
   ```
3. Reiniciar a aplicação:
   ```bash
   python run.py
   ```
4. O banco será recriado vazio

---

## 🐛 Troubleshooting

### Erro: "ModuleNotFoundError: No module named 'flask'"

**Causa**: Ambiente virtual não ativado ou dependências não instaladas

**Solução**:
```bash
# Ativar ambiente virtual
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r requirements.txt
```

### Erro: "Porta 5000 já está em uso"

**Causa**: Outra aplicação está usando a porta 5000

**Solução 1**: Fechar outra instância da aplicação

**Solução 2**: Usar outra porta
```bash
# Editar run.py e mudar:
# app.run(debug=True, host='0.0.0.0', port=5000)
# para:
# app.run(debug=True, host='0.0.0.0', port=5001)
```

### Erro: "Banco de dados bloqueado"

**Causa**: Múltiplas instâncias acessando o banco simultaneamente

**Solução**:
1. Fechar todas as instâncias da aplicação
2. Aguardar alguns segundos
3. Reiniciar a aplicação

### Erro: "Senha incorreta" após registrar

**Causa**: Senha não foi salva corretamente

**Solução**:
1. Resetar o banco de dados (ver seção "Limpar Dados")
2. Registrar novamente

### Aplicação não abre no navegador

**Causa**: Porta 5000 não está acessível

**Solução**:
1. Verificar se a aplicação está rodando (ver mensagem no terminal)
2. Tentar acessar http://127.0.0.1:5000 em vez de http://localhost:5000
3. Verificar firewall

---

## 📊 Estrutura de Arquivos

```
sistema_financeiro_flask/
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   ├── models.py
│   ├── routes.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── dashboard.html
│   │   ├── categories.html
│   │   ├── create_category.html
│   │   ├── edit_category.html
│   │   ├── transactions.html
│   │   ├── create_transaction.html
│   │   └── edit_transaction.html
│   └── static/
├── venv/                    # Ambiente virtual (não versionado)
├── sistema_financeiro.db    # Banco de dados (criado automaticamente)
├── run.py
├── requirements.txt
├── README.md
├── SCRIPT_SQL.md
├── INSTRUCOES_EXECUCAO.md
├── GUIA_VIDEO_DEMONSTRACAO.md
└── .gitignore
```

---

## 🔐 Segurança

### Boas Práticas

1. **Nunca compartilhe sua senha**: Cada usuário tem sua própria senha
2. **Use senhas fortes**: Combine letras, números e símbolos
3. **Logout ao terminar**: Sempre clique em "Sair" ao finalizar
4. **Não acesse em WiFi público**: Especialmente sem VPN

### Para Produção

Se for colocar em produção:

1. Altere `FLASK_ENV` para `production` em `.env`
2. Gere uma `SECRET_KEY` forte:
   ```bash
   python3 -c "import secrets; print(secrets.token_hex(32))"
   ```
3. Use um servidor WSGI (Gunicorn, uWSGI)
4. Configure HTTPS/SSL
5. Use um banco de dados robusto (PostgreSQL, MySQL)

---

## 📞 Suporte

Se encontrar problemas:

1. Verifique se todas as dependências estão instaladas
2. Certifique-se de que o ambiente virtual está ativado
3. Verifique a porta 5000 está disponível
4. Tente resetar o banco de dados
5. Consulte o arquivo README.md para mais informações

---

**Aproveite o Sistema Financeiro Simplificado! 💰**
