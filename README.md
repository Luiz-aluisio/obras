# obras

aplicação para gerenciar autor e obras desenvolvidas em [python](https://python.org.br/) e [django](https://www.djangoproject.com/)

Para contribuir ou utilizar este projeto você deve ter o [poetry](https://python-poetry.org/) instalado.

## Execução da Aplicação

comando para instalar dependencias de utilização da aplicação

    poetry intall

Ative o ambiente virtual com o seguinte comando.

    poetry shell

Para eecutar a apliacação preciasamos fazer as migrações.

    task db-migrate

Comando para executar a aplicação

    task run

## Contribuir com o projeto

 comando para intalar dependencias de desenvolvimento

    poetry install --with dev

**Com o ambiente virtual ativado**

Comando para verificar o projeto está no padrão da [PEP8](https://peps.python.org/pep-0008/)

    task lint

Formantando código na [PEP8](https://peps.python.org/pep-0008/)

    task fomat

Executando os testes

    task test

