Tutorial sencillo para publicar una página web utilizando GitHub y Microsoft Azure en el curso Taller de Innovación y Emprendimiento Tecnológico 2026 (segundo semestre), Universidad Adolfo Ibáñez.

Hecho por el Ayudante Instructor Artemio Araya Day con ayuda de Codex.  
Profesor del curso: Martín Céspedes Escuti.

# Página de suma con backend Python 3.14.8

Esta aplicación muestra **hello world** en rojo y permite ingresar dos números. Al pulsar **Sumar**, el navegador envía un `POST /api/sumar` al backend, que calcula la suma y devuelve JSON. El frontend es `index.html` (HTML, CSS y JavaScript); el backend es `server.py` (**Python 3.14.8**). Ambos están en el mismo servidor, por lo que no hace falta CORS.

**No necesita Flask, FastAPI, Node.js ni paquetes de terceros.** Todo se implementa con módulos incluidos en Python.

## Ejecutar localmente

1. Instala [Python 3.14.8](https://www.python.org/downloads/release/python-3148/).
2. Abre una terminal en la carpeta del proyecto.
3. Inicia el servidor:

```powershell
# Windows, si se instaló la versión 3.14 mediante el lanzador py:
py -3.14 server.py
```

En Linux o macOS, si `python3` es la versión 3.14.8:

```sh
python3 server.py
```

Abre **http://localhost:8080**. Para comprobar qué versión tienes instalada ejecuta `py -3.14 --version` (Windows) o `python3 --version` (Linux/macOS).

Por defecto se usa el puerto 8080. También puedes indicar otro con la variable de entorno `PORT`. La versión deseada queda indicada en `.python-version` para las herramientas que la respetan.

## Ejecutar pruebas

```sh
python -m unittest discover -v
```

En Windows, también sirve `py -3.14 -m unittest discover -v`.

## Ejecutar con Docker (Python 3.14.8 exacto)

```sh
docker compose up --build
```

Abre **http://localhost:8080**. El `Dockerfile` fija explícitamente la imagen `python:3.14.8-slim` para garantizar esa versión de Python dentro del contenedor. No hace falta instalar Python en el equipo anfitrión si usas Docker.

## Rutas

| Método | Ruta | Resultado |
|---|---|---|
| GET | `/` | Devuelve `index.html` |
| GET | `/health` | `{"estado":"ok"}` |
| POST | `/api/sumar` | Recibe `{"a":2,"b":3}` y devuelve `{"suma":5}` |

Los datos deben contener dos números finitos. Las peticiones inválidas reciben un error JSON, y el cuerpo de entrada tiene límite de 1024 bytes.

## Publicar en Azure App Service desde GitHub

El workflow `.github/workflows/main_paginacalculadora.yml` ejecuta las pruebas usando **Python 3.14.8** y mantiene el despliegue con el nombre de Web App `paginacalculadora` y los secretos de autenticación OIDC existentes.

**IMPORTANTE: la Web App anterior utilizaba Node.js.** Antes de desplegar este proyecto, cambia su runtime a **Python 3.14 en Linux** y establece el **Comando de inicio** (Startup Command) a:

```sh
PORT=8000 python server.py
```

Este comando fija el puerto 8000 que utiliza habitualmente el runtime Python administrado de Azure.

En Azure Portal: Web App → Configuración → Configuración general → versión de Python (3.14) y comando de inicio. También se puede usar Azure CLI (sustituye `MI_GRUPO` por el grupo de recursos real):

```sh
az webapp config set --resource-group MI_GRUPO --name paginacalculadora --linux-fx-version 'PYTHON|3.14'
az webapp config set --resource-group MI_GRUPO --name paginacalculadora --startup-file 'PORT=8000 python server.py'
```

Si no aparece Python 3.14 entre los runtimes compatibles con el plan o plataforma de tu Web App, despliega usando una **imagen Docker personalizada**. El runtime administrado por Azure selecciona la versión de mantenimiento de Python 3.14, por lo que **no garantiza específicamente el parche 3.14.8**; para fijarlo exactamente utiliza el Dockerfile suministrado.

El workflow requiere que los secretos OIDC de Azure estén configurados y que la identidad utilizada tenga permiso para desplegar en la Web App. Sin estos datos el despliegue no se completará. El plan Free F1, si está disponible, puede servir para este tutorial.

## Publicar en Google Cloud Run

El archivo `cloudbuild.yaml` sigue compilando y desplegando el `Dockerfile`. Por tanto, en Cloud Run se ejecuta Python **3.14.8**, sin modificaciones adicionales al proceso de compilación original. Es necesario configurar previamente Cloud Build, Artifact Registry y los permisos correspondientes.

## Archivos principales

- `index.html`: la interfaz original; se conserva sin cambios.
- `server.py`: reemplaza `server.js` y atiende las rutas HTTP.
- `test_server.py`: pruebas automáticas sin dependencias.
- `Dockerfile` y `compose.yaml`: contenedor con Python 3.14.8.
- `.python-version`: selección de versión para herramientas compatibles.
- `requirements.txt`: indica que no se instalan paquetes externos.
- `.github/workflows/main_paginacalculadora.yml`: CI con Python y despliegue a Azure.
- `cloudbuild.yaml`: despliegue de contenedor a Cloud Run.
