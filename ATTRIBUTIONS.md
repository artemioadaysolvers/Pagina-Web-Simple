# Cuaderno de mecanismos · Fuentes y atribuciones

Página de [Artemio Araya](https://github.com/artemioadaysolvers), identificado como Artemio Araya Day en su perfil público.

## Crédito tecnológico

Utiliza tecnología de AutoMind, con código fuente disponible en GitHub.

Los dos visores parten de los archivos proporcionados por el usuario:

- `AutoMind_MJCF_Modular_Viewer_1.html`
- `AutoMind_MJCF_Modular_Viewer_2.html`

Autor de las herramientas: Artemio Araya Day.

Los dos HTML se adaptaron para compartir la tipografía Latin Modern Mono, el fondo beige y los controles del cuaderno. Conservan sus modelos, recursos, logotipos y avisos. El sonido anterior de los botones se reemplazó por el archivo `mixkit-typewriter-soft-hit-1366.wav` proporcionado por el usuario, embebido en cada visor.

La regla de Git para `site/viewers/*.html` desactiva la conversión de finales de línea y conserva sus bytes al descargar el repositorio.

Proyectos de referencia:

- [AutoMind URDF / USD / MJCF Loader](https://github.com/artemioadaysolvers/AutoMind-URDF-USD-MJCF-Loader): visualización de modelos URDF+, USD y MJCF, con uso declarado para frontend web, Power BI y Google Colab.
- [AutoMindCloud Experimental](https://github.com/artemioadaysolvers/AutoMindCloudExperimental): biblioteca de ingeniería para Google Colab que reúne sustitución automática complementaria a SymPy, resúmenes de cálculo con IA, pizarra y visores de formatos CAD y robóticos. Su README enlaza la biblioteca en Colab y señala que el acceso puede requerir permisos de lectura del autor.
- [Converter .IAM → MJCF / USD](https://github.com/artemioadaysolvers/.IAM-to-MJCF-USD-Plugin-AutoDesk-Inventor-): complemento de Autodesk Inventor para convertir ensamblajes `.IAM` a MJCF y USD.

Google Colab es un entorno de uso documentado para Loader y AutoMindCloud Experimental. El convertidor es un complemento de Autodesk Inventor; no se presenta como una aplicación que se ejecute en Colab. Estos recursos enlazados no añaden un backend a esta página estática.

Los proyectos enlazados conservan sus propias condiciones. [AutoMindCloud Experimental publica su licencia propia](https://github.com/artemioadaysolvers/AutoMindCloudExperimental/blob/main/LICENSE); no se asigna una licencia MIT global a estas herramientas, a los visores ni a los modelos.

## Three.js

Los visores utilizan [Three.js r132](https://github.com/mrdoob/three.js/tree/r132), distribuido bajo la [licencia MIT de esa versión](https://github.com/mrdoob/three.js/blob/r132/LICENSE). Los avisos y las dependencias presentes en los HTML originales se mantienen intactos. Three.js corresponde al visor; la página principal utiliza HTML, CSS y JavaScript sin frameworks.

## Modelos CAD

El usuario facilitó las fichas originales de [GrabCAD Community Library](https://grabcad.com/library) para los dos modelos:

- `AutoMind_MJCF_Modular_Viewer_1.html` · identificador `Robot_Gripper` · 20 componentes: [Robot Gripper](https://grabcad.com/library/robot-gripper-37).
- `AutoMind_MJCF_Modular_Viewer_2.html` · identificador `262_GRIPPER_4` · 37 componentes: [3D CAD Basic Exercise — Mechanical Gripper / Pinza mecánica — Autodesk Inventor Pro](https://grabcad.com/library/3d-cad-basic-exercise-mechanical-gripper-pinza-mecanica-autodesk-inventor-pro-1).

Estas correspondencias proceden de la información proporcionada por el usuario. En esta consulta, GrabCAD devolvió una página sin los datos del modelo o un bloqueo HTTP 403, por lo que no fue posible verificar los nombres de sus autores ni las condiciones particulares de cada ficha. No se atribuyen los diseños a autores encontrados en otros modelos similares.

Los modelos conservan los derechos y condiciones de sus respectivos creadores. Este repositorio no les asigna una licencia nueva ni extiende la licencia de Three.js a los modelos o a los visores originales.

## Referencia visual y tipografía

La referencia de la página principal es el PDF *Modelamiento Matemático (10).pdf* proporcionado por el usuario. Se toma su aspecto de cuaderno impreso: papel `#f2e8cf`, tinta `#332a24` y tipografía monoespaciada Latin Modern Mono.

La familia [Latin Modern](https://ctan.org/pkg/lm), de B. Jackowski y J. M. Nowacki, se distribuye bajo la [GUST Font License](https://ctan.org/license/gfl). La página incluye las variantes LMMono12 regular, LMMonoLt10 negrita y LMMono10 cursiva en sus estilos. La licencia de las fuentes corresponde exclusivamente a esa familia tipográfica y se incluye en `FONT-LICENSE.txt`. Las fuentes y el logotipo del crédito tecnológico están embebidos en la página y sus estilos.

Esta presentación se aplica a la página principal y a la interfaz de ambos visores.

La insignia AutoMind en tonos beige y marrón de esta versión fue proporcionada por el usuario y se incluye sin modificaciones, embebida en la página y ambos visores.
