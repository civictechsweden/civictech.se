---
title: Anmäl dig till meetup
excerpt: Koda med Civic Tech i Uppsala
ref: code-with-us-register
layout: form
ingress-text: Koda med oss i Uppsala den 21/3
form:
- id: namn
  title: Ditt namn
  type: text
  required: required
- id: _replyto
  title: Din mailadress
  required: required
  type: email
- id: phone
  title: Ditt telefonnummer
  type: text
  required: required
  description: Används endast för att kontakta dig om eventet tex ställs in på kort varsel.
- id: interest
  title: Vad är du intresserad av att göra på meetupen?   
  type: textarea
  description: Du kan även komma och se vad som händer utan en färdig plan!
- id: _subject
  value: Anmälan koda med oss
  type: hidden
- id: redirect_to
  value: http://civictech.se/tack/
  type: hidden
- id: _after
  value: http://civictech.se/
  type: hidden
- id: _honeypot
  value: ''
  type: hidden
- id: send
  type: submit
  title: Skicka
---

