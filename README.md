# AutoMind Cursos: Hello World

Página web mínima que muestra `hello world` en rojo. El proyecto se sirve con
Nginx en el puerto 8080 y se puede ejecutar localmente con Docker Compose o
desplegar en Google Cloud Run con Cloud Build.

## Archivos

- `gpt-proxy/index.html`: página web.
- `gpt-proxy/Dockerfile` y `gpt-proxy/nginx.conf`: imagen y servidor web.
- `gpt-proxy/compose.yaml`: ejecución local.
- `gpt-proxy/cloudbuild.yaml`: construcción y despliegue en Cloud Run.

## Ejecución local

Desde la raíz de este proyecto:

```sh
docker compose -f gpt-proxy/compose.yaml up --build
```

Abrir http://localhost:8080. Para detenerlo, usar Ctrl+C.

## Despliegue en Cloud Run

El YAML usa la región `us-central1`, el servicio `automind-cursos` y el
repositorio de Artifact Registry `cloud-run-source-deploy`. Antes del primer
despliegue, habilita Cloud Build, Cloud Run y Artifact Registry, crea ese
repositorio Docker en la región indicada y concede a la cuenta de servicio de
Cloud Build permisos para publicar imágenes y desplegar Cloud Run.

Desde la raíz del proyecto:

```sh
gcloud builds submit --config gpt-proxy/cloudbuild.yaml .
```

Si tu proyecto usa otra región, nombre de servicio o repositorio, cambia las
substituciones `_REGION`, `_SERVICE` y `_REPO` del YAML antes de desplegar.

El repositorio conserva la ubicación `gpt-proxy/cloudbuild.yaml` para que un
trigger que ya apunte a esa ruta pueda seguir usándola.
