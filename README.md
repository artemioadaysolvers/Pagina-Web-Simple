# Cuaderno de mecanismos

Un cuaderno visual de [Artemio Araya](https://github.com/artemioadaysolvers) para explorar dos mecanismos de pinza en 3D: geometría, piezas y relaciones mecánicas. Los dos visores HTML originales se presentan uno debajo del otro, dentro de una única página.

Frontend estático de HTML, CSS y JavaScript. Sin instalación de paquetes ni proceso de compilación. El despliegue en GitHub Pages publica únicamente la carpeta `site/`.

La presentación toma como referencia el PDF *Modelamiento Matemático (10).pdf* proporcionado por el usuario: tipografía Latin Modern Mono, fondo de papel `#f2e8cf` y tinta `#332a24`.

## Crédito tecnológico

Utiliza tecnología de AutoMind, con código fuente disponible en GitHub. Las herramientas enlazadas son desarrolladas por [Artemio Araya](https://github.com/artemioadaysolvers), cuyo perfil público figura como Artemio Araya Day.

- [AutoMind URDF / USD / MJCF Loader](https://github.com/artemioadaysolvers/AutoMind-URDF-USD-MJCF-Loader): visores de modelos URDF+, USD y MJCF para frontend web, Power BI y Google Colab.
- [AutoMindCloud Experimental](https://github.com/artemioadaysolvers/AutoMindCloudExperimental): reúne sustitución automática complementaria a SymPy, resúmenes de cálculo con IA, pizarra y visores CAD y robóticos en Google Colab.
- [Converter .IAM → MJCF / USD](https://github.com/artemioadaysolvers/.IAM-to-MJCF-USD-Plugin-AutoDesk-Inventor-): complemento de Autodesk Inventor que convierte ensamblajes `.IAM` a MJCF y USD.

Google Colab corresponde a los proyectos enlazados; esta página se publica como un frontend estático. Los créditos y las condiciones de cada recurso se documentan por separado en [ATTRIBUTIONS.md](ATTRIBUTIONS.md).

## Publicar en GitHub

1. Crea un repositorio vacío en GitHub, por ejemplo `cuaderno-mecanismos`.
2. Desde esta carpeta, sube los archivos; sustituye `TU_USUARIO` por tu cuenta:

   ```sh
   git init
   git add .
   git commit -m "Agregar Cuaderno de mecanismos"
   git branch -M main
   git remote add origin https://github.com/TU_USUARIO/cuaderno-mecanismos.git
   git push -u origin main
   ```

   Utiliza Git para subir el repositorio: los HTML originales son demasiado grandes para la carga de archivos desde la interfaz web de GitHub.

3. En el repositorio, abre **Settings → Pages → Build and deployment → Source** y elige **GitHub Actions**.
4. En **Actions**, abre **Publicar en GitHub Pages** y pulsa **Run workflow** sobre `main` si el primer despliegue todavía no se ha completado.

La dirección será `https://TU_USUARIO.github.io/cuaderno-mecanismos/`. Los siguientes cambios enviados a `main` se publican automáticamente. El flujo también se puede ejecutar manualmente desde **Actions**. No necesitas configurar secretos.

Referencia: [desplegar con un flujo personalizado de GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Vista previa local

Puedes abrir `site/index.html` directamente en tu navegador, con conexión a Internet. También puedes utilizar una vista previa HTTP; con Python instalado, ejecuta desde esta carpeta:

```sh
python -m http.server 8000 --directory site
```

Abre [http://localhost:8000](http://localhost:8000). Este servidor se utiliza sólo para la vista previa; la página publicada funciona íntegramente en el navegador.

Necesitas JavaScript y un navegador con WebGL habilitado. Los modelos están dentro de los HTML originales; sus dependencias externas conservan las direcciones originales y requieren conexión a Internet.

La web tiene una única página principal con dos visores embebidos. El proyecto no utiliza Node.js, npm, TypeScript, frameworks, backend ni base de datos. Los visores conservan la carga de sus dependencias remotas tal como venía en los HTML originales.

Los dos visores se incorporan mediante `iframe` y comparten el estilo del cuaderno: Latin Modern Mono, papel beige `#f2e8cf`, tinta marrón y controles de bordes discretos. El fondo del escenario 3D también es beige. Sus modelos y controles se conservan. El sonido anterior de los botones se sustituye por `mixkit-typewriter-soft-hit-1366.wav`, embebido en base64 en cada HTML; el audio no necesita conexión ni un archivo WAV aparte. Los módulos del visor siguen requiriendo Internet.

## Archivos

```text
site/
  index.html       Página principal
  assets/          Estilos, tipografía y recursos visuales
  viewers/         Los dos visores con estilo y audio adaptados
.github/workflows/deploy.yml
ATTRIBUTIONS.md
```

Los créditos, fuentes y condiciones de los recursos están en [ATTRIBUTIONS.md](ATTRIBUTIONS.md).

Las dos fichas de GrabCAD facilitadas por el usuario están enlazadas en la página y en las atribuciones. La consulta no permitió verificar los nombres de los autores, porque GrabCAD no mostró sus datos o bloqueó el acceso.
