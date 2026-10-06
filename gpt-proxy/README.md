# Página de suma con backend

La página muestra `hello world` en rojo y permite introducir dos números.
Al pulsar **Sumar**, envía los números al backend (`POST /api/sumar`) y muestra
la respuesta. El frontend y el backend se sirven desde el mismo proceso Node.js.

## Ejecutar localmente

```sh
npm start
```

Abrir http://localhost:8080. También puedes usar `docker compose up --build`.
No hay dependencias de npm que instalar.

## Publicar en Azure desde GitHub privado

Azure Blob Storage solo publica archivos estáticos; para ejecutar este backend
crea una **Web App (App Service)** con publicación de **código**, runtime Node.js
y una región permitida por tu suscripción. Elige el plan Free F1 si está disponible.
Azure te dará una dirección `*.azurewebsites.net` sin comprar un dominio.

El workflow `.github/workflows/publicar-azure-app-service.yml` despliega
automáticamente cada cambio de la rama `main`. Si tu rama tiene otro nombre,
modifica `branches` en el workflow.

En la configuración del repositorio de GitHub, crea:

- Variable de Actions `AZURE_WEBAPP_NAME`: nombre exacto de la Web App en Azure.
- Secreto de Actions `AZURE_WEBAPP_PUBLISH_PROFILE`: contenido completo del
  perfil de publicación descargado desde la Web App. Nunca lo guardes en el repo.

El secreto `AZURE_STORAGE_CONNECTION_STRING` del sitio estático anterior no se
utiliza en esta versión. El sitio anterior de Blob Storage tampoco se actualizará
con este workflow.

Si Azure no permite descargar el perfil de publicación, configura la conexión
con GitHub desde **Centro de implementación** de la Web App; Azure generará su
propio workflow con la autenticación disponible para tu cuenta.

## Otros archivos

`Dockerfile` y `compose.yaml` permiten ejecutar el proyecto en un contenedor.
`cloudbuild.yaml` mantiene una opción de despliegue en Google Cloud Run, separada
del workflow de Azure.
