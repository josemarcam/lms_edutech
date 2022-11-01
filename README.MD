# LMS Edutech

Python 3.9.0

## Pré-requisitos

```
#Preencher .env
preencha as váriaveis no .env.example e retire o .example do arquivo

#Crie o Virtual Enviroment
python -m venv venv
```

Ative o Virtual Enviroment:
* Windows
    ```sh
    ./venv/Scripts/activate.bat
    ```
* Unix
    ```sh
    source venv/bin/activate
    ```
    
```
#Instale as dependencias
pip install -r requirements.txt

#Rode migrations
python manage.py migrate

#Rode o Projeto
python manage.py runserver # certifique-se de ter criado o seu primeiro usuario
```
    
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

# Rodando os testes

    #Teste DRF
    python manage.py test

    #coverage e relatório html
    coverage run manage.py test && coverage html # o caminho para o relatório é ./htmlcov/index.html