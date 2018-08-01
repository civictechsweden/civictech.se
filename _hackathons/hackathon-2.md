---
title: 'Hackathon #2'
ref: hackathon-2
image: "/uploads/hackathon-1.jpg"
excerpt: 'Hackathon #2 för Civic Tech-communitiet i Göteborg'
ingress-text: Välkommen till Göteborgs nya mötesplats för civic tech-communitiet!
event-date: 2018-09-02 01:00:00 +02:00
event-date-desc: 2 september 2018, kl 10 - 19
place: Viktoriahuset, Göteborg
links:
- title: Anmälan
  url: "/hackathon-2/#register"
  style: button
- title: Ansök med projekt
  url: "/form/project/"
form:
- id: namn
  title: Namn
  type: text
  required: required
- id: _replyto
  title: E-post
  required: required
  type: email
- id: telefon
  title: Telefonnummer
  type: text
- id: kunskaper
  title: Vad har du för kunskaper som du kan bidra med?
  description: Inom programmering, design, projektledning eller annat?
  required: required
- id: mat
  title: Maten blir vegetarisk, fyll i om du har allergier eller andra behov för maten
  type: text
- id: kurs
  type: checkbox
  options:
  - option: 
    name: Jag vill vara med på en nybörjarkurs i programmering innan hackathonet
    id: ja
- id: _subject
  value: Anmälan till hackathon
  type: hidden
- id: _after
  value: http://civictech.se
  type: hidden
- id: _honeypot
  value: ''
  type: hidden
- id: send
  type: submit
  title: Skicka
---

