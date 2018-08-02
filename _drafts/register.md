---
title: Anmälan till hackathon
date: 2018-08-02 10:15:12.410000000 +02:00
excerpt: Anmälan till hackathon
ref: register
layout: form
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
  title: Vad har du för kunskaper som du kan bidra med inom programmering, design,
    projektledning eller annat?
  required: required
- id: mat
  title: Maten blir vegetarisk, fyll i om du har allergier eller andra behov för maten
  type: text
- id: kurs
  title: Vill du vara med på en nybörjarkurs i programmering innan hackathonet?
  type: checkbox
  options:
  - option: 
    name: Ja
    id: ja
- id: _subject
  value: Anmälan till hackathon
  type: hidden
- id: _after
  value: http://digidemlab.org
  type: hidden
- id: _honeypot
  value: ''
  type: hidden
- id: send
  type: submit
  title: Skicka
---

Namn
E-post
Telefon
