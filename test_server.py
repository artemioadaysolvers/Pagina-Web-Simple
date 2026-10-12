"""Pruebas de integración con la biblioteca estándar."""

import json
import threading
import unittest
from http.server import ThreadingHTTPServer
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from server import Manejador


class PruebasServidor(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.servidor = ThreadingHTTPServer(("127.0.0.1", 0), Manejador)
        cls.hilo = threading.Thread(target=cls.servidor.serve_forever, daemon=True)
        cls.hilo.start()
        cls.url = f"http://127.0.0.1:{cls.servidor.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.servidor.shutdown()
        cls.servidor.server_close()
        cls.hilo.join(timeout=3)

    def consultar(self, ruta, datos=None, cuerpo=None):
        if datos is not None:
            cuerpo = json.dumps(datos).encode("utf-8")
        req = Request(self.url + ruta, data=cuerpo, headers={"Content-Type": "application/json"})
        try:
            with urlopen(req, timeout=3) as respuesta:
                return respuesta.status, respuesta.read(), respuesta.headers
        except HTTPError as error:
            return error.code, error.read(), error.headers

    def test_pagina(self):
        estado, contenido, cabeceras = self.consultar("/")
        self.assertEqual(estado, 200)
        self.assertIn(b"hello world", contenido)
        self.assertIn(b"/api/sumar", contenido)
        self.assertIn("text/html", cabeceras["Content-Type"])

    def test_estado(self):
        estado, contenido, _ = self.consultar("/health")
        self.assertEqual((estado, json.loads(contenido)), (200, {"estado": "ok"}))

    def test_suma_enteros(self):
        estado, contenido, _ = self.consultar("/api/sumar", {"a": 2, "b": 3})
        self.assertEqual((estado, json.loads(contenido)), (200, {"suma": 5}))

    def test_suma_decimales(self):
        estado, contenido, _ = self.consultar("/api/sumar", {"a": 0.1, "b": 0.2})
        self.assertEqual((estado, json.loads(contenido)), (200, {"suma": 0.3}))

    def test_datos_invalidos(self):
        casos = [{"a": True, "b": 2}, {"a": "2", "b": 3}, {"a": 2}, {"a": None, "b": 1}, {"a": float("inf"), "b": 1}]
        for datos in casos:
            with self.subTest(datos=datos):
                estado, _, _ = self.consultar("/api/sumar", datos)
                self.assertEqual(estado, 400)

    def test_resultado_no_finito(self):
        estado, _, _ = self.consultar("/api/sumar", {"a": 1e308, "b": 1e308})
        self.assertEqual(estado, 400)

    def test_json_invalido(self):
        estado, _, _ = self.consultar("/api/sumar", cuerpo=b"{mal}")
        self.assertEqual(estado, 400)

    def test_cuerpo_excesivo(self):
        estado, _, _ = self.consultar("/api/sumar", cuerpo=b" " * 1025)
        self.assertEqual(estado, 413)

    def test_ruta_inexistente(self):
        estado, contenido, _ = self.consultar("/no-existe")
        self.assertEqual(estado, 404)
        self.assertEqual(json.loads(contenido), {"error": "Ruta no encontrada"})


if __name__ == "__main__":
    unittest.main()
