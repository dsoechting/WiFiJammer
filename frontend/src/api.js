import * as $ from 'jquery';

export function attack(apMac, clientMac, channel) {
  return $.get({
    url: 'http://localhost:5000/attack',
    data: {
      bssid: `${apMac}`,
      clientMac: `${clientMac}`,
      channel: `${channel}`
    }
  }).then((res) => {
    return JSON.parse(res);
  });
}

export function attackAll(apMac, channel) {
  return $.get({
    url: 'http://localhost:5000/attackAll',
    data: {
      bssid: `${apMac}`,
      channel: `${channel}`
    }
  }).then((res) => {
    return JSON.parse(res);
  });
}

export function search() {
  return $.get('http://localhost:5000/aps').then((res) => {
    return JSON.parse(res);
  });
}
