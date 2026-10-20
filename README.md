# AutoMind · Mechanics

Una página para explorar dos mecanismos de pinza en 3D: geometría, piezas y relaciones mecánicas, con los dos visores HTML originales de AutoMind integrados uno debajo del otro.

Frontend estático de HTML, CSS y JavaScript. Sin instalación de paquetes ni proceso de compilación. El despliegue en GitHub Pages publica únicamente la carpeta `site/`.

## Herramientas de Artemio Araya

Las herramientas de AutoMind enlazadas aquí son desarrolladas por [Artemio Araya](https://github.com/artemioadaysolvers), cuyo perfil público figura como Artemio Araya Day.

- [AutoMind URDF / USD / MJCF Loader](https://github.com/artemioadaysolvers/AutoMind-URDF-USD-MJCF-Loader): visores de modelos URDF+, USD y MJCF para frontend web, Power BI y Google Colab.
- [AutoMindCloud Experimental](https://github.com/artemioadaysolvers/AutoMindCloudExperimental): reúne sustitución automática complementaria a SymPy, resúmenes de cálculo con IA, pizarra y visores CAD y robóticos en Google Colab.
- [Converter .IAM → MJCF / USD](https://github.com/artemioadaysolvers/.IAM-to-MJCF-USD-Plugin-AutoDesk-Inventor-): complemento de Autodesk Inventor que convierte ensamblajes `.IAM` a MJCF y USD. La dirección `AutoMind-IAM-to-MJCF` indicada inicialmente devolvía 404; el enlace anterior es el repositorio público verificado del mismo autor con esa función.

La propuesta de innovación conecta diseño CAD, visualización robótica y cálculo interactivo entre herramientas. Google Colab corresponde a los proyectos enlazados; esta página se publica como un frontend estático.

## Publicar en GitHub

1. Crea un repositorio vacío en GitHub, por ejemplo `automind-mechanics`.
2. Desde esta carpeta, sube los archivos; sustituye `TU_USUARIO` por tu cuenta:

   ```sh
   git init
   git add .
   git commit -m "Agregar galería de mecanismos AutoMind"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/automind-mechanics.git
   git push -u origin main
   ```

   Utiliza Git para subir el repositorio: los HTML originales son demasiado grandes para la carga de archivos desde la interfaz web de GitHub.

3. En el repositorio, abre **Settings → Pages → Build and deployment → Source** y elige **GitHub Actions**.
4. En **Actions**, abre **Publicar en GitHub Pages** y pulsa **Run workflow** sobre `main` si el primer despliegue todavía no se ha completado.

La dirección será `https://TU_USUARIO.github.io/automind-mechanics/`. Los siguientes cambios enviados a `main` se publican automáticamente. El flujo también se puede ejecutar manualmente desde **Actions**. No necesitas configurar secretos.

Referencia: [desplegar con un flujo personalizado de GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Vista previa local

Puedes abrir `site/index.html` directamente en tu navegador, con conexión a Internet. También puedes utilizar una vista previa HTTP; con Python instalado, ejecuta desde esta carpeta:

```sh
python -m http.server 8000 --directory site
```

Abre [http://localhost:8000](http://localhost:8000). Este servidor se utiliza sólo para la vista previa; la página publicada funciona íntegramente en el navegador.

Necesitas JavaScript y un navegador con WebGL habilitado. Los modelos están dentro de los HTML originales; sus dependencias externas conservan las direcciones originales y requieren conexión a Internet.

La web tiene una única página principal con dos visores embebidos. El proyecto no utiliza Node.js, npm, TypeScript, frameworks, backend ni base de datos. Los visores conservan la carga de sus dependencias remotas tal como venía en los HTML originales.

Los dos archivos HTML suministrados se conservan sin modificaciones. La página los incorpora mediante `iframe` y no altera su contenido, modelos ni dependencias.

## Archivos

```text
site/
  index.html       Página principal
  assets/          Estilos y logotipos
  viewers/         Los dos HTML originales sin modificaciones
.github/workflows/deploy.yml
ATTRIBUTIONS.md
```

Los créditos, fuentes y condiciones de los recursos están en [ATTRIBUTIONS.md](ATTRIBUTIONS.md).

Las dos fichas de GrabCAD facilitadas por el usuario están enlazadas en la página y en las atribuciones. La consulta no permitió verificar los nombres de los autores, porque GrabCAD no mostró sus datos o bloqueó el acceso.
