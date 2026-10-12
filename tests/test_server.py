import http.client
import json
import threading
import unittest

from waitress import create_server

from server import PAGINA, aplicacion, comprobar_version


class BackendTests(unittest.TestCase):
    """Verifica el contrato HTTP que utiliza la página, con un servidor real."""

    @classmethod
    def setUpClass(cls):
        comprobar_version()
        cls.servidor = create_server(aplicacion, host="127.0.0.1", port=0)
        cls.puerto = int(cls.servidor.effective_port)
        cls.hilo = threading.Thread(target=cls.servidor.run, daemon=True)
        cls.hilo.start()

    @classmethod
    def tearDownClass(cls):
        cls.servidor.close()
        cls.hilo.join(timeout=5)

    def solicitar(self, metodo, ruta, cuerpo=None):
        conexion = http.client.HTTPConnection("127.0.0.1", self.puerto, timeout=5)
        try:
            conexion.request(metodo, ruta, body=cuerpo, headers={"Content-Type": "application/json"})
            respuesta = conexion.getresponse()
            return respuesta.status, dict(respuesta.getheaders()), respuesta.read()
        finally:
            conexion.close()

    def test_pagina(self):
        estado, cabeceras, cuerpo = self.solicitar("GET", "/?ejemplo=1")
        self.assertEqual(estado, 200)
        self.assertIn("text/html", cabeceras["Content-Type"])
        self.assertEqual(cuerpo, PAGINA)

    def test_health(self):
        estado, cabeceras, cuerpo = self.solicitar("GET", "/health")
        self.assertEqual(estado, 200)
        self.assertEqual(json.loads(cuerpo), {"estado": "ok"})
        self.assertEqual(cabeceras["Cache-Control"], "no-store")

    def test_sumas(self):
        for a, b, esperado in [(2, 3, 5), (-8, 3, -5), (0, 0, 0), (0.1, 0.2, 0.3), (1e100, 1e100, 2e100)]:
            with self.subTest(a=a, b=b):
                estado, _, cuerpo = self.solicitar("POST", "/api/sumar", json.dumps({"a": a, "b": b}))
                self.assertEqual(estado, 200)
                self.assertEqual(json.loads(cuerpo), {"suma": esperado})

    def test_numeros_invalidos(self):
        for datos in [{"a": "2", "b": 3}, {"a": True, "b": 3}, {"a": None, "b": 3}, {"a": 2}, {}, [], None, {"a": 1e309, "b": 0}]:
            with self.subTest(datos=datos):
                estado, _, cuerpo = self.solicitar("POST", "/api/sumar", json.dumps(datos))
                self.assertEqual(estado, 400)
                self.assertIn("error", json.loads(cuerpo))

    def test_json_invalido(self):
        for cuerpo in [b"", b"{", b'{"a": NaN, "b": 2}', b'{"a": Infinity, "b": 2}', b"\xff"]:
            with self.subTest(cuerpo=cuerpo):
                estado, _, respuesta = self.solicitar("POST", "/api/sumar", cuerpo)
                self.assertEqual(estado, 400)
                self.assertEqual(json.loads(respuesta)["error"], "Solicitud JSON inválida")

    def test_resultado_demasiado_grande(self):
        estado, _, cuerpo = self.solicitar("POST", "/api/sumar", b'{"a": 1e308, "b": 1e308}')
        self.assertEqual(estado, 400)
        self.assertEqual(json.loads(cuerpo)["error"], "El resultado es demasiado grande")

    def test_limite_cuerpo(self):
        datos = b'{"a": 2, "b": 3}'
        for longitud, esperado in [(1024, 200), (1025, 413)]:
            with self.subTest(longitud=longitud):
                estado, _, cuerpo = self.solicitar("POST", "/api/sumar", datos.ljust(longitud, b" "))
                self.assertEqual(estado, esperado)
                self.assertIn("suma" if esperado == 200 else "error", json.loads(cuerpo))

    def test_ruta_o_metodo_desconocido(self):
        for metodo, ruta in [("GET", "/server.py"), ("GET", "/api/sumar"), ("POST", "/health"), ("PUT", "/api/sumar"), ("GET", "/no-existe")]:
            with self.subTest(metodo=metodo, ruta=ruta):
                estado, _, cuerpo = self.solicitar(metodo, ruta)
                self.assertEqual(estado, 404)
                self.assertEqual(json.loads(cuerpo)["error"], "Ruta no encontrada")


if __name__ == "__main__":
    unittest.main()
