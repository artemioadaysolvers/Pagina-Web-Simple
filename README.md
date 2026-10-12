Tutorial sencillo para publicar una página web desde GitHub en Microsoft Azure,
para el Curso de Taller de Innovación y Emprendimiento Tecnológico 2026,
segundo semestre, de la Universidad Adolfo Ibáñez.

Hecho por el Ayudante Instructor Artemio Araya Day con ayuda de Codex.
Profesor del Curso: Martín Céspedes Escuti.

# Página de suma con backend Python 3.14.8

La página muestra `hello world` en rojo y suma dos números mediante
`POST /api/sumar`. Python sirve tanto el HTML como la API, usando Waitress.
`GET /health` devuelve `{"estado": "ok"}`. La página conserva su diseño original.

La versión solicitada es **exactamente Python 3.14.8**, publicada el
30 de septiembre de 2026: [descarga oficial](https://www.python.org/downloads/release/python-3148/).
`.python-version`, Docker y las pruebas de GitHub usan esa versión.
El servidor comprueba la versión al arrancar para evitar ejecutar otra por accidente.

## Ejecutar con Docker

Desde esta carpeta, con Docker instalado:

```sh
docker compose up --build
```

Abre http://localhost:8080. El contenedor instala Python 3.14.8 y Waitress;
no necesitas instalar Python en tu equipo. Detén el servidor con Ctrl+C.

## Ejecutar con Python en Windows

Instala Python 3.14.8 desde la página oficial. Después, abre una terminal
en esta carpeta y ejecuta:

```powershell
py -3.14 --version
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe server.py
```

El primer comando debe mostrar `Python 3.14.8`. Si muestra otra revisión,
actualiza Python antes de crear el entorno. Abre http://localhost:8080.
No hace falta activar el entorno virtual ni cambiar la política de PowerShell.

En Linux/macOS, con Python 3.14.8 instalado:

```sh
python3.14 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python server.py
```

El puerto predeterminado es `8080`; puedes cambiarlo con la variable `PORT`.

## Pruebas

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

En Linux/macOS usa `.venv/bin/python` en lugar de la ruta de Windows.
Las pruebas comprueban la página, salud, sumas, decimales, validación,
JSON inválido, desbordamientos, tamaño de solicitudes y rutas desconocidas.

## Desplegar en Azure desde GitHub

Para controlar la revisión exacta de Python, el workflow utiliza el contenedor
`python:3.14.8-slim`. El runtime administrado de App Service se selecciona por
serie (por ejemplo, `PYTHON|3.14`), por lo que no fija por sí solo la revisión 3.14.8.
Consulta la [configuración oficial de Python](https://learn.microsoft.com/en-us/azure/app-service/configure-language-python)
y el [tutorial de contenedores de App Service](https://learn.microsoft.com/en-us/azure/app-service/tutorial-custom-container).

Esta opción requiere una **Web App de Linux configurada para contenedores**
y un **Azure Container Registry (ACR)**. Revisa el costo y la compatibilidad del
plan: la configuración anterior de publicación de código con Node.js no basta.

Antes del primer despliegue:

1. Prepara la Web App `paginacalculadora` y un ACR. Si el nombre de la Web App
   cambia, actualiza `AZURE_WEBAPP_NAME` en el workflow.
2. Activa la identidad administrada asignada por el sistema de la Web App.
   Concédele el rol `AcrPull` sobre un ACR que use el modelo de permisos RBAC
   tradicional. El workflow configura la descarga mediante esa identidad.
3. Conserva la conexión OIDC y los tres secretos `AZUREAPPSERVICE_CLIENTID_…`,
   `AZUREAPPSERVICE_TENANTID_…` y `AZUREAPPSERVICE_SUBSCRIPTIONID_…` que ya usaba
   el workflow original. La identidad de despliegue debe tener permisos para
   actualizar la Web App y ejecutar construcciones de ACR (por ejemplo,
   Contributor, limitado a los recursos necesarios).
4. En GitHub, en **Settings → Secrets and variables → Actions → Variables**, crea:
   - `AZURE_RESOURCE_GROUP`: grupo de recursos de la Web App.
   - `AZURE_CONTAINER_REGISTRY`: nombre del ACR, sin `.azurecr.io`.
5. Sube los archivos de esta carpeta a la raíz del repositorio, incluyendo
   `.github`. Elimina del repositorio los antiguos `server.js` y `package.json`,
   y reemplaza el workflow original; no mantengas ambos servidores activos.

El workflow `.github/workflows/main_paginacalculadora.yml` prueba el backend
en cada push o pull request a `main`. En un push o ejecución manual, construye
y despliega el contenedor si las dos variables de Azure están configuradas.
Si faltan, ejecuta las pruebas y omite el despliegue. Ajusta la rama si no usas `main`.
La preparación de infraestructura y los permisos se realizan una vez en Azure;
este ZIP no crea ni modifica recursos de tu cuenta por sí solo.

## Google Cloud Run

`cloudbuild.yaml` conserva la alternativa de Cloud Run y utiliza el mismo
Dockerfile con Python 3.14.8. Requiere el proyecto, Artifact Registry y permisos
de Cloud Build/Cloud Run configurados previamente. Ajusta sus sustituciones
de región, servicio y repositorio según tu proyecto.

## Archivos principales

- `server.py`: servidor Python y API.
- `index.html`: página original.
- `requirements.txt`: dependencia Waitress fijada a la versión 3.0.2.
- `.python-version`: versión exacta de Python.
- `Dockerfile` y `compose.yaml`: ejecución en contenedor.
- `.github/workflows/main_paginacalculadora.yml`: pruebas y despliegue de Azure.
- `tests/test_server.py`: pruebas HTTP del backend.
