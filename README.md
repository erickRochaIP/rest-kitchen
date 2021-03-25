# rest-kitchen
API Rest usando Django

```shell
# Vendo todas as receitas
$ curl http://127.0.0.1:8000/receitas/

# Adicionando receita
$ curl -d "nome='nomedareceita'&descricao='descricaodareceita'" -X POST http://127.0.0.1:8000/receitas/
```