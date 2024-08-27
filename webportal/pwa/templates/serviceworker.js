// Base Service Worker implementation.  To use your own Service Worker, set the PWA_SERVICE_WORKER_PATH variable in settings.py

var staticCacheName = "myProject" + new Date().getTime();
var filesToCache = [
    '/',
    '/news/overview',
    '/downloads/',
    '/terms-of-use/',
    '/impressum/',
    '/data-policy/',
    'https://unpkg.com/dexie@latest/dist/dexie.js',
    '/offline/overview',
    '/offline/category1interface',
    '/offline/category2interface',
    '/offline/category3interface',
    '/offline/category4interface',
    '/static/css/range.css',
    '/static/css/toggle-switchy.css',
    '/static/js/rangeslider.js',
    '/static/js/offline/observations/category1.js',
    '/static/js/offline/observations/category2.js',
    '/static/js/offline/observations/category3.js',
    '/static/js/offline/observations/category4.js',
    '/static/js/offline/csrftoken.js',
    '/static/js/offline/db_instance.js',
    '/static/js/offline/background_upload_download.js',
    '/static/js/offline/user.js',
    '/static/css/django-pwa-app.css',
    '/static/image/icons/icon-72x72.png',
    '/static/image/icons/icon-96x96.png',
    '/static/image/icons/icon-128x128.png',
    '/static/image/icons/icon-144x144.png',
    '/static/image/icons/icon-152x152.png',
    '/static/image/icons/icon-192x192.png',
    '/static/image/icons/icon-384x384.png',
    '/static/image/icons/icon-512x512.png',
    '/static/image/symbol_offline.svg',
];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("portal")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});

// Serve from Cache
self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                // when the app is online, the sites are fetched from the server
                if (navigator.onLine) {
                    console.log("Is online (fetching from server):");

                    return fetch(event.request)
                } else if (response) {
                    // else, the sites are fetches from the cache
                    console.log("Is offline (getting site from cache)");
                    console.log(response)
                    return response
                }
                return fetch(event.request);
            })
            .catch(() => {
                return caches.match('/offline/overview');
            })
    )
});


