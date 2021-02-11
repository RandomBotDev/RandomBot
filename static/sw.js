var cacheVer = 'v1';
var cacheFiles = [
  '/',
  '/manifest.json',
  '/invite',
  '/support',
  '/perms-invite',
  '/static/styles/buttons.css',
  '/favicon.ico',
  '/apple-touch-icon.png'
];

self.addEventListener('install', (e) => {
  e.waitUntil(
    caches.open(cacheVer).then((cache) => {
      return cache.addAll(cacheFiles);
    })
  );
});

self.addEventListener('fetch', (e) => {
  e.respondWith(
    caches.match(e.request).then((r) => {
      return r || fetch(e.request).then((response) => {
        return caches.open(cacheVer).then((cache) => {
          cache.put(e.request, response.clone());
          return response;
        });
      });
    })
  );
});

self.addEventListener('activate', (e) => {
  e.waitUntil(
    caches.keys().then((keyList) => {
      return Promise.all(keyList.map((key) => {
        if(key !== cacheVer) {
          return caches.delete(key);
        }
      }));
    })
  );
});