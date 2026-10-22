// Servidor de archivos estáticos para Azure App Service (Node.js 26).
// El frontend original HTML/CSS/JavaScript se conserva en /site.
// Sin dependencias npm ni configuración manual de arranque.
'use strict';
const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');

const webRoot = path.resolve(__dirname, 'site');
const port = Number(process.env.PORT || process.env.WEBSITES_PORT || 8080);
const mime = {
  '.html':'text/html; charset=utf-8',
  '.css':'text/css; charset=utf-8',
  '.js':'text/javascript; charset=utf-8',
  '.mjs':'text/javascript; charset=utf-8',
  '.json':'application/json; charset=utf-8',
  '.wasm':'application/wasm',
  '.glb':'model/gltf-binary',
  '.gltf':'model/gltf+json',
  '.png':'image/png',
  '.jpg':'image/jpeg',
  '.jpeg':'image/jpeg',
  '.gif':'image/gif',
  '.webp':'image/webp',
  '.svg':'image/svg+xml',
  '.ico':'image/x-icon',
  '.woff':'font/woff',
  '.woff2':'font/woff2',
  '.ttf':'font/ttf',
  '.pdf':'application/pdf',
  '.txt':'text/plain; charset=utf-8'
};

http.createServer((req, res) => {
  if (req.method !== 'GET' && req.method !== 'HEAD') {
    res.writeHead(405, {'Allow':'GET, HEAD'});
    return res.end();
  }
  let relative;
  try {
    relative = decodeURIComponent(new URL(req.url, 'http://localhost').pathname);
  } catch {
    res.writeHead(400);
    return res.end('Solicitud inválida');
  }
  if (relative === '/') relative = '/index.html';
  // La URL sólo puede leer archivos dentro de la carpeta pública /site.
  const target = path.resolve(webRoot, '.' + relative);
  if (target !== webRoot && !target.startsWith(webRoot + path.sep)) {
    res.writeHead(403);
    return res.end('Acceso denegado');
  }
  fs.stat(target, (err, stat) => {
    if (err || !stat.isFile()) {
      res.writeHead(404, {'Content-Type':'text/plain; charset=utf-8'});
      return res.end('Archivo no encontrado');
    }
    res.writeHead(200, {
      'Content-Type': mime[path.extname(target).toLowerCase()] || 'application/octet-stream',
      'Content-Length': stat.size,
      'X-Content-Type-Options':'nosniff'
    });
    if (req.method === 'HEAD') return res.end();
    const stream = fs.createReadStream(target);
    stream.on('error', () => res.destroy());
    stream.pipe(res);
  });
}).listen(port, '0.0.0.0', () => {
  console.log(`Tutorial-Web-I disponible en puerto ${port}`);
});
