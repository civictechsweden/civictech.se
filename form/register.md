---
title: Projektstart - presentation till hemsidan
excerpt: Presentationsformulär för nya projekt.
ref: project-start
layout: form
ingress-text: Nu kör vi igång! Svara kortfattat på de här frågorna för att presentera
  ditt projekt på digidemlab.org, skriv två till tre meningar på varje fråga. Under
  projektets gång kan du bygga på presentationen genom att skicka bilder, videor och
  annat till <a href="mailto:petter@digidemlab.org">petter@digidemlab.org</a>.
form:
- id: namn
  title: Ditt namn
  type: text
  required: required
- id: _replyto
  title: Din mailadress
  required: required
  type: email
- id: projectName
  title: Vad vill du kalla ditt projekt?
  description: Något kort och kärnfullt!
- id: projectDate
  title: Vilket datum vill du börja?
  description: Projektet kommer att hålla på i tre månader från det datumet.
- id: projectDesc
  title: Vad kommer du göra under projektperioden?
  description: Två till tre meningar.
  type: textarea
- id: projectResult
  title: Vad hoppas du det ger för resultat?
  type: textarea
  description: Två till tre meningar.
- id: projectLeader
  title: Berätta om dig själv...
  type: textarea
  description: Två till tre meningar.
- id: file
  title: "... och skicka med en bild på dig själv!"
  type: file
- id: _subject
  value: Start på projekt
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

