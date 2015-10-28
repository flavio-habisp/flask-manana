#flask-manana
e-Commerce platform based on Flask (python microframework) and Mongo database.

##Installation

######Download the repository
```bash
    git clone https://github.com/kvs1904/flask-manana.git
    cd flask-manana
```

######Install OS external packages (by default for Ubuntu Linux)
```bash
    make install_soft
```

######Create python3.x virtual environment
```bash
    make env_create
```

######Activate it
```bash
   source .venv/bin/activate
```

######Install python packages
```bash
    make install_eggs
```

######Run the tests
```bash
    py.test .
```
