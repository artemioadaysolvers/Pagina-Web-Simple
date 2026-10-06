import http from 'node:http';
import { readFile } from 'node:fs/promises';

const pagina = await readFile(new URL('./index.html', import.meta.url));
const puerto = Number(process.env.PORT || 8080);

function enviarJson(respuesta, estado, datos) {
  respuesta.writeHead(estado, {
    'Content-Type': 'application/json; charset=utf-8',
    'Cache-Control': 'no-store'
  });
  respuesta.end(JSON.stringify(datos));
}

async function manejarPeticion(peticion, respuesta) {
  const ruta = new URL(peticion.url, 'http://localhost').pathname;

  if (peticion.method === 'GET' && ruta === '/') {
    respuesta.writeHead(200, {
      'Content-Type': 'text/html; charset=utf-8',
      'Cache-Control': 'no-store'
    });
    respuesta.end(pagina);
    return;
  }

  if (peticion.method === 'GET' && ruta === '/health') {
    enviarJson(respuesta, 200, { estado: 'ok' });
    return;
  }

  if (peticion.method === 'POST' && ruta === '/api/sumar') {
    try {
      let cuerpo = '';
      for await (const fragmento of peticion) {
        cuerpo += fragmento;
        if (Buffer.byteLength(cuerpo) > 1024) {
          enviarJson(respuesta, 413, { error: 'Solicitud demasiado grande' });
          return;
        }
      }

      const datos = JSON.parse(cuerpo);
      if (!datos || typeof datos.a !== 'number' || typeof datos.b !== 'number' ||
          !Number.isFinite(datos.a) || !Number.isFinite(datos.b)) {
        enviarJson(respuesta, 400, { error: 'Introduce dos números válidos' });
        return;
      }

      const suma = datos.a + datos.b;
      if (!Number.isFinite(suma)) {
        enviarJson(respuesta, 400, { error: 'El resultado es demasiado grande' });
        return;
      }

      enviarJson(respuesta, 200, { suma: Number(suma.toPrecision(15)) });
    } catch {
      if (!respuesta.headersSent) {
        enviarJson(respuesta, 400, { error: 'Solicitud JSON inválida' });
      }
    }
    return;
  }

  enviarJson(respuesta, 404, { error: 'Ruta no encontrada' });
}

const servidor = http.createServer(manejarPeticion);

servidor.listen(puerto, '0.0.0.0', () => {
  console.log(`Servidor iniciado en el puerto ${puerto}`);
});

export { servidor, manejarPeticion };
