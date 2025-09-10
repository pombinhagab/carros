# Sistema de Revenda de Carros 

Este projeto é um **sistema de revenda de carros** desenvolvido em **Python** utilizando o framework **Django** (padrão MVT – Model-View-Template) e **PostgreSQL** como banco de dados.  

O sistema permite o **gerenciamento completo de veículos**, desde a adição de novos carros ao catálogo até a exclusão de registros, passando pela visualização detalhada e atualização de informações.  

Uma funcionalidade inovadora é a **integração com Inteligência Artificial**, que gera automaticamente descrições para os carros quando estas não são fornecidas, otimizando o processo de cadastro e enriquecendo a apresentação dos veículos.  

---

## Tecnologias Utilizadas 

- **Python** – Linguagem de programação principal  
- **Django** – Framework web de alto nível para desenvolvimento rápido e seguro  
- **PostgreSQL** – Banco de dados relacional robusto  
- **Inteligência Artificial (IA)** – Integração para geração automática de descrições de veículos  
  - IA utilizada: **Mistral AI**  

---

## Funcionalidades Principais 

- **Adicionar Carro** – Cadastra novos veículos no sistema, incluindo marca, modelo, ano, preço e descrição (gerada automaticamente pela IA, caso não fornecida)  
- **Listar Carros** – Exibe uma lista completa dos veículos disponíveis no catálogo  
- **Ver Detalhes do Carro** – Permite visualizar informações detalhadas de um veículo específico  
- **Atualizar Carro** – Permite editar informações de veículos já cadastrados  
- **Deletar Carro** – Remove veículos do catálogo do sistema  
- **Integração com IA** – Geração automática de descrições para veículos sem descrição prévia  

---

## Configuração do Ambiente  

### Pré-requisitos  

Certifique-se de ter os seguintes softwares instalados:  
- **Python 3.x** (recomendado 3.9 ou superior)  
- **pip** (gerenciador de pacotes do Python)  
- **PostgreSQL** (servidor de banco de dados)  

### Clonar o Repositório  

```bash
git clone https://github.com/pombinhagab/carros.git
cd carros
```

### Criar Ambiente Virtual e Instalar Dependências  

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Configuração do Banco de Dados (PostgreSQL)  

```sql
CREATE DATABASE carros_db;
CREATE USER seu_usuario WITH PASSWORD 'sua_senha';
ALTER ROLE seu_usuario SET client_encoding TO 'utf8';
ALTER ROLE seu_usuario SET default_transaction_isolation TO 'read committed';
ALTER ROLE seu_usuario SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE carros_db TO seu_usuario;
```

### Variáveis de Ambiente  

Crie um arquivo `.env` na raiz do projeto (mesmo nível do `manage.py`) com:  

```env
SECRET_KEY=sua_chave_secreta_aqui
DEBUG=True
DATABASE_URL=postgres://seu_usuario:sua_senha@localhost:5432/carros_db
ALLOWED_HOSTS=127.0.0.1,localhost
```

Gere uma chave secreta com:  
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Aplicar Migrações  

```bash
python manage.py migrate
```

### Criar Superusuário  

```bash
python manage.py createsuperuser
```

### Iniciar o Servidor  

```bash
python manage.py runserver
```

Acesse o sistema em:  
👉 [http://127.0.0.1:8000/cars](http://127.0.0.1:8000/cars)
👉 [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## Status do Projeto  

- **Versão:** BETA  
- **Status:** Em desenvolvimento ativo 🚧  

---

## Licença  

Este projeto é de uso **educacional** e não possui fins comerciais.  
