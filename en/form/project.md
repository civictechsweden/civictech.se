---
title: Apply with project
excerpt: Apply with your project for CivicTechSweden
ref: project-presentation
layout: form
ingress-text: Apply to be a part of CivicTechSweden's hackathons.
links:
  - title: Guidelines for projects
    url: /en/about/#guidelines
form:
- id: namn
  title: Your name
  type: text
  required: required
- id: organisation
  title: Organisation that you represent
  type: text
- id: _replyto
  title: Your email
  required: required
  type: email
- id: phone
  title: Your phone number
  type: text
  required: required
- id: projectName
  title: Name of the project
  type: text
  required: required
- id: projectTrack
  title: Which track suits your project best?
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
  title: Describe your project
  type: textarea
  required: required
- id: projectNeeds
  title: Which skills do you need for your project?
  type: textarea
- id: projectMaterial
  title: Do you need to borrow equipment?
  description: Material och programs, besides the laptops that the participants will bring.
  type: text
- id: projectLeader
  title: Tell us a little bit about yourself
  type: textarea
- id: file
  title: Logo or image for the project
  type: file
- id: _subject
  value: Anmälan av projekt
  type: hidden
- id: _after
  value: http://civictech.se/en
  type: hidden
- id: redirect_to
  value: http://civictech.se/en
  type: hidden
- id: _honeypot
  value: ''
  type: hidden
- id: send
  type: submit
  title: Send
---
