# Tutorial Web I - usando un flujo de trabajo EXISTENTE

**Objetivo:** subir un único proyecto a GitHub y, en Azure, escoger **«Usar flujo de trabajo existente»**.

## Proyecto

El sitio original está en `site/` (HTML, CSS, JavaScript y ambos visualizadores 3D). En la raíz están `package.json`, `package-lock.json` y `server.js`: Azure puede detectar Node.js, construir el proyecto con Oryx e iniciarlo usando `npm start`. No necesitas Python, PHP, PM2, ni editar variables de compilación para un despliegue nuevo.

## Instrucciones

1. Descomprimir el ZIP. En tu repositorio GitHub, copiar **todo el contenido de `Tutorial-Web-I-main/`** (también la carpeta oculta `.github`), conservando su estructura. Hacer Commit y Push a `main` en GitHub Desktop. Verificar que aparece el archivo `.github/workflows/deploy-azure-existing.yml` en GitHub.
2. En Azure Portal, crear **App Services > Crear > Aplicación web**, Publicar **Código**, Linux, **Node.js 26** si está disponible. Crear grupo `rg-visualizador-web` y la aplicación web con un nombre globalmente disponible. F1/Gratis y Chile Central solo si Azure permite la combinación; revisar el costo estimado.
3. En la aplicación creada, abrir **Centro de implementación > GitHub**, autorizar y elegir el repositorio y la rama `main`. Mantener **GitHub Actions**.
4. En **Flujo de trabajo**, elegir **Usar flujo de trabajo existente** y seleccionar `.github/workflows/deploy-azure-existing.yml` (si muestra solamente el nombre, `deploy-azure-existing.yml`).
5. En **Autenticación**, seleccionar **Identidad asignada por el usuario** y crear/elegir la identidad con permisos de publicación. **Guardar**. Azure configura en GitHub los secretos `AZURE_CLIENT_ID`, `AZURE_TENANT_ID` y `AZURE_SUBSCRIPTION_ID` cuando esta configuración es compatible y tienes los permisos necesarios.
6. En GitHub > **Actions**, abrir **Publicar Tutorial Web I en Azure (workflow existente)** y pulsar **Run workflow** para iniciar el primer despliegue. Luego, cada cambio en `main` vuelve a desplegar.

## Si hay mas de una App Service en el grupo

El workflow intenta encontrar **una única aplicación** en `rg-visualizador-web`. Si la identidad de Azure no permite enumerarlas, o hay más de una, en GitHub > Settings > Secrets and variables > Actions > Variables, crear la variable `AZURE_WEBAPP_NAME` con el nombre exacto de la aplicación de destino. No hay que editar el YAML. Para el ejemplo que ya existía en tu suscripción también se admite `visualizador-web-estudiante01` como respaldo si Azure autoriza a consultarla.

## Si el despliegue falla

- `Login failed`: revisar que Azure ha creado los tres secretos comunes y la identidad tiene permiso Website Contributor sobre la aplicación. Puede ser necesario volver a guardar la conexión en Centro de implementación.
- `Could not detect any platform`: verificar que `package.json` está en la raíz del repositorio **y** que el workflow despliega `package: '.'`.
- Página de bienvenida o error 404: confirmar despliegue completo y revisar el registro de App Service.
- Node 26 no disponible: seleccionar una versión de Node.js soportada por la región y suscripción. El servidor usa APIs estándar compatibles con Node.js >=20.

Esta configuración se entrega para un **proyecto nuevo** con el despliegue gestionado por Azure. Si una aplicación existente tiene Oryx desactivado manualmente, un inicio personalizado incorrecto o una pila diferente, habrá que corregir esa configuración histórica en Azure; el ZIP no puede alterar opciones remotas.

Fuentes: https://learn.microsoft.com/azure/app-service/deploy-continuous-deployment ; https://learn.microsoft.com/azure/app-service/configure-language-nodejs
