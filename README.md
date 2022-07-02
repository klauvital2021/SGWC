# SGWC

UNIVESP - Projeto Integrador II - Sistema de Gerenciamento de Cuidadores.

## Este projeto foi feito com:

* [Python 3.10.4](https://www.python.org/)
* [Django 4.0.5](https://www.djangoproject.com/)
* [Bootstrap 4.0](https://getbootstrap.com/)

## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/klauvital2021/SGWC.git
cd SGWC
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
python manage.py createsuperuser --username="admin" --email=""
```

## Diagramas ER

```
python manage.py graph_models -a -g -o img/models.png  # all
```

## Links

https://www.djangoproject.com/

https://ccbv.co.uk/

https://htmx.org/

