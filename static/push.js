async function enablePushForSentiment() {
  if (!("serviceWorker" in navigator) || !("PushManager" in window)) return;

  // register service worker
  const reg = await navigator.serviceWorker.register("/sw.js");

  // ask permission
  const perm = await Notification.requestPermission();
  if (perm !== "granted") return;

  // fetch server public key
  const vapidKey = await fetch("/vapidPublicKey").then(r => r.text());

  // subscribe
  const sub = await reg.pushManager.subscribe({
    userVisibleOnly: true,
    applicationServerKey: urlBase64ToUint8Array(vapidKey),
  });

  // save subscription in server
  await fetch("/saveSubscription", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(sub),
  });
}

function urlBase64ToUint8Array(base64String) {
  const padding = "=".repeat((4 - (base64String.length % 4)) % 4);
  const base64 = (base64String + padding).replace(/-/g, "+").replace(/_/g, "/");
  const raw = atob(base64);
  const arr = new Uint8Array(raw.length);
  for (let i = 0; i < raw.length; i++) arr[i] = raw.charCodeAt(i);
  return arr;
}
