---
title: "Almedalsdata, diving into the data of the world’s biggest political festival"
date: 2021-08-03 17:10:47 +00:00
lang: en
ref: almedalsdata
author: "Pierre Mesure"
tags: ["democracy", "almedalen", "open-data", "sweden", "civictech"]
excerpt: "For those who don’t know about it, Almedalsveckan is a political festival taking place every year on the first week of July in Visby, a cute town on the island of Gotland."
image:
medium_url: https://medium.com/civictechsweden/almedalsdata-diving-into-the-data-of-the-worlds-biggest-political-festival-267eb6865860
medium_id: 267eb6865860
---

[Svensk version](/blog/almedalsdata-oppna-data-om-varldens-storsta-politiska-festival/)

For those who don’t know about it, Almedalsveckan is a political festival taking place every year on the first week of July in Visby, a cute town on the island of Gotland. It was initiated around 50 years ago by then education minister Olof Palme and has now grown to be what I believe is the biggest political festival in the world. Thousands of events, tens of thousands of attendees and about every important Swedish political or economical stakeholder!

![](https://cdn-images-1.medium.com/max/1024/1*HK8uBoJMxHsmRjSC2IzDCQ.jpeg)
*Annie Lööf holds her party speech at Almedalen on the 4th of July 2018 (CC-BY 4.0 Pierre Mesure)*

Ever since I arrived to Sweden, I’ve been fascinated by **Almedalsveckan**. I’ve been there every year up to the pandemic and it quickly became part of my Swedish summers. I can safely say it helped me a lot to understand the Swedish society, its political system and culture. I still remember how amazed I was the first year I attended. I could barely speak Swedish but I already managed to speak to two ministers and a few MPs (not sure they understood me 😁).

As my local network and my understanding of the system grew, I also learnt to see the dark side of this festival, how big corporate lobbying and money have become and how exclusive it is today. While there has been criticism about that worsening trend, I have yet to find some ambitious journalistic or research work about lobbying (completely possible that I missed it, please send your book/article tips!).

### The festival program

![](https://cdn-images-1.medium.com/max/1024/1*3g8quSm_6pLAU3kycwxFkA.jpeg)
*Programs from 2017 and 2018 (CC-BY 4.0 Pierre Mesure)*

One object that always fascinated me is that thick program that you get handed when you exit the boat and enter Visby’s city center for the first time. A long list of all the events (actually, all the public events but it took me some time to understand it) that I had to religiously browse to make my own list.

Could that program be a good starting material to understand what interests have come and passed in the public debate? To evaluate the growing influence of private interests on Swedish politics?

Although the book itself is freely distributed and the [website](https://program.almedalsveckan.info) is public, all of these questions were hard to answer. As usual in Sweden, structured data of really good quality exists but the idea of making it available as open data is quite remote… That’s why I decided to have a closer look and today I present to you…

### Almedalsdata

Almedalsdata is a small civic tech project I worked with on my free time. The first step was to find as much of the programs as I could online. The second was to write a small script to fetch that data and convert it to a structured format.

The result is available on Github [here](https://github.com/civictechsweden/almedalsdata).

#### What data is available?

As of now, I managed to gather **all events from 2009 to 2021**.

For each event, the title, organiser, speakers, description, dates, address, category and a few more metadata are saved.

I’m probably going to add the years 2003 to 2008 soon but I only found event lists without much information about them. Nothing earlier than 2003. Don’t hesitate to contact me if you know about sources that I haven’t found.

#### What can be found in the data?

A lot, but I haven’t had time to dig yet. This dataset could for example be used to trace the career of some politicians. Have a look at **Nooshi Dadgostar** for example:

- 2016: [Bostadspolitisk talesperson, (V)](https://program.almedalsveckan.info/event/user-view/42157)
- 2018: [Vice ordförande, Vänsterpartiet](https://program.almedalsveckan.info/event/user-view/51842)
- 2021: [Partiledare, Vänsterpartiet](https://program.almedalsveckan.info/event/user-view/60998)

In the same spirit, it could also help to identify some revolving doors:

- 2016: [sektionschef för Center för e-samhället, SKL](https://program.almedalsveckan.info/event/user-view/42241)
- 2018: [CDO of Sweden](https://program.almedalsveckan.info/event/user-view/50206)
- 2019: [Förbundsdirektör, IT&Telekomföretagen](https://program.almedalsveckan.info/event/user-view/59563)

For now, I’ve only gathered a few interesting statistics such as the amount of events per year:

![](https://cdn-images-1.medium.com/max/1024/1*q5ha6veqX5dl-sQy3J5yQw.png)
*Number of events per year (CC-BY 4.0 Pierre Mesure)*

After a stable growth over the past ten years, culminating in the 50th anniversary of the festival (and election year), Almedalsveckan was simply cancelled in 2020 before reappearing in a much humbler digital 2021 edition.

The 10 most active organisers and the 10 most popular event categories:

![](https://cdn-images-1.medium.com/max/1024/1*ubKEwkEh3D__rjw2oEAAbw.png)
*Number of event per organiser and per category, top 10 (CC-BY 4.0 Pierre Mesure)*

And finally, maybe the one piece of information you couldn’t live without!? The proportion of events offering food to attendees, available since 2011!

![](https://cdn-images-1.medium.com/max/1024/1*n8kR41tGuISEuluGKt4mNw.png)
*Proportion of events offering food per year (CC-BY 4.0 Pierre Mesure)*

The amount of events locking people with a free breakfast/fika seems to be steadily decreasing since the beginning of the 2010s. The first pandemic Almedalsveckan reaches a bottom of only 4 events with food in 2021.

![](https://cdn-images-1.medium.com/max/1024/1*eI6TqmjSaUuxJze3oJ3rNw.jpeg)
*Wraps that will soon be eaten, Almedalsveckan 2017 (CC-BY 4.0 Pierre Mesure)*

### Now, your turn!

What will you find in this data? It’s all yours to [explore](https://flatgithub.com/civictechsweden/almedalsdata?filename=summary.csv) and [reuse](https://github.com/civictechsweden/almedalsdata)! Please mention the project if you do! And don’t hesitate to contribute if you know where to find more data!
