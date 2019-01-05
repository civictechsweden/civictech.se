---
title: Register for hackathon
excerpt: Registration for hackathon
ref: participant
layout: form
ingress-text: Register by the form below.
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
- id: sep
  title: Do you identify as woman or non-binary?
  type: radio
  required: required
  options:
  - option: 
    name: Yes
    id: ja
  - option: 
    name: No
    id: nej
- id: desc
  title: Tell us a little about yourself!
  type: textarea
  description: For example your areas of interest, what you can contribute with during the hack, your education or your work. If you have any specific skill or competence it's perfect to put here!
- id: mat
  title: Do you have any allergies or food preferences? 
  type: text
- id: project
  title: Which project/s are you interested in?
  type: checkbox
  required: required
  description: Information about <a href="/projects/mdgh-en"> Who owns the city? </a>, <a href="/projects/handlingar-en"> Documents </a> or <a href="/projects/mangfaldsdata-en"> Open diversity data </a>! 
  options:
  - option: 
    name: Who owns the city?
    id: vem-ager-staden
  - option: 
    name: Documents
    id: handlingar
  - option: 
    name: Open diveristy data
    id: oppnamangfaldsdata
- id: pre-meetup
  title: Do you want to participate in a pre-meetup? 
  type: radio
  description: To install software etc
  options:
  - option: 
    name: Yes
    id: ja
  - option: 
    name: No
    id: nej
- id: when
  title: If you want to come to the pre-meetup, which times work well for you?
  type: checkbox
  options:
  - option: 
    name: Daytime, monday-friday
    id: vardag-dag
  - option: 
    name: Evenings, monday-friday
    id: vardag-kvall
  - option: 
    name: Daytime, weekends
    id: helg-dag
  - option:
    name: Evenings, weekends
    id: helg-kvall
- id: needs
  title: Is there anything we can do to make you feel more comfortable before or during the event, or do you have any questions or wishes?  
  type: textarea
- id: fragar
  title: Is there anything specific you'd like to hear the presenters, Vanessa or Rebecca, talk about?
  type: textarea
- id: anvandare
  title: Whats your username in the civictech-chat?
  description: If you have a username and want to join the chat for the hackathon
- id: lat
  title: Write a song you like right now!
  type: text
-  id: var
   title: How did you hear about the hackathon?
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
  title: Send
---

