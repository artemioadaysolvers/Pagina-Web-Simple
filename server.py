"""Servidor HTTP sencillo para la página de suma (Python 3.14.8).

No necesita instalar bibliotecas externas.
"""

import json
import math
import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit


PAGINA = Path(__file__).with_name("index.html").read_bytes()
LIMITE_CUERPO = 1024


class Manejador(BaseHTTPRequestHandler):
    """Sirve el frontend y las rutas de la API."""

    def enviar(self, estado, contenido, tipo):
        self.send_response(estado)
        self.send_header("Content-Type", tipo)
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(contenido)))
        self.end_headers()
        self.wfile.write(contenido)

    def enviar_json(self, estado, datos):
        contenido = json.dumps(datos, ensure_ascii=False, allow_nan=False).encode("utf-8")
        self.enviar(estado, contenido, "application/json; charset=utf-8")

    def do_GET(self):
        ruta = urlsplit(self.path).path

        if ruta == "/":
            self.enviar(200, PAGINA, "text/html; charset=utf-8")
        elif ruta == "/health":
            self.enviar_json(200, {"estado": "ok"})
        else:
            self.enviar_json(404, {"error": "Ruta no encontrada"})

    def do_POST(self):
        if urlsplit(self.path).path != "/api/sumar":
            self.enviar_json(404, {"error": "Ruta no encontrada"})
            return

        longitud = self.headers.get("Content-Length")
        if longitud is None:
            self.enviar_json(411, {"error": "Falta Content-Length"})
            return
        try:
            cantidad = int(longitud)
        except ValueError:
            self.enviar_json(400, {"error": "Content-Length inválido"})
            return

        if cantidad < 0:
            self.enviar_json(400, {"error": "Content-Length inválido"})
            return
        if cantidad > LIMITE_CUERPO:
            self.enviar_json(413, {"error": "Solicitud demasiado grande"})
            return

        try:
            cuerpo = self.rfile.read(cantidad)
            datos = json.loads(cuerpo.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError):
            self.enviar_json(400, {"error": "Solicitud JSON inválida"})
            return

        if not isinstance(datos, dict):
            self.enviar_json(400, {"error": "Introduce dos números válidos"})
            return

        try:
            # bool es una subclase de int en Python, pero no equivale a un número JSON.
            a, b = datos["a"], datos["b"]
            if any(isinstance(x, bool) or not isinstance(x, (int, float)) for x in (a, b)):
                raise ValueError("Se necesitan dos números")
            a, b = float(a), float(b)
            if not (math.isfinite(a) and math.isfinite(b)):
                raise ValueError("Los números deben ser finitos")
        except (KeyError, ValueError, OverflowError):
            self.enviar_json(400, {"error": "Introduce dos números válidos"})
            return

        suma = a + b
        if not math.isfinite(suma):
            self.enviar_json(400, {"error": "El resultado es demasiado grande"})
            return

        # Conserva las 15 cifras significativas del servidor Node.js original.
        suma = float(format(suma, ".15g"))
        if suma.is_integer() and abs(suma) <= 1e15:
            suma = int(suma)
        self.enviar_json(200, {"suma": suma})


def main():
    # Azure App Service (runtime administrado) utiliza normalmente el puerto 8000.
    # En local y Cloud Run se mantiene el 8080, salvo si PORT está definido.
    puerto_por_defecto = "8000" if os.environ.get("WEBSITE_SITE_NAME") else "8080"
    puerto = int(os.environ.get("PORT", puerto_por_defecto))
    servidor = ThreadingHTTPServer(("0.0.0.0", puerto), Manejador)
    print(f"Servidor Python iniciado en el puerto {puerto}", flush=True)
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("Servidor detenido")
    finally:
        servidor.server_close()


if __name__ == "__main__":
    main()
