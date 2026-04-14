# Script SQL - Sistema Financeiro Simplificado

Este documento contém o script SQL completo para criar o banco de dados e todas as tabelas do Sistema Financeiro Simplificado.

## Criação do Banco de Dados

```sql
CREATE DATABASE IF NOT EXISTS sistema_financeiro;
USE sistema_financeiro;
```

## Tabela: users

Armazena informações dos usuários do sistema.

```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL,
    INDEX idx_username (username),
    INDEX idx_email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

## Tabela: categories

Armazena as categorias financeiras (entrada ou saída).

```sql
CREATE TABLE categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    type VARCHAR(10) NOT NULL CHECK (type IN ('entrada', 'saída')),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_type (type)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

## Tabela: transactions

Armazena todos os lançamentos financeiros (entradas e saídas).

```sql
CREATE TABLE transactions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    category_id INT NOT NULL,
    value FLOAT NOT NULL CHECK (value > 0),
    description VARCHAR(255),
    type VARCHAR(10) NOT NULL CHECK (type IN ('entrada', 'saída')),
    date DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE RESTRICT,
    INDEX idx_user_id (user_id),
    INDEX idx_category_id (category_id),
    INDEX idx_type (type),
    INDEX idx_date (date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

## Tabela: audit_logs

Armazena o histórico de todas as operações (CREATE, UPDATE, DELETE) para auditoria.

```sql
CREATE TABLE audit_logs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    action VARCHAR(100) NOT NULL,
    entity_type VARCHAR(50) NOT NULL,
    entity_id INT NOT NULL,
    old_value LONGTEXT,
    new_value LONGTEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_action (action),
    INDEX idx_entity_type (entity_type),
    INDEX idx_timestamp (timestamp)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

## Índices para Performance

Os índices já estão incluídos nas definições das tabelas acima, mas aqui está um resumo:

```sql
-- Índices em users
ALTER TABLE users ADD INDEX idx_username (username);
ALTER TABLE users ADD INDEX idx_email (email);

-- Índices em categories
ALTER TABLE categories ADD INDEX idx_user_id (user_id);
ALTER TABLE categories ADD INDEX idx_type (type);

-- Índices em transactions
ALTER TABLE transactions ADD INDEX idx_user_id (user_id);
ALTER TABLE transactions ADD INDEX idx_category_id (category_id);
ALTER TABLE transactions ADD INDEX idx_type (type);
ALTER TABLE transactions ADD INDEX idx_date (date);

-- Índices em audit_logs
ALTER TABLE audit_logs ADD INDEX idx_user_id (user_id);
ALTER TABLE audit_logs ADD INDEX idx_action (action);
ALTER TABLE audit_logs ADD INDEX idx_entity_type (entity_type);
ALTER TABLE audit_logs ADD INDEX idx_timestamp (timestamp);
```

## Constraints e Validações

### Validações de Tipo

- **categories.type**: Deve ser 'entrada' ou 'saída'
- **transactions.type**: Deve ser 'entrada' ou 'saída'
- **transactions.value**: Deve ser maior que 0

### Chaves Estrangeiras

- **categories.user_id** → **users.id** (ON DELETE CASCADE)
- **transactions.user_id** → **users.id** (ON DELETE CASCADE)
- **transactions.category_id** → **categories.id** (ON DELETE RESTRICT)
- **audit_logs.user_id** → **users.id** (ON DELETE CASCADE)

## Queries Úteis

### Obter resumo financeiro de um usuário

```sql
SELECT 
    SUM(CASE WHEN type = 'entrada' THEN value ELSE 0 END) as total_entrada,
    SUM(CASE WHEN type = 'saída' THEN value ELSE 0 END) as total_saida,
    SUM(CASE WHEN type = 'entrada' THEN value ELSE -value END) as saldo
FROM transactions
WHERE user_id = 1;
```

### Listar lançamentos de um usuário com categoria

```sql
SELECT 
    t.id,
    t.date,
    c.name as categoria,
    t.description,
    t.type,
    t.value
FROM transactions t
JOIN categories c ON t.category_id = c.id
WHERE t.user_id = 1
ORDER BY t.date DESC;
```

### Filtrar lançamentos por tipo

```sql
SELECT * FROM transactions
WHERE user_id = 1 AND type = 'entrada'
ORDER BY date DESC;
```

### Filtrar lançamentos por categoria

```sql
SELECT * FROM transactions
WHERE user_id = 1 AND category_id = 5
ORDER BY date DESC;
```

### Obter histórico de auditoria

```sql
SELECT 
    a.id,
    a.action,
    a.entity_type,
    a.entity_id,
    a.old_value,
    a.new_value,
    a.timestamp
FROM audit_logs a
WHERE a.user_id = 1
ORDER BY a.timestamp DESC;
```

## Notas Importantes

1. **SQLite vs MySQL**: O script acima é para MySQL. Para SQLite, use:
   ```sql
   CREATE TABLE users (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       username TEXT UNIQUE NOT NULL,
       email TEXT UNIQUE NOT NULL,
       password TEXT NOT NULL,
       created_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
       updated_at DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL
   );
   ```

2. **Migrations**: Este projeto usa SQLAlchemy ORM, então as tabelas são criadas automaticamente ao iniciar a aplicação.

3. **Backup**: Sempre faça backup do banco de dados antes de executar operações destrutivas.

4. **Segurança**: Nunca exponha credenciais do banco de dados em código. Use variáveis de ambiente.

---

**Última atualização**: 14/04/2026
