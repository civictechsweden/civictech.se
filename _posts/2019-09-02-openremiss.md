---
title: OpenRemiss
date: 2019-09-02 01:00:00 +02:00
categories:
- open data
- democracy
- hackathon-2
tags:
- remiss
- legislation
- opendata
- datascience
chat: 'dinriksdag'
ref: openremiss
links:
- title: Chatta om projektet
  url: https://chat.civictech.se/channel/dinriksdag
- title:
  url:
ingress-text: Hämta och använda data från remissprocessen (lobbying i lagstiftningsprocessen).
excerpt: Vilka lobbar mest din regering?
image: "/uploads/openremiss.png"
contact:
- name: Pierre
  image: "/uploads/pierre.jpg"
  text:
  mail: pierre@digidemlab.org
  organisation:
  organisation-link:
---

OpenRemiss startades på ett Civic Tech hack i Göteborg i september 2018.

Målet är att titta på remissprocessen, där regeringen får tidig feedback i lagstiftningsprocessen. Myndigheter, kommuner men även branschorganisationer, privata företag och andra typer av lobby (inkluderande enskilda medborgare) kan lämna en kommentar och regeringen ber vissa av dem om att göra så. Det är ett viktigt steg eftersom det är det största officiella lobbyingssteg i processen.

Historiskt har regeringen sparat dessa dokument på papper i sina arkivsalar (trotts att den får dem på PDF sedan 2010), vilket gör dem omöjligt att uforskas på grund av höga kostnader (de bedömde den själv till minst 600 000kr) och resurser som skuller behövas för att skanna dem.

Nyligen började regeringen att publicera en del av dessa dokument på sin webbplats, [regeringen.se](regeringen.se/remisser), men utan en fungerande sökmotor, utan struktur och utan API eller öppna data, vilket gör det fortfarande svårt att använda dem.
Vårt arbete var att skapa ett Python skript som laddar ner alla dessa dokument och att sortera dem. Resultatet är fortfarande långt ifran perfekt men alla kan bläddra igenom dokumenten på ett enklare sätt och se statistik kring processen.

Man kan läsa mer om projektet på sitt [Githubs sida](https://github.com/DinRiksdag/OpenRemiss).

Just nu finns det fortfarande mycket att göra, t.ex.:
*	förbättra sorteringsalgoritmen och namnrensingsalgoritmen
*	använda OCR för att hämta innehållet av en del remissinstanser som har varit skannade
*	hämta innehåll från alla remissvar, med OCR när det behövs

Det finns såklart mycket mer man kan göra med datan och den är helt fri att använda!

Om du vill delta i projektet behöver du bara lite kunskap om programering. Vi använder Python, vilket är ett enkelt språk, och vanligt i datavetenskap så det kan också vara ett bra sätt att börja!
