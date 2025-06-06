# Consultório de Psicologia

Este projeto é um sistema web desenvolvido em Django para gerenciar pacientes e consultas em um consultório de psicologia, utilizando MySQL como banco de dados e interface moderna com Bootstrap 5. - Criado totalmente utilizando GitHub Copilot Pro

## Funcionalidades

- Cadastro e listagem de pacientes
- Registro e agendamento de consultas
- Validação de agendamento: não permite duas consultas para o mesmo paciente no mesmo dia e exige intervalo de 60 minutos entre consultas
- Validação de telefone: formato obrigatório +55 11 9 12345678
- Relatório de consultas realizadas no mês
- Interface administrativa via Django Admin
- Visual profissional com Bootstrap 5

## Pré-requisitos

- Python 3.10+
- MySQL instalado e rodando
- Banco de dados `consultorio_db` criado no MySQL

## Como rodar o projeto

1. Configure o arquivo `.env` com a senha do banco MySQL:

   ```env
   PASSWORD=sua_senha
   ```

2. Certifique-se de que o banco `consultorio_db` existe no MySQL.
3. Ative o ambiente virtual:
   - No PowerShell: `.venv\Scripts\Activate.ps1`

4. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

5. Aplique as migrações:

   ```bash
   python manage.py migrate
   ```

6. Crie um superusuário:

   ```bash
   python manage.py createsuperuser
   ```

7. Rode o servidor:

   ```bash
   python manage.py runserver
   ```

## Acesso rápido

- [Admin](http://localhost:8000/admin/)
- [Pacientes](http://localhost:8000/pacientes/)
- [Novo Paciente](http://localhost:8000/pacientes/novo/)
- [Consultas Agendadas](http://localhost:8000/consultas/)
- [Agendar Consulta](http://localhost:8000/consultas/novo/)
- [Relatório de Consultas do Mês](http://localhost:8000/consultas/relatorio/)

## Observações

- O telefone deve ser cadastrado no formato: `+55 11 9 12345678`
- O sistema utiliza Bootstrap 5 para um visual moderno e responsivo.
- Caso não tenha o MySQL, instale e crie o banco com:

  ```sql
  CREATE DATABASE consultorio_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
  ```
