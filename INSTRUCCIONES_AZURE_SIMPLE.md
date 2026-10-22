# Publicación sencilla de Tutorial-Web-I en Azure App Service

El frontend original utiliza **HTML, CSS y JavaScript**. `server.js` lo sirve con Node.js y no requiere paquetes externos.

1. Extraer el ZIP. En GitHub, crear un repositorio propio (por ejemplo `Tutorial-Web-I`) y subir **el contenido de la carpeta `Tutorial-Web-I-main` a la raíz de la rama `main`** mediante GitHub Desktop (Commit → Push). Debe quedar `package.json` visible en la raíz de GitHub, junto a `server.js` y `site`.
2. En Azure Portal, crear **App Services → Aplicación web → Código**, con **Linux** y **Node.js 26** si está disponible en la suscripción y región. Elegir el plan y comprobar el costo antes de crear.
3. En el recurso, abrir **Centro de implementación**. Seleccionar **GitHub → GitHub Actions**, autorizar y elegir la cuenta, el repositorio y `main`.
4. Seleccionar **Identidad asignada por el usuario**, crear o elegir la identidad propuesta por Azure, y pulsar **Guardar**. Azure generará el workflow propio de esa cuenta.
5. En GitHub → Actions, comprobar que la ejecución termine correctamente; abrir el dominio publicado en Azure.

No hace falta crear un archivo `.github/workflows/*.yml` manualmente, definir `requirements.txt`, modificar variables Oryx ni introducir un comando de inicio. Azure detecta `package.json` en la raíz y utiliza `npm start` para ejecutar `server.js`.

**Importante:** sólo crear App Service no publica contenido. Se requiere subir el código a GitHub y conectar Azure en el Centro de implementación. Node.js 26 puede estar en versión preliminar; si no figura disponible, consulta la pila admitida en tu suscripción/región.
