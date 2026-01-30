TaskLink API 🚀
Plataforma de organização de estudos solo e em grupo, desenvolvida com Django, PostgreSQL e Docker.

🛠️ Tecnologias
Framework: Django REST Framework

Banco de Dados: PostgreSQL 15

Containerização: Docker & Docker Compose

Autenticação: JWT (JSON Web Token)

🚀 Como Rodar o Projeto
Clone o repositório:
git clone https://github.com/SEU_USUARIO/api_tasklink.git
cd api_tasklink

Suba os containers:
docker-compose up -d

Aplique as migrações e crie seu usuário:
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

🗄️ Conexão com o pgAdmin

Host: localhost

Port: 5432

Database: db_tasklink

Username: admin_tasklink

Password: tasklinksenha

📌 Tabelas Principais

usuarios: Perfis e Gamificação (XP/Nível).

tarefas: Gestão de afazeres individuais.

grupos_estudo: Gestão de grupos colaborativos.

membros_grupos: Vínculo entre usuários e grupos.

## 👥 Equipe
* **Danilo Diniz** - [(https://github.com/dinizdanilo)]
* **Eythor do Nascimento** - [(https://github.com/EythordoNascimento)]
* **Kauã Ambrosio** - []