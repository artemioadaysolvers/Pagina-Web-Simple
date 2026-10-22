# Publicar Tutorial-Web-I en Azure App Service (Linux)

## 1. Configurar Azure

1. Abrir Azure Portal > App Services > visualizador-web-estudiante01.
2. En Configuracion > Configuracion de pila, seleccionar **Node.js**, con una version LTS compatible disponible.
3. En el campo **Comando de inicio**, establecer exactamente:

   ```bash
   pm2 serve /home/site/wwwroot --no-daemon
   ```

4. Guardar los cambios; App Service reiniciara la aplicacion.
5. En Configuracion > Variables de entorno, verificar que `SCM_DO_BUILD_DURING_DEPLOYMENT` no este en `true`; para esta pagina estatica, usar `false` para evitar compilacion con Oryx.

Nota: Node.js se utiliza solamente para servir los archivos HTML, CSS y JavaScript; el proyecto no tiene backend en Node.js ni Python. No se requiere instalar dependencias de Python.

## 2. Subir el contenido del ZIP al repositorio

1. Abrir GitHub Desktop con el repositorio `artemioadaysolvers/Tutorial-Web-I` clonado.
2. Extraer el ZIP y copiar **el contenido de la carpeta Tutorial-Web-I-main**, no la carpeta contenedora, a la raiz del repositorio clonado.
3. Conservar los archivos y subcarpetas `site`, `.github/workflows`, `.gitattributes`, `.gitignore`, etc. Si se solicita reemplazo del workflow, aceptarlo.
4. Hacer Commit to main y luego Push origin.
5. Ir a GitHub > Actions. El flujo publicara `site/` en Azure App Service.

## 3. Verificaciones

- El archivo `.github/workflows/main_visualizador-web-estudiante01.yml` usa `azure/login@v2` y `azure/webapps-deploy@v3`.
- Publica `package: site`, que contiene `index.html`, estilos y ambos visores 3D.
- Los nombres de los secretos de GitHub referenciados son los del flujo de Azure mas reciente que se encontro, no los secretos anteriores del ZIP.
- Si falla el paso de autenticacion, hay que comprobar Settings > Secrets and variables > Actions y la identidad federada configurada en Azure. El ZIP no contiene los valores secretos.
- Si GitHub Actions termina en verde pero aparece la pagina por defecto de Azure, revisar el comando de inicio, la pila Node.js, las variables de entorno y los registros de la aplicacion en Azure.

## Cambios en este ZIP

- Reemplazado el workflow de Python por despliegue estatico de la carpeta `site`.
- Conservados sin cambios los archivos de la pagina, visores 3D, CSS, licencias y tutorial PDF de la copia descargada.
- Actualizado el README para coincidir con la version actual comprobada en GitHub.
- Agregada esta guia como documento independiente.

**Importante:** no se ha ejecutado un despliegue real ni se ha podido verificar la configuracion privada de Azure del usuario.
