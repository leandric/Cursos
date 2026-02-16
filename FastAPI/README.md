
# 📚 API de Livros (FastAPI + SQLModel)

API REST simples para cadastro e manutenção de livros, com paginação na listagem e persistência via SQLModel/SQLAlchemy.

---

## 🧱 Stack

- **FastAPI** (endpoints e documentação Swagger)
- **SQLModel** (modelagem + ORM)
- **SQLite** (comum em projetos de estudo; pode ser trocado por outro banco)
- **Uvicorn/FastAPI CLI** (servidor de desenvolvimento)

---

## ▶️ Como rodar o projeto

Ative seu ambiente virtual e rode:

```bash
fastapi dev api/main.py
````

A API ficará disponível em:

* API: `http://127.0.0.1:8000`
* Swagger (Docs): `http://127.0.0.1:8000/docs`
* OpenAPI JSON: `http://127.0.0.1:8000/openapi.json`

---

## 🗂️ Estrutura (visão geral)

* `api/main.py` → cria o app FastAPI e registra routers
* `api/routers/livros_routers.py` → endpoints de livros
* `api/models.py` → modelos (`Livro`, `LivroPost`, `LivroPut`, `LivroPatch`, `LivroResposta`, `ConfirmaDelete`)
* `api/database.py` → engine, sessão e dependência `get_session`

---

## 📌 Convenções do modelo Livro

Campos esperados para criação/atualização completa:

* `autor` (string)
* `titulo` (string)
* `editora` (string)
* `ano` (int)
* `uuid` (UUID) → gerado na criação (no `POST`)

> Observação: o `uuid` é usado como identificador nas rotas (`/livros/{livro_id}`).

---

# 🔌 Endpoints

Base path: **`/livros`**

Tag OpenAPI: **Livros**

---

## 1) Listar livros (com paginação)

### `GET /livros/`

Lista livros paginados. O tamanho da página é fixo em **10 itens**.

#### Query Params

* `page` (int, default=1, ge=1) → página solicitada

#### Response Headers

* `X-Total-Pages` → total de páginas
* `X-Total-Items` → total de itens no banco

#### Exemplo

```bash
curl -i "http://127.0.0.1:8000/livros/?page=1"
```

#### Resposta (200)

```json
[
  {
    "uuid": "8c7d7e38-2c61-4d44-9b91-6d2c1a52b0f3",
    "autor": "George Orwell",
    "titulo": "1984",
    "editora": "Companhia das Letras",
    "ano": 1949
  }
]
```

---

## 2) Buscar livro por UUID

### `GET /livros/{livro_id}`

Retorna um livro pelo `uuid`.

#### Path Params

* `livro_id` (UUID)

#### Exemplo

```bash
curl "http://127.0.0.1:8000/livros/8c7d7e38-2c61-4d44-9b91-6d2c1a52b0f3"
```

#### Respostas

* `200 OK` → livro encontrado
* `404 Not Found` → `{"detail":"Livro não encontrado"}`

---

## 3) Criar livro

### `POST /livros/`

Cria um novo livro. O `uuid` é gerado no servidor.

#### Body (LivroPost)

```json
{
  "autor": "George Orwell",
  "titulo": "1984",
  "editora": "Companhia das Letras",
  "ano": 1949
}
```

#### Exemplo

```bash
curl -X POST "http://127.0.0.1:8000/livros/" \
  -H "Content-Type: application/json" \
  -d '{"autor":"George Orwell","titulo":"1984","editora":"Companhia das Letras","ano":1949}'
```

#### Resposta (200)

```json
{
  "uuid": "8c7d7e38-2c61-4d44-9b91-6d2c1a52b0f3",
  "autor": "George Orwell",
  "titulo": "1984",
  "editora": "Companhia das Letras",
  "ano": 1949
}
```

---

## 4) Atualizar livro (substituição completa)

### `PUT /livros/{livro_id}`

Atualiza o livro de forma completa (espera todos os campos do `LivroPut`).

#### Body (LivroPut)

```json
{
  "autor": "George Orwell",
  "titulo": "1984 (edição revisada)",
  "editora": "Companhia das Letras",
  "ano": 1950
}
```

#### Exemplo

```bash
curl -X PUT "http://127.0.0.1:8000/livros/8c7d7e38-2c61-4d44-9b91-6d2c1a52b0f3" \
  -H "Content-Type: application/json" \
  -d '{"autor":"George Orwell","titulo":"1984 (edição revisada)","editora":"Companhia das Letras","ano":1950}'
```

#### Respostas

* `200 OK` → livro atualizado
* `404 Not Found` → `{"detail":"Livro não encontrado"}`

---

## 5) Atualizar livro (parcial)

### `PATCH /livros/{livro_id}`

Atualiza parcialmente um livro. Só os campos enviados são alterados.

#### Body (LivroPatch)

Você pode enviar qualquer subconjunto de campos:

```json
{
  "titulo": "Novo título"
}
```

#### Regras importantes

* Se nenhum dado for enviado (body vazio `{}` ou tudo `null`), retorna **400**:

  * `{"detail":"Nenhum dado recebido"}`

#### Exemplo

```bash
curl -X PATCH "http://127.0.0.1:8000/livros/8c7d7e38-2c61-4d44-9b91-6d2c1a52b0f3" \
  -H "Content-Type: application/json" \
  -d '{"titulo":"1984 (atualizado via PATCH)"}'
```

#### Respostas

* `200 OK` → livro atualizado
* `400 Bad Request` → `{"detail":"Nenhum dado recebido"}`
* `404 Not Found` → `{"detail":"Livro não encontrado"}`

---

## 6) Deletar livro

### `DELETE /livros/{livro_id}`

Remove um livro pelo UUID e retorna uma confirmação.

#### Exemplo

```bash
curl -X DELETE "http://127.0.0.1:8000/livros/8c7d7e38-2c61-4d44-9b91-6d2c1a52b0f3"
```

#### Resposta (200)

```json
{
  "mensagem": "Livro 1984 deletado.",
  "uuid": "8c7d7e38-2c61-4d44-9b91-6d2c1a52b0f3"
}
```

#### Resposta (404)

```json
{"detail":"Livro não encontrado"}
```

> ⚠️ **Observação importante (bug a corrigir):** no código atual, o decorator está como:
>
> ```py
> @router.delete("/{livros_id}", ...)
> async def deletar_livro(livro_id: UUID, ...)
> ```
>
> O path param está nomeado como `livros_id`, mas o argumento da função é `livro_id`.
> O correto é manter o mesmo nome em ambos:
>
> ```py
> @router.delete("/{livro_id}", ...)
> async def deletar_livro(livro_id: UUID, ...)
> ```

---

# 🧪 Testes rápidos

## Criar e listar

```bash
curl -X POST "http://127.0.0.1:8000/livros/" \
  -H "Content-Type: application/json" \
  -d '{"autor":"Teste","titulo":"Livro Teste","editora":"Editora X","ano":2024}'

curl -i "http://127.0.0.1:8000/livros/?page=1"
```

## Patch parcial

```bash
curl -X PATCH "http://127.0.0.1:8000/livros/<UUID>" \
  -H "Content-Type: application/json" \
  -d '{"ano":2025}'
```

---

# 📎 Códigos de erro comuns

* **400**: Nenhum dado enviado no PATCH
* **404**: Livro não encontrado para UUID informado
* **422**: Erro de validação (ex.: `ano` não é inteiro) ou JSON inválido
* **405**: Método não permitido (rota existe, mas não aceita aquele método)

---

# ✅ Próximos passos (opcionais)

* Permitir `page_size` como query param (`le=100`)
* Ordenação na listagem (`order_by`)
* Endpoint de upload CSV para carga em lote (`POST /livros/upload-csv`)
* Deduplicação (ex.: por `titulo+autor`) e mensagens de erro por linha no batch

---

