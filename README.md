# Point Stonks

### Requisitos da aplicação

Você deve ter <code> Python 3.8</code>, <code> Pip 20.2</code> e <code>Postgres 20</code> instalado em sua máquina.

### Instalação e Execução

#### 1. Clone o repositório

```
$ git clone https://github.com/ExpertProIHC/point-stonks.git
```

#### 2. Acesse a pasta do repositório

```
$ cd point-stonks
```

#### 3. Crie uma ambiente virtual para a aplicação: 

```
$ virtualenv venv
```

#### 4. Ative o ambiente virtual: 

```
$ source venv/bin/activate
```

#### 5. Depois de criar e ativar um ambiente virtual, execute o comando abaixo para instalar todas as bibliotecas Python listadas em requirements.txt:

```
$ pip install -r requirements.txt
```

#### 6. Copie o arquivo dev.env para um novo arquivo chamado .env

```
$ cp dot.env .env
```

#### 7. Em seguida, execute os comandos para criar as tabelas no banco de dados:

```
$ python manage.py makemigrations
```
```
$ python manage.py migrate
```


#### 7. Execute o servidor:

```
$ python manage.py runserver
```
