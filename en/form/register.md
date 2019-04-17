---
title: Register for hackathon
excerpt: Registration for hackathon
ref: participant
ingress-text: We have filled all the spots for the hackathon, but please register anyway and we will mail you if someone drops off. Register by the form below.
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
  description: Information about <a href="/projects/mdgh-en"> Who owns the city? </a>, <a href="/projects/handlingar-en"> Documents </a>, <a href="/projects/mangfaldsdata-en"> Open diversity data </a> or <a href="/projects/civilkurage-en"> Family dinner and courage</a>!
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
  - option:
    name: Family dinner and courage
    id: kurage
- id: pre-meetup
  title: Do you want to participate in a pre-meetup?
  type: radio
  description: To install software, set up projects locally etc
  options:
  - option:
    name: Yes
    id: ja
  - option:
    name: No
    id: nej
- id: needs
  title: Do you have any wishes or suggestions for the event, or any questions?  
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
