---
title: Anmäl dig till hackathonet
excerpt: Anmälan till hackathon
ref: participant
layout: form
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
- id: sep
  title: Identifierar du dig som kvinna eller icke-binär? 
  type: radio
  required: required
  options:
  - option: 
    name: Ja
    id: ja
    required: required
  - option: 
    name: Nej
    id: nej
- id: mat
  title: Har du några allergier eller matpreferenser?
  type: text
- id: project
  title: Vilket/vilka projekt är du intresserad av?
  type: checkbox
  required: required
  description: Läs mer om <a href="/projects/mdgh"> Vem äger staden </a>, <a href="/projects/handlingar"> Handlingar </a> eller  <a href="/projects/mangfaldsdata"> Öppna mångfaldsdata </a>! 
  options:
  - option: 
    name: Vem äger staden?
    id: vem-ager-staden
  - option: 
    name: Handlingar
    id: handlingar
  - option: 
    name: Öppna mångfaldsdata
    id: oppnamangfaldsdata
- id: pre-meetup
  title: Vill du delta i en förträff?
  type: radio
  required: required
  description: För att installera mjukvara etc
  options:
  - option: 
    name: Ja
    id: ja
  - option: 
    value: Nej
    id: nej
- id: when
  title: Om du vill delta på en förträff, när passar det dig bäst?
  type: checkbox
  options:
  - option: 
    name: Vardag, dagtid
    id: vardag-dag
  - option: 
    name: Vardag, kvällstid
    id: vardag-kvall
  - option: 
    name: Helg, dagtid
    id: helg-dag
  - option:
    name: Helg, kvällstid
    id: helg-kvall
- id: needs
  title: Finns det något vi kan göra för att det ska kännas mer bekvämt inför eventet eller under eventet för dig, eller har du några frågor eller önskemål?  
  type: textarea
- id: fragar
  title: Är det något du gärna vill höra presentatörerna, Vanessa eller Rebecca, prata extra om? 
  type: textarea
- id: anvandare
  title: Vad är ditt användarnamn på civictech-chatten?
  description: Om du har ett och vill vara med i chatten
- id: lat
  title: Skriv en låt du tycker är bra just nu! 
  type: text
- id: var
  title: Hur fick du höra om hacket?
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

