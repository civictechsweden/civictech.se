---
title: Ansök med projekt
excerpt: Ansök med projekt till CivicTechSweden
ref: project-presentation
layout: form
ingress-text: Ansök här för att bli antagen till CivicTechSwedens hackathon.
links:
  - title: Riktlinjer för projekt
    url: /about/#riktlinjer
form:
- id: namn
  title: Ditt namn
  type: text
  required: required
- id: organisation
  title: Organisation som du representerar
  type: text
  description: Du kan också göra projekt som privatperson.
- id: _replyto
  title: Din mailadress
  required: required
  type: email
- id: phone
  title: Ditt telefonnummer
  type: text
  required: required
- id: projectName
  title: Projektets namn
  type: text
  required: required
- id: projectTrack
  title: Vilket spår passar ditt projekt in på?
  type: checkbox
  required: required
  options:
    - option:
      name: Sharing is caring
      id: sharing-is-caring
    - option:
      name: Power to the people
      id: power-to-the-people
    - option:
      name: I like to move it
      id: i-like-to-move-it
- id: projectDesc
  title: Beskriv ditt projekt i några meningar
  type: textarea
  required: required
- id: projectNeeds
  title: Vad behöver du för kompetens till ditt projekt?
  type: textarea
- id: projectMaterial
  title: Behöver du låna utrustning?
  description: Till exempel program eller material, förutom egna laptops?
  type: text
- id: projectLeader
  title: Berätta kort om dig själv
  type: textarea
- id: file
  title: Logotyp eller bild till projektet
  type: file
- id: _subject
  value: Anmälan av projekt
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
