"""Página de suma y API, servidas por Python y Waitress."""

import json
import logging
import math
import os
import platform
from http import HTTPStatus
from pathlib import Path


DIRECTORIO = Path(__file__).resolve().parent
PAGINA = (DIRECTORIO / "index.html").read_bytes()
VERSION_PYTHON = (DIRECTORIO / ".python-version").read_text().strip()
LIMITE_CUERPO = 1024


def responder(iniciar_respuesta, estado, cuerpo, tipo="application/json"):
    iniciar_respuesta(
        f"{estado} {HTTPStatus(estado).phrase}",
        [
            ("Content-Type", f"{tipo}; charset=utf-8"),
            ("Content-Length", str(len(cuerpo))),
            ("Cache-Control", "no-store"),
        ],
    )
    return [cuerpo]


def enviar_json(iniciar_respuesta, estado, datos):
    cuerpo = json.dumps(datos, ensure_ascii=False, allow_nan=False).encode("utf-8")
    return responder(iniciar_respuesta, estado, cuerpo)


def rechazar_constante(valor):
    # NaN e Infinity no forman parte del formato JSON.
    raise ValueError(f"Constante JSON inválida: {valor}")


def es_numero(valor):
    # En Python bool hereda de int; la API acepta solo números JSON.
    if type(valor) not in (int, float):
        return False
    try:
        return math.isfinite(float(valor))
    except OverflowError:
        return False


def aplicacion(entorno, iniciar_respuesta):
    metodo = entorno.get("REQUEST_METHOD", "GET")
    ruta = entorno.get("PATH_INFO", "/")

    if metodo == "GET" and ruta == "/":
        return responder(iniciar_respuesta, 200, PAGINA, "text/html")

    if metodo == "GET" and ruta == "/health":
        return enviar_json(iniciar_respuesta, 200, {"estado": "ok"})

    if metodo == "POST" and ruta == "/api/sumar":
        try:
            longitud = int(entorno.get("CONTENT_LENGTH") or "0")
            if longitud < 0:
                raise ValueError("Longitud inválida")
            if longitud > LIMITE_CUERPO:
                return enviar_json(
                    iniciar_respuesta, 413, {"error": "Solicitud demasiado grande"}
                )
            cuerpo = entorno["wsgi.input"].read(longitud)
            if len(cuerpo) != longitud:
                raise ValueError("Cuerpo incompleto")
            datos = json.loads(cuerpo.decode("utf-8"), parse_constant=rechazar_constante)
        except (ValueError, UnicodeError, RecursionError):
            return enviar_json(iniciar_respuesta, 400, {"error": "Solicitud JSON inválida"})

        if (
            not isinstance(datos, dict)
            or not es_numero(datos.get("a"))
            or not es_numero(datos.get("b"))
        ):
            return enviar_json(
                iniciar_respuesta, 400, {"error": "Introduce dos números válidos"}
            )

        # Igual que el backend original, usamos números de doble precisión
        # y devolvemos el resultado con 15 cifras significativas.
        suma = float(datos["a"]) + float(datos["b"])
        if not math.isfinite(suma):
            return enviar_json(
                iniciar_respuesta, 400, {"error": "El resultado es demasiado grande"}
            )
        return enviar_json(iniciar_respuesta, 200, {"suma": float(f"{suma:.15g}")})

    return enviar_json(iniciar_respuesta, 404, {"error": "Ruta no encontrada"})


def comprobar_version():
    if platform.python_version() != VERSION_PYTHON:
        raise SystemExit(
            f"Este proyecto requiere Python {VERSION_PYTHON}; "
            f"estás usando {platform.python_version()}. "
            "Instala la versión indicada o ejecuta docker compose up --build."
        )


def main():
    comprobar_version()
    try:
        puerto = int(os.environ.get("PORT", "8080"))
        if not 1 <= puerto <= 65535:
            raise ValueError
    except ValueError:
        raise SystemExit("PORT debe ser un entero entre 1 y 65535.") from None

    from waitress import serve

    logging.basicConfig(level=logging.INFO)
    logging.info("Servidor Python %s iniciado en el puerto %s", VERSION_PYTHON, puerto)
    serve(
        aplicacion,
        host=os.environ.get("HOST", "0.0.0.0"),
        port=puerto,
        threads=4,
        max_request_body_size=1024 * 1024,
        expose_tracebacks=False,
    )


if __name__ == "__main__":
    main()
