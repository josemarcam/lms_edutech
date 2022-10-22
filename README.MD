# LMS Edutech

Python 3.9.0

## Pré-requisitos

    #Preencher .env
    preencha as váriaveis no .env.example e retire o .example do arquivo
    
    #Instalando dependencias
    pip install -r requirements.txt

    #Rodando migrations
    python manage.py migrate

    #Rodando o Projeto
    python manage.py runserver

# Rodando os testes

    #Teste DRF
    python manage.py test

    #coverage e relatório html
    coverage run manage.py test && coverage html # o caminho para o relatório é ./htmlcov/index.html

# Criando Primeiro Usuario

    #Entrar no shell django
    python manage.py shell

    #Importar a factory de users
    from modules.user.factories.user import UserFactory

    #Criar novo objeto de usuario (a senha padrao 'e '123qwe')
    user = UserFactory(username="admin", email='admin@admin.com', user_level=1, is_staff=1, is_superuser=1)

    #Salvar objeto no banco
    user.save()

    #Sair do shell
    exit() #ou Crt + d

