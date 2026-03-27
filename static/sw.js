self.addEventListener("push", (event) => {
  let data = {};
  try {
    data = event.data ? event.data.json() : {};
  } catch (e) {}

  const title = data.title || "Sentiment ready ✅";
  const options = {
    body: data.body || "Your sentiment result is ready to view.",
    data: { url: data.url || "/sentiment_result" }
  };

  event.waitUntil(self.registration.showNotification(title, options));
});

self.addEventListener("notificationclick", (event) => {
  event.notification.close();
  const url = (event.notification.data && event.notification.data.url) || "/sentiment_result";
  event.waitUntil(clients.openWindow(url));
});
