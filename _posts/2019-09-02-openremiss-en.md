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
ref: openremiss
chat: 'dinriksdag'
lang: en
links:
- title: Chat about the project
  url: https://chat.civictech.se/channel/dinriksdag
ingress-text: This project aims at obtaining data from the remissprocess (formal lobbying in the Swedish legislation process) and reusing it.
excerpt: Which organisations lobby your government the most?
image: "/uploads/openremiss.png"
contact:
- name: Pierre
  image: "/uploads/pierre.jpg"
  text:
  mail: pierre@digidemlab.org
  organisation:
  organisation-link:
---

OpenRemiss started at a Civic Tech hackathon in Göteborg in September 2018.

The goal is to look at the remiss process, by which the Swedish government gets feedback early on in the process of creating a new law. Government agencies, municipalities but also branch organisations, private companies and any other kind of lobby (including individual citizens) can leave a comment and some of them are contacted by the government to do so. It's a crucial step because it could be considered as the main official lobbying step of the whole process.

Until recently, the government has been storing these documents on paper in its archive rooms (even though it receives them on PDF since 2010), making them virtually unexploitable due to the high cost barrier of an FOIA request (I got a first estimate of at least 600 000kr) and the resources needed to scan them.

Part of these documents are now available on its website, [regeringen.se](regeringen.se/remisser), but the lack of a working search engine, of a proper structure and of any kind of API or open data, still makes it hard to use them.
Our work consisted in writing a Python script that downloads all the documents and sorts them. The output, although imperfect, allows anyone to browse through the document in an easier way, and to see some statistics around the process.

You can read more about the project on its [Github page](github.com/DinRiksdag/OpenRemiss).

Right now, a few examples of what could still be done:
*	improve the sorting and the name cleaning algorithm
*	use OCR to extract the content of some of the remiss lists where the text can't be parsed
*	extract the content of the remiss answers themselves, with OCR when necessary

There is a lot more that could be done with the data, which we are making available freely.

You only need basic programming skills to be able to join this project. We use Python for the script, a simple language commonly used in data science so it can also be a good way to start!
