# Aplicacion para conectar gitlab y confluence.

Esta aplicación extrae el contenido de un archivo en un repositorio de GitLab, como por ejemplo el README.md, mediante la API de GitLab. Luego, convierte el contenido de HTML a Markdown y lo carga a través de la API de Confluence.

## Requerimientos:
- atlassian-python-api
- markdown2
- python-gitlab
- json

Modifica el archivo `config.json` con la infomacion requerida.

```json
[
    {
      "gitlab": {
        "url": "https://gitlab.com",
        "private_token": "TU-TOKEN"
      }
    },
    {
      "confluence": {
        "url": "https://USER.atlassian.net",
        "usernames": "TU-USURIO",
        "private_token": "TU-TOKEN"
      }
    }
  ]
```

### Referencias.

Doc-python-gitlab
[[https://python-gitlab.readthedocs.io/en/stable/]]

Doc-atlassian-python-api
[[https://atlassian-python-api.readthedocs.io/index.html]]

