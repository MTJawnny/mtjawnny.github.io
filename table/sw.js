/* MTJawnny Tablekeep — offline cache.
   Stale-while-revalidate: serve from cache instantly, refresh in the
   background. Covers the page itself plus the Google Fonts CSS/woff2,
   so the tracker works with zero signal once it's been opened once. */
const CACHE = 'mtj-tablekeep-v3';

self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', e => {
  // Bump CACHE (above) whenever a same-origin asset changes and old
  // clients need to stop serving their stale cached copy -- opening a
  // new cache store means old entries won't be found by cache.match(),
  // and this sweep drops the old store instead of leaving it dangling.
  e.waitUntil(
    Promise.all([
      self.clients.claim(),
      caches.keys().then(keys =>
        Promise.all(keys.filter(k => k !== CACHE && k.startsWith('mtj-tablekeep-')).map(k => caches.delete(k)))
      )
    ])
  );
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);
  const cacheable =
    url.origin === self.location.origin ||
    url.hostname === 'fonts.googleapis.com' ||
    url.hostname === 'fonts.gstatic.com';
  if (!cacheable) return;

  e.respondWith(
    caches.open(CACHE).then(async cache => {
      const hit = await cache.match(req);
      const refresh = fetch(req)
        .then(res => {
          if (res && res.ok) cache.put(req, res.clone());
          return res;
        })
        .catch(() => hit); // offline: fall back to whatever we have
      return hit || refresh;
    })
  );
});
