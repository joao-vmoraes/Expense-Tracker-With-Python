    # Administrador Financeiro (Expense Tracker)

Um sistema simples de gerenciamento de finanças pessoais (rastreador de despesas) desenvolvido em **Python** utilizando o terminal. Este foi o meu primeiro projeto aplicando os conceitos de **Programação Orientada a Objetos (POO)** e a arquitetura **MVC (Model-View-Controller)** para manter o código limpo, organizado e escalável.

## 🚀 Funcionalidades

O sistema apresenta um menu interativo no terminal que permite:
* **Adicionar Compra:** Registra um novo gasto associado a uma categoria específica.
* **Remover Compra:** Exclui um gasto existente através do seu ID.
* **Atualizar Compra:** Modifica o valor, nome ou categoria de um registro.
* **Listar Compras:** Exibe todos os gastos registrados.
* **Filtrar por Data:** Lista compras filtrando pelo mês e ano.
* **Totais por Categoria:** Exibe o valor total gasto agrupado por cada categoria.

## 🛠️ Tecnologias e Arquitetura

* **Linguagem:** Python 3
* **Banco de Dados:** MySQL
* **Arquitetura:** MVC (Model, View, Controller)
* **Bibliotecas Principais:** * `pymysql` (Comunicação com o banco de dados)
  * `python-dotenv` (Gerenciamento de variáveis de ambiente)

## 📋 Como Executar o Projeto

### 1. Pré-requisitos
Certifique-se de ter o Python e o MySQL instalados na sua máquina (ou utilize o Docker, se preferir usar o arquivo `docker-compose.yml` incluso).

### 2. Configuração do Banco de Dados
1. Crie um banco de dados no MySQL.
2. Execute o script SQL localizado em `app/database/_init_db.sql` para criar as tabelas necessárias (`categorias` e `compras`) e inserir as categorias iniciais.

### 3. Configuração do Ambiente
1. Clone este repositório.
2. Crie um arquivo `.env` na raiz do projeto com base no arquivo `.env-example` e preencha com as credenciais do seu banco de dados:
   ```env
   MYSQL_HOST=localhost
   MYSQL_USER=seu_usuario
   MYSQL_PASSWORD=sua_senha
   MYSQL_DATABASE=nome_do_banco