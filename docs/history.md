catalunha@pop-os:~/apps/celery_rabbitmq_1$ pyenv versions
  system
  3.11.0
* 3.12.0 (set by /home/catalunha/.pyenv/version)
  3.12.2
catalunha@pop-os:~/apps/celery_rabbitmq_1$ pyenv local 3.12.0
catalunha@pop-os:~/apps/celery_rabbitmq_1$ poetry init

This command will guide you through creating your pyproject.toml config.

Package name [celery_rabbitmq_1]:  
Version [0.1.0]:  
Description []:  
Author [catalunha <catalunha.mj@gmail.com>, n to skip]:  
License []:  
Compatible Python versions [^3.11]:  3.12

Would you like to define your main dependencies interactively? (yes/no) [yes] no
Would you like to define your development dependencies interactively? (yes/no) [yes] no
Generated file

[tool.poetry]
name = "celery-rabbitmq-1"
version = "0.1.0"
description = ""
authors = ["catalunha <catalunha.mj@gmail.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "3.12"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"


Do you confirm generation? (yes/no) [yes] 
catalunha@pop-os:~/apps/celery_rabbitmq_1$ poetry config --list
cache-dir = "/home/catalunha/.cache/pypoetry"
experimental.system-git-client = false
installer.max-workers = null
installer.modern-installation = true
installer.no-binary = null
installer.parallel = true
keyring.enabled = true
solver.lazy-wheel = true
virtualenvs.create = true
virtualenvs.in-project = true
virtualenvs.options.always-copy = false
virtualenvs.options.no-pip = false
virtualenvs.options.no-setuptools = false
virtualenvs.options.system-site-packages = false
virtualenvs.path = "{cache-dir}/virtualenvs"  # /home/catalunha/.cache/pypoetry/virtualenvs
virtualenvs.prefer-active-python = false
virtualenvs.prompt = "{project_name}-py{python_version}"
warnings.export = true
catalunha@pop-os:~/apps/celery_rabbitmq_1$ poetry add celery
The currently activated Python version 3.11.0 is not supported by the project (3.12).
Trying to find and use a compatible version. 
Using python3 (3.12.0)
Creating virtualenv celery-rabbitmq-1 in /home/catalunha/apps/celery_rabbitmq_1/.venv
Using version ^5.4.0 for celery

Updating dependencies
Resolving dependencies... (2.1s)

Package operations: 14 installs, 0 updates, 0 removals

  - Installing vine (5.1.0)
  - Installing wcwidth (0.2.13)
  - Installing amqp (5.2.0)
  - Installing click (8.1.7)
  - Installing prompt-toolkit (3.0.47)
  - Installing six (1.16.0)
  - Installing billiard (4.2.0)
  - Installing click-didyoumean (0.3.1)
  - Installing click-plugins (1.1.1)
  - Installing click-repl (0.3.0)
  - Installing kombu (5.4.0)
  - Installing python-dateutil (2.9.0.post0)
  - Installing tzdata (2024.1)
  - Installing celery (5.4.0)

Writing lock file
catalunha@pop-os:~/apps/celery_rabbitmq_1$ 

Subir docker do rabbitmq

# latest RabbitMQ 3.13
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13-management

executando o celery
catalunha@pop-os:~/apps/celery_rabbitmq_1/app$ poetry run celery -A tasks worker --loglevel=INFO

basta gerar o producer com 
python app.py
que o celery captará a mensagem e vai executar
