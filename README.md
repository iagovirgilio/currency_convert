
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
    
## Melhorias

1 - Criar um usuário específico para rodar a aplicação. Até o momento o damemon do docker está usando o usuário root o que não é uma prática recomendada a nível de segurança.

2 - Controle de acesso por usuário para enviar o csrf_token para validar o consumo do endpoint ou outro tipo de validação via token.

3 - Limitação da API de cotação: Inicialmente usei a biblioteca forex-python, pois já tem uma função para converter moedas, mas me deparei com a limitação da versão do python. jJá que estava na versão 3.12 o que não é compatível com a biblioteca. Então decidi usar uma API de terceiros, pois foi menos custoso do que refazer todo o projeto usando outra versão do Python. 

No primeiro momento escolhi a API exchangerate v4, mas tem a limitação de não ter cotação para criptomoedas. Troquei para coingecko, que funcionou muito bem, mas tem limitação de requisição por ser uma API paga.

## Observações

O arquivo .env está no repositório para cumprir o requisito pedido no teste de apenas dar o comando para subir a aplicação e funcionar. Em projetos não coloco o .env no repositório, apenas o .env-example.
