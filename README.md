# rest-kitchen

API Rest para receitas :cake:

## Preparando o ambiente
Antes de começar, tenha certeza de que tem instalado: [Python](https://www.python.org/), [Git](https://git-scm.com/)
```shell
# Clone o repositorio
$ git clone https://github.com/erickRochaIP/rest-kitchen.git

# Acesse o diretorio
$ cd rest-kitchen

# Instale as dependencias
$ pip install -r requirements.txt

# Acesse o aplicativo
$ cd restkitchen

# Rode os testes
$ python manage.py test

# Rode o servidor
$ python manage.py runserver
```
## Documentação

**Receitas**
----
Receitas possuem id, nome, descrição e id_chef. A API permite você criar, deletar, editar e pesquisar receitas.
* **URLs**

    Base: http://127.0.0.1:8000/
    
    [GET /receitas/](#listar-receitas)
  
    [POST /receitas/](#criar-receita)
  
    [GET /receitas/:id](#mostrar-receita)
  
    [PUT /receitas/:id](#atualizar-receita)
  
    [PATCH /receitas/:id](#atualizar-parcialmente-receita)
  
    [DELETE /receitas/:id](#deletar-receita)
    
  
**Listar receitas**
----
Retorna lista json com as receitas que se encaixam nos filtros de pesquisa.
* **Parâmetros:**

  **Requeridos:**
  
    Nenhum

  **Opcionais:**

    `id_chef=[integer]`

* **Resposta:**

    * **Código:** 200
    * **Conteúdo:** 
      ```
      [
      {"id":1,"nome":"Pão com ovo","descricao":"Delicioso pão com um ovo de brinde","id_chef":0},
      {"id":2,"nome":"Pão sem ovo","descricao":"Delicioso pão, porém sem um ovo de brinde","id_chef":4}
      ]
      ```
      
* **Exemplo de uso:**

  ```shell
  # Vendo todas as receitas
  $ curl http://127.0.0.1:8000/receitas/ 
  
  # Vendo todas as receitas do chef '4'
  $ curl http://127.0.0.1:8000/receitas/?id_chef=4 
  ```

**Criar receita**
----
Cria uma nova receita com nome, descrição e id_chef informados. Caso não seja informado, id_chef = 0.

* **Parâmetros:**

  **Requeridos:**

    `nome=[string]`
  
    `descricao=[string]`

  **Opcionais:**

    `id_chef=[integer]`

* **Resposta:**
  * **Código:** 200
  * **Conteúdo:**
  ```
  {"id":9,"nome":"nome da receita","descricao":"descricao da receita","id_chef":4}
  ```
* **Exemplo de uso:**
  ```shell
  # Criando nova receita
  $ curl -d "nome=nome da receita&descricao=descricao da receita&id_chef=4" -X POST http://127.0.0.1:8000/receitas/ 
  ```

**Mostrar receita**
----
Retorna json da receita com o id pesquisado
* **Parâmetros:**
  
  Nenhum

* **Resposta:**

  * **Código:** 200
  * **Conteúdo:**
  ```
  {"id":9,"nome":"nome da receita","descricao":"descricao da receita","id_chef":4}
  ```
* **Resposta de erro:**
  
  * **Código:** 404
  * **Conteúdo:**
  ```
  {"detail":"Not found."}
  ```
  
* **Exemplo de uso:**
  ```shell
  # Vendo a receita com id '9'
  $ curl http://127.0.0.1:8000/receitas/9/
  ```
  
**Atualizar receita**
----
Atualiza todos os valores da receita com o id informado.
Caso não seja informado, id_chef permanece o mesmo.
* **Parâmetros:**

  **Requeridos:**
    
    `nome=[string]`
    
    `descricao=[string]`

  **Opcionais:**

    `id_chef=[integer]`

* **Resposta:**

  * **Código:** 200
  * **Conteúdo:**
  ```
  {"id":9,"nome":"Bolinho","descricao":"Pequeno bolo","id_chef":1} 
  ```
  
* **Resposta de erro:**

  * **Código:** 400
  * **Conteúdo:**
  ```
  {"nome":["This field is required."],"descricao":["This field is required."]}
  ```
  
  OU

  * **Código:** 404
  * **Conteúdo:**
  ```
  {"detail":"Not found."}
  ```

* **Exemplo de uso:**

  ```shell
  # Editando receita com id '9'
  $ curl -d "nome=Bolinho&descricao=Pequeno bolo&id_chef=1" -X PUT http://127.0.0.1:8000/receitas/9/ 
  ```
**Atualizar parcialmente receita**
----

Atualiza alguns dos valores da receita com o id informado.
* **Parâmetros:**

  **Requeridos:**
    
    Nenhum

  **Opcionais:**

  `nome=[string]`

  `descricao=[string]`

  `id_chef=[integer]`

* **Resposta:**

  * **Código:** 200
  * **Conteúdo:**
  ```
  {"id":9,"nome":"Bolinho","descricao":"Pequeno novo bolo","id_chef":1} 
  ```

* **Resposta de erro:**

  * **Código:** 404
  * **Conteúdo:**
  ```
  {"detail":"Not found."}
  ```

* **Exemplo de uso:**

  ```shell
  # Editando parcialmente receita com id '9'
  $ curl -d "descricao=Pequeno novo bolo" -X PATCH http://127.0.0.1:8000/receitas/9/ 
  ```

**Deletar receita**
----
Deleta a receita com o id informado.
* **Parâmetros:**
  
  Nenhum

* **Resposta:**
  * **Código:** 204

* **Resposta de erro:**

  * **Código:** 404
  * **Conteúdo:**
  ```
  {"detail":"Not found."}
  ```
  
* **Exemplo de uso:**

  ```shell
  # Excluindo receita com id '9'
  $ curl -X DELETE http://127.0.0.1:8000/receitas/9/ 
  ```