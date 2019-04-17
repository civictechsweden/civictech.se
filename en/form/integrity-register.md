---
title: Register for meetup
excerpt: Integrity-hangout in Stockholm
ref: integrity-register
ingress-text: Integrity-hangout in Stockholm 24/3
form:
- id: namn
  title: Your name
  type: text
  required: required
- id: _replyto
  title: Your email
  required: required
  type: email
- id: phone
  title: Your phone number
  type: text
  required: required
  description: Only used to contact you if the event is cancelled in last minute
- id: interest
  title: What are you interested in doing  at the meetup?
  type: textarea
  description: You can always show up to see whats going on without a plan.
- id: allergies
  title: Allergies or food preferences
  type: text
- id: _subject
  value: Anmälan integritet
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
  title: Send
---
