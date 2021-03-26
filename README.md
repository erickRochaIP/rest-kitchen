#rest-kitchen
Como usar essa incrível API Rest

**Listar receitas**
----
Retorna uma lista json com as receitas buscadas.
* **URL**

    /receitas/
* **Método:**

    `GET`
* **Parâmetros**

  **Requeridos:**
  
    Nenhum

  **Opcionais:**

    `id_chef=[integer]`

* **Resposta de Sucesso:**

    * **Código:** 200
    * **Conteúdo:** 
      ```
      [
      {"id":1,"nome":"Pão com ovo","descricao":"Delicioso pão com um ovo de brinde","id_chef":0},
      {"id":2,"nome":"Pão sem ovo","descricao":"Delicioso pão, porém sem um ovo de brinde","id_chef":0}
      ]
      ```


```shell
# Vendo todas as receitas
$ curl http://127.0.0.1:8000/receitas/

# Vendo todas as receitas do chef '4'
$ curl http://127.0.0.1:8000/receitas/?id_chef=4

# Adicionando receita do chef '4'
$ curl -d "nome=nome da receita&descricao=descricao da receita&id_chef=4" -X POST http://127.0.0.1:8000/receitas/

# Editando receita com id '4'
$ curl -d "nome=novo nome&descricao=nova descricao" -X PUT http://127.0.0.1:8000/receitas/4/

# Editando campo específico de receita com id '4'
$ curl -d "nome=novo nome" -X PATCH http://127.0.0.1:8000/receitas/4/

# Excluindo receita com id '4'
$ curl -X DELETE http://127.0.0.1:8000/receitas/4/
```