# Guia de Demonstração em Vídeo

## 📹 Instruções para Gravar o Vídeo de Demonstração

**Duração recomendada**: 3 a 5 minutos

### Preparação

1. **Iniciar a aplicação**
   ```bash
   cd sistema_financeiro_flask
   source venv/bin/activate  # ou venv\Scripts\activate no Windows
   python run.py
   ```

2. **Abrir no navegador**
   - Acesse: http://localhost:5000

3. **Preparar dados de teste**
   - Crie uma conta de teste
   - Crie algumas categorias
   - Registre alguns lançamentos

---

## 🎬 Roteiro de Demonstração (3-5 minutos)

### Parte 1: Autenticação (30 segundos)

**O que mostrar:**
1. Página inicial com opção de Login/Registrar
2. Clicar em "Registrar"
3. Preencher formulário (username, email, senha)
4. Submeter e ver mensagem de sucesso
5. Fazer login com as credenciais criadas

**Fala sugerida:**
> "O Sistema Financeiro Simplificado começa com autenticação segura. Aqui vemos a página de registro onde o usuário cria uma conta com username, email e senha. A senha é armazenada com hash para segurança. Após registrar, fazemos login com as credenciais."

---

### Parte 2: Dashboard (30 segundos)

**O que mostrar:**
1. Página do Dashboard
2. Destacar os 3 cards: Total de Entradas, Total de Saídas, Saldo
3. Mostrar a seção "Ações Rápidas"
4. Mostrar últimos lançamentos na tabela

**Fala sugerida:**
> "Após login, o usuário chega ao Dashboard que oferece um resumo financeiro em tempo real. Vemos o total de entradas, o total de saídas e o saldo calculado automaticamente. Temos também ações rápidas para criar categorias ou registrar lançamentos, e uma tabela com os últimos lançamentos."

---

### Parte 3: Gerenciamento de Categorias (1 minuto)

**O que mostrar:**
1. Clicar em "Categorias" no menu
2. Listar categorias existentes (se houver)
3. Clicar em "+ Nova Categoria"
4. Preencher formulário (nome e tipo)
5. Submeter e ver mensagem de sucesso
6. Mostrar categoria criada na lista
7. Clicar em "Editar" para mostrar formulário de edição
8. Voltar sem salvar

**Fala sugerida:**
> "Agora vamos gerenciar categorias. Aqui podemos criar categorias personalizadas definindo um nome e um tipo: entrada (para receitas) ou saída (para despesas). Vemos a lista de categorias com opções para editar ou deletar. Cada categoria pertence ao usuário e é isolada de outros usuários do sistema."

---

### Parte 4: Registro de Lançamentos (1 minuto)

**O que mostrar:**
1. Clicar em "Lançamentos" no menu
2. Mostrar lista vazia ou com lançamentos
3. Clicar em "+ Novo Lançamento"
4. Preencher formulário completo:
   - Tipo: Entrada
   - Categoria: (selecionar uma)
   - Valor: 3000.00
   - Descrição: "Salário mensal"
   - Data: hoje
5. Submeter e ver mensagem de sucesso
6. Voltar à lista e mostrar lançamento criado
7. Criar um segundo lançamento de Saída

**Fala sugerida:**
> "Agora registramos lançamentos financeiros. Cada lançamento tem um tipo (entrada ou saída), uma categoria obrigatória, um valor positivo, uma descrição opcional e uma data. Aqui criamos uma entrada de R$ 3000 como salário. O sistema valida que o valor é positivo e que a categoria existe. Depois criamos uma saída para demonstrar como o sistema funciona com ambos os tipos."

---

### Parte 5: Filtros e Dashboard Atualizado (1 minuto)

**O que mostrar:**
1. Voltar para a página de Lançamentos
2. Usar filtro por tipo (mostrar apenas "Entradas")
3. Mostrar resultado filtrado
4. Limpar filtro
5. Usar filtro por categoria
6. Mostrar resultado filtrado
7. Voltar ao Dashboard
8. Mostrar que os valores foram atualizados (Entradas, Saídas, Saldo)

**Fala sugerida:**
> "O sistema oferece filtros avançados para consultar lançamentos. Podemos filtrar por tipo (entrada ou saída) ou por categoria. Aqui filtramos apenas as entradas e vemos apenas o salário. Depois filtramos por uma categoria específica. Voltando ao Dashboard, vemos que os totais foram atualizados automaticamente com base nos lançamentos registrados."

---

### Parte 6: Edição e Deleção (30 segundos)

**O que mostrar:**
1. Na lista de lançamentos, clicar em "Editar" em um lançamento
2. Modificar algum campo (ex: descrição)
3. Submeter e ver mensagem de sucesso
4. Voltar à lista
5. Clicar em "Deletar" em outro lançamento
6. Confirmar deleção
7. Ver mensagem de sucesso

**Fala sugerida:**
> "O sistema oferece operações CRUD completas. Podemos editar lançamentos para corrigir informações ou deletar lançamentos que foram registrados por engano. Todas as operações geram logs de auditoria para rastreabilidade."

---

### Parte 7: Regras de Negócio (30 segundos)

**O que mostrar:**
1. Tentar criar um lançamento com valor negativo ou zero
2. Mostrar mensagem de erro: "O valor deve ser positivo"
3. Tentar criar um lançamento sem categoria
4. Mostrar mensagem de erro: "Categoria é obrigatória"
5. Tentar criar uma categoria com tipo inválido
6. Mostrar mensagem de erro: "Tipo inválido"

**Fala sugerida:**
> "O sistema implementa regras de negócio rigorosas. O valor do lançamento deve ser sempre positivo - o tipo (entrada/saída) define se é positivo ou negativo. A categoria é obrigatória para cada lançamento. O tipo de categoria deve ser entrada ou saída. Todas essas validações são feitas no backend para garantir integridade dos dados."

---

### Parte 8: Logout (15 segundos)

**O que mostrar:**
1. Clicar em "Sair" no menu
2. Ser redirecionado para login
3. Tentar acessar uma rota protegida (ex: digitar /categories na URL)
4. Ser redirecionado para login

**Fala sugerida:**
> "Por fim, o sistema oferece logout seguro. Ao clicar em sair, a sessão é encerrada e o usuário é redirecionado para login. Rotas protegidas não podem ser acessadas sem autenticação, garantindo segurança dos dados."

---

## 📊 Estrutura Técnica a Mencionar

Durante o vídeo, mencione brevemente:

1. **Stack**: Python + Flask + SQLAlchemy + SQLite
2. **Banco de Dados**: 4 tabelas (users, categories, transactions, audit_logs)
3. **Autenticação**: Senhas com hash (werkzeug.security)
4. **Isolamento**: Cada usuário acessa apenas seus dados
5. **Auditoria**: Todas as operações são registradas
6. **Validações**: Backend valida todas as entradas

---

## 💡 Dicas para Gravar

1. **Qualidade**: Use resolução 1080p ou superior
2. **Áudio**: Use microfone de qualidade, fale claramente
3. **Velocidade**: Não fale muito rápido, deixe tempo para entender
4. **Edição**: Corte partes desnecessárias (erros, esperas)
5. **Legenda**: Considere adicionar legendas para melhor compreensão
6. **Demonstração**: Mostre funcionalidades reais, não apenas explicação

---

## ✅ Checklist Antes de Gravar

- [ ] Aplicação iniciada e funcionando
- [ ] Navegador limpo (sem abas extras)
- [ ] Dados de teste preparados
- [ ] Microfone testado
- [ ] Câmera/tela em boa resolução
- [ ] Tempo cronometrado (3-5 minutos)
- [ ] Roteiro memorizado ou anotado

---

## 🎯 Pontos-Chave a Destacar

1. **Funcionalidade**: Sistema completo e funcional
2. **Regras de Negócio**: Validações implementadas corretamente
3. **Banco de Dados**: 4 tabelas com relacionamentos
4. **Segurança**: Autenticação e isolamento de dados
5. **UX**: Interface intuitiva e responsiva
6. **Auditoria**: Rastreamento de ações

---

**Boa sorte com a demonstração! 🎬**
