# API MATERIAL SEARCH
- API feita para gerenciamento de usuarios e posts da rede social only reads
- Aplicação feita em FastAPI + SQLAlchemy


# Como rodar?

1 - Criar diretorio de biblioteca
``` bash
  python -m venv ./venv
```

2 - Ativar seu ambiente

Windows
``` bash
./venv/Script/activate
```

Linux
``` bash
source ./venv/Script/ativate
```

3 - Instalar dependencias
``` bash
pip install -r requirements.txt
```

4 - Criar variaveis de ambiente
- No diretorio principal, crie o arquivo .env e insira as variaveis necessarias, DATABASE_URL="Url do banco, se for só pra teste: 'sqlite:///database.db'", SECRET_KEY="chave de criptografia de token, qualquer string...", ALGORITHM="Algoritmo jwt, pode ser HS256", ACCESS_TOKEN_EXPIRE_MINUTES="tempo de expiração de token em minutos"

5 - Rodar o projeto dentro do app
``` bash
cd ./app && fastapi dev main.py
```

