# Guia: Enviando o Projeto para GitHub

## 🔐 Segurança em Primeiro Lugar

**NUNCA compartilhe seu token de acesso em chats, emails ou mensagens!**

Este guia usa um script que você executa **localmente no seu computador**, mantendo seu token seguro.

---

## 📋 Pré-requisitos

1. **Git instalado** no seu computador
   - [Download Git](https://git-scm.com/download)
   - Verifique: `git --version`

2. **Repositório criado no GitHub**
   - Acesse: https://github.com/new
   - Nome: `Sistema-Financeiro`
   - Descrição: "Sistema de controle financeiro pessoal com Python + Flask"
   - Deixe vazio (não inicialize com README)
   - Clique em "Create repository"

3. **Token de acesso pessoal do GitHub**
   - Acesse: https://github.com/settings/tokens
   - Clique em "Generate new token"
   - Selecione apenas: `repo` (acesso completo a repositórios)
   - Expiration: 1 hora (para segurança)
   - Clique em "Generate token"
   - **COPIE o token** (você não verá novamente)

---

## 🚀 Passo a Passo

### 1. Preparar o Projeto Localmente

```bash
# Abra o terminal/PowerShell no diretório do projeto
cd /caminho/para/sistema_financeiro_flask

# Verifique se o arquivo run.py existe
ls run.py  # Linux/macOS
dir run.py # Windows
```

### 2. Executar o Script de Setup

**Linux/macOS:**
```bash
chmod +x setup_github.sh
./setup_github.sh
```

**Windows (PowerShell):**
```powershell
# Execute como administrador
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
.\setup_github.sh
```

**Windows (Git Bash):**
```bash
chmod +x setup_github.sh
./setup_github.sh
```

### 3. Responder as Perguntas

O script fará as seguintes perguntas:

```
1. Deseja configurar seu nome e email no Git? (s/n)
   → Responda: s
   → Digite seu nome: João Silva
   → Digite seu email: joao@example.com

2. Digite seu username do GitHub (ex: psanttana)
   → Responda: psanttana

3. Digite o nome do repositório (ex: Sistema-Financeiro)
   → Responda: Sistema-Financeiro
```

### 4. Autenticar no GitHub

Quando o script pedir autenticação:

```
Username for 'https://github.com': psanttana
Password for 'https://psanttana@github.com': 
```

**No campo "Password", cole seu token de acesso**

```
Password for 'https://psanttana@github.com': ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 5. Aguardar Conclusão

O script fará automaticamente:
- ✅ Inicializar repositório Git
- ✅ Configurar credenciais
- ✅ Adicionar todos os arquivos
- ✅ Criar commit inicial
- ✅ Conectar ao repositório remoto
- ✅ Fazer push para GitHub

---

## ✅ Verificar Sucesso

Após o script terminar:

1. Acesse: `https://github.com/psanttana/Sistema-Financeiro`
2. Verifique se todos os arquivos estão lá:
   - `src/` (código Python)
   - `README.md`
   - `SCRIPT_SQL.md`
   - `INSTRUCOES_EXECUCAO.md`
   - `GUIA_VIDEO_DEMONSTRACAO.md`
   - `requirements.txt`
   - `run.py`

3. Clique em "Settings" e adicione uma descrição:
   - **About**: "Sistema de controle financeiro pessoal"
   - **Website**: (opcional)

---

## 🔧 Se Algo Deu Errado

### Erro: "fatal: remote origin already exists"

```bash
git remote remove origin
# Execute o script novamente
```

### Erro: "Authentication failed"

1. Verifique se o token está correto
2. Verifique se o token não expirou
3. Gere um novo token em: https://github.com/settings/tokens

### Erro: "Repository not found"

1. Verifique se o repositório foi criado no GitHub
2. Verifique se o username está correto
3. Verifique se o nome do repositório está correto

### Erro: "fatal: branch master does not exist"

```bash
# Se a branch padrão é 'main' em vez de 'master'
git branch -M main
git push -u origin main
```

---

## 📝 Após Enviar para GitHub

1. **Adicione um .gitignore melhorado** (já incluído no projeto)

2. **Configure o repositório:**
   - Vá para Settings → General
   - Marque "Require a pull request review before merging"
   - Marque "Automatically delete head branches"

3. **Adicione uma descrição do repositório:**
   - Clique em "Edit" ao lado do nome
   - Adicione descrição e website (opcional)

4. **Compartilhe com seu professor:**
   - Copie o link: `https://github.com/psanttana/Sistema-Financeiro`
   - Envie via email ou plataforma de aula

---

## 🔒 Boas Práticas de Segurança

✅ **Faça:**
- Usar tokens com expiração curta
- Usar tokens com permissões limitadas
- Revogar tokens após usar
- Usar autenticação de dois fatores no GitHub

❌ **Não faça:**
- Compartilhar tokens em chats ou emails
- Commitar tokens no repositório
- Usar a mesma senha para GitHub e outros serviços
- Deixar tokens expirados no seu computador

---

## 📞 Suporte

Se encontrar problemas:

1. Verifique se Git está instalado: `git --version`
2. Verifique se o repositório existe no GitHub
3. Verifique se o token está correto e não expirou
4. Tente fazer push manualmente: `git push -u origin main`

---

**Seu projeto está pronto para o GitHub! 🚀**
