# Cuaderno de mecanismos · Azure

Proyecto estático de Artemio Araya con dos modelos mecánicos interactivos.
Esta entrega tiene una sola copia del sitio y un solo workflow para Azure.

## Estructura del repositorio

```text
.github/
  workflows/
    main_visualizador-web-estudiante01.yml
site/
  index.html
  assets/
    styles.css
  viewers/
    AutoMind_MJCF_Modular_Viewer_1.html
    AutoMind_MJCF_Modular_Viewer_2.html
ATTRIBUTIONS.md
FONT-LICENSE.txt
README.md
```

El ZIP contiene directamente estos archivos. No incluye una carpeta exterior
ni una copia anidada en `mecanismos-retro/`.

## Sustituir la entrega anterior

1. Descomprime el ZIP en una carpeta nueva.
2. Copia su contenido a la raíz del repositorio `Tutorial-Web-I`, incluyendo
   `.github/`. En GitHub deben quedar `.github/` y `site/` al mismo nivel.
3. Elimina del repositorio la copia anterior `mecanismos-retro/` y conserva un
   solo workflow de despliegue: el incluido en esta entrega. Copiar los nuevos
   archivos sobre una carpeta existente no elimina los antiguos.
4. Guarda los cambios en la rama `main` y súbelos a GitHub. El workflow se
   ejecuta con cada push a `main`; también permite ejecución manual desde
   Actions → Publicar sitio en Azure → Run workflow.

Los visores superan el límite de carga de archivos de la interfaz web de GitHub.
Sube el repositorio mediante Git o GitHub Desktop. No subas el ZIP como sustituto
de los archivos: Actions necesita acceder a `site/index.html` y al workflow.

## Publicación en Azure

El workflow publica únicamente `site/` en la aplicación existente
`visualizador-web-estudiante01`, slot `Production`. Los nombres de secretos de
Azure se mantienen iguales a los de tu configuración anterior. Los valores de
los secretos se conservan en GitHub; este ZIP no contiene credenciales.

La página utiliza HTML, CSS y JavaScript. No necesita Composer, instalación de
PHP, npm ni compilación. El workflow verifica `site/index.html`, inicia sesión
en Azure y publica esa carpeta.

Modificar o descomprimir estos archivos en tu equipo no actualiza Azure hasta
que subas los cambios a GitHub. La aplicación de Azure debe estar en ejecución
para servir la página.

## Estilo y audio

La página y ambos visores usan Latin Modern Mono, papel beige `#f2e8cf` y tinta
`#332a24`. Los botones y menús siguen la misma paleta.

El audio `mixkit-typewriter-soft-hit-1366.wav` proporcionado por el usuario está
embebido en base64 en cada visor y reemplaza el sonido anterior de los botones.
No es necesario distribuir un WAV aparte. Los modelos, las imágenes y las
fuentes también están incluidos en los archivos del sitio.

Los módulos JavaScript del visor siguen cargándose desde Internet. Los recursos
embebidos no convierten esta página en una aplicación completamente offline.

## Vista previa

Abre `site/index.html` en un navegador con conexión a Internet y WebGL habilitado.
También puedes servir la carpeta `site/` con un servidor HTTP local.

Los créditos y las condiciones de los recursos se incluyen en `ATTRIBUTIONS.md`
y `FONT-LICENSE.txt`.
