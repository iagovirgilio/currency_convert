
# Currency Convert

Desafio técnico  backend Python/Django da Data Stone. Criar uma API para conversão monetária contendo as seguintes moedas: USD, BRL, EUR, BTC e ETH.


## Instalação

```bash
  git clone https://github.com/iagovirgilio/currency_convert.git
  cd currency_convert
  docker-compose up --build
```


Execute o código com:
```bash
  docker-compose up
```

Acesse o sistema pela porta 8000:
http://127.0.0.1:8000

## Testes

Acesso ao terminal da aplicação:
```bash
  docker exec -it app sh
```

Comando para executar os testes:
```bash
  python manage.py test
```

## Criar super usuário para acessar o painel admin:

Acesso ao terminal da aplicação:
```bash
  docker exec -it app sh
```

Comando para criar usuário:
```bash
  python manage.py createsuperuser
```

## Melhorias

1 - Preparar a imagem do Docker para criar um usuário específico, no linux, para rodar a aplicação. Até o momento o damemon do docker está usando o usuário root o que não é uma prática recomendada a nível de segurança.

2 - Controle de acesso por usuário para enviar o csrf_token para validar o consumo do endpoint -- Isso depende de criar autenticação de usuário -- ou outro tipo de validação via token.

3 - Limitação da API de cotação: No primeiro momento escolhi a API exchangerate v4, mas tem a limitação de não ter cotação para criptomoedas. Troquei para coingecko, que funcionou muito bem, mas tem limitação de requisição por ser uma API paga.

4 - Criar tela específica par cadastrar moedas. Até o momento só pode adicionar moedas pelo painel do Admin.

## Observações

1 - O arquivo .env está no repositório para cumprir o requisito pedido no teste de apenas dar o comando para subir a aplicação e funcionar. Num projeto não coloco o .env no repositório, apenas o .env-example.

2 - Inicialmente usei a biblioteca forex-python, pois já tem uma função para converter moedas, mas me deparei com a limitação da versão do python. Já que estava na versão 3.12 o que não é compatível com a biblioteca. Então decidi usar uma API de terceiros, pois foi menos custoso do que refazer todo o projeto usando outra versão do Python.
