#!/bin/bash

# ============================================================================
# Script de Setup para GitHub - Sistema Financeiro Simplificado
# ============================================================================
# Este script configura o repositório Git local e faz push para GitHub
# IMPORTANTE: Execute este script no seu computador, não em um servidor
# ============================================================================

echo "🚀 Iniciando configuração do repositório GitHub..."
echo ""

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Verificar se Git está instalado
if ! command -v git &> /dev/null; then
    echo -e "${RED}❌ Git não está instalado. Por favor, instale Git primeiro.${NC}"
    exit 1
fi

# Verificar se estamos no diretório correto
if [ ! -f "run.py" ]; then
    echo -e "${RED}❌ Erro: Execute este script no diretório raiz do projeto${NC}"
    echo "   (O arquivo run.py deve estar no diretório atual)"
    exit 1
fi

echo -e "${GREEN}✓ Diretório correto detectado${NC}"
echo ""

# ============================================================================
# CONFIGURAÇÃO GIT LOCAL
# ============================================================================

echo "📝 Configurando repositório Git local..."

# Inicializar repositório se não existir
if [ ! -d ".git" ]; then
    git init
    echo -e "${GREEN}✓ Repositório Git inicializado${NC}"
else
    echo -e "${GREEN}✓ Repositório Git já existe${NC}"
fi

echo ""

# ============================================================================
# CONFIGURAR CREDENCIAIS (Opcional)
# ============================================================================

read -p "Deseja configurar seu nome e email no Git? (s/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Ss]$ ]]; then
    read -p "Digite seu nome (ex: João Silva): " git_name
    read -p "Digite seu email (ex: joao@example.com): " git_email
    
    git config user.name "$git_name"
    git config user.email "$git_email"
    
    echo -e "${GREEN}✓ Credenciais configuradas${NC}"
fi

echo ""

# ============================================================================
# ADICIONAR ARQUIVOS
# ============================================================================

echo "📦 Adicionando arquivos ao Git..."

# Remover ambiente virtual do git (se existir)
echo "venv/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo "*.db" >> .gitignore
echo ".env" >> .gitignore
echo "*.pyc" >> .gitignore
echo "instance/" >> .gitignore

git add -A
echo -e "${GREEN}✓ Arquivos adicionados${NC}"

echo ""

# ============================================================================
# CRIAR COMMIT INICIAL
# ============================================================================

echo "💾 Criando commit inicial..."

git commit -m "Initial commit: Sistema Financeiro Simplificado

- Backend: Python + Flask + SQLAlchemy
- Banco de dados: 4 tabelas (users, categories, transactions, audit_logs)
- Frontend: HTML5 + CSS3 + Jinja2
- Funcionalidades: Autenticação, CRUD, Dashboard, Filtros, Auditoria
- Documentação: README, Script SQL, Instruções de execução"

echo -e "${GREEN}✓ Commit criado${NC}"

echo ""

# ============================================================================
# CONECTAR AO REPOSITÓRIO REMOTO
# ============================================================================

echo "🔗 Conectando ao repositório remoto..."
echo ""

read -p "Digite seu username do GitHub (ex: psanttana): " github_user
read -p "Digite o nome do repositório (ex: Sistema-Financeiro): " repo_name

# Validar entrada
if [ -z "$github_user" ] || [ -z "$repo_name" ]; then
    echo -e "${RED}❌ Username ou nome do repositório não podem estar vazios${NC}"
    exit 1
fi

# Adicionar remote
remote_url="https://github.com/${github_user}/${repo_name}.git"
git remote remove origin 2>/dev/null  # Remover se já existir
git remote add origin "$remote_url"

echo -e "${GREEN}✓ Remote adicionado: $remote_url${NC}"

echo ""

# ============================================================================
# FAZER PUSH PARA GITHUB
# ============================================================================

echo "📤 Fazendo push para GitHub..."
echo ""
echo -e "${YELLOW}⚠️  Você será solicitado a autenticar no GitHub${NC}"
echo "   Use seu token de acesso pessoal como senha"
echo ""

# Tentar push
if git push -u origin main 2>/dev/null; then
    echo -e "${GREEN}✓ Push realizado com sucesso na branch main${NC}"
elif git push -u origin master 2>/dev/null; then
    echo -e "${GREEN}✓ Push realizado com sucesso na branch master${NC}"
else
    echo -e "${RED}❌ Erro ao fazer push${NC}"
    echo ""
    echo "Possíveis soluções:"
    echo "1. Verifique se o repositório existe no GitHub"
    echo "2. Verifique se o token está correto"
    echo "3. Tente fazer push manualmente:"
    echo "   git push -u origin main"
    exit 1
fi

echo ""

# ============================================================================
# SUCESSO
# ============================================================================

echo -e "${GREEN}════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}✅ SUCESSO! Projeto enviado para GitHub${NC}"
echo -e "${GREEN}════════════════════════════════════════════════════════════${NC}"
echo ""
echo "📍 Repositório: $remote_url"
echo ""
echo "Próximos passos:"
echo "1. Acesse: https://github.com/${github_user}/${repo_name}"
echo "2. Verifique se todos os arquivos foram enviados"
echo "3. Adicione uma descrição no repositório"
echo "4. Configure o README como página inicial"
echo ""
echo -e "${GREEN}Projeto pronto para apresentação ao professor! 🎉${NC}"
