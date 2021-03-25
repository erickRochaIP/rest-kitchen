# rest-kitchen
API Rest usando Django

```shell
# Vendo todas as receitas
$ curl http://127.0.0.1:8000/receitas/

# Adicionando receita
$ curl -d "nome=nome da receita&descricao=descricao da receita" -X POST http://127.0.0.1:8000/receitas/

# Editando receita com id '4'
$ curl -d "nome=novo nome&descricao=nova descricao" -X PUT http://127.0.0.1:8000/receitas/4/

# Excluindo receita com id '4'
$ curl -X DELETE http://127.0.0.1:8000/receitas/4/
```