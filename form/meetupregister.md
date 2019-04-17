---
title: Anmäl dig till meetup
excerpt: Anmälan till Open Data Day i Uppsala
ref: meetupregister
ingress-text: Anmälan sker via formuläret nedan.
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
- id: organisation
  title: Din organisation
  type: text
  description: Privatpersoner är välkomna också!
- id: allergies
  title: Allergier/matpreferens
  type: text
- id: _subject
  value: Anmälan
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
