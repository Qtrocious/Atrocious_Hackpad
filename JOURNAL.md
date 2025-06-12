|title |	author	|description	|created_at|
|:--------:|:------:|:--------:|:-----:|
|Atrocious_Hackpad | [@Qtrocious](https://github.com/qtrocious/)| A 9 key macropad with a rotary encoder, 9 sk6812 leds and a oled display |2024-05-28|

Total time spent: 38 hours

> So for clarification, didn't realized i needed to journal for a starter project (dumb from my part ik) but thankfully (and luckily) i did have a local repo that i had from the beginning, i'll attach an screenshot to each day that i commit something TT

![Clarification](https://github.com/user-attachments/assets/f3a44ea1-a1bb-42a6-b7ed-e7e84d66de7a)

# May 28 :suspect:

![image](https://github.com/user-attachments/assets/ec16d681-52de-4e49-bfe7-219c1d75327b)

After doing Solder, i thought that i could do the hackpad YSWS. 
I didn't do the tutorial first, i just kinda based what i did from there. So here it goes:

For a long time i wanted to mess around with a display so this was the perfect opportunity. I wanted to use all the 16 keyswitches, without thinking on how it would be placed on the pcb.
 
Then, i realized, i didn't want to make it big or sort of medium sized. I wanted it to be small, compact, not taking too much space from my desk.

So i ended up with the choice of using 9 keyswitches for the hackpad, an oled and also wanted to use the leds, just didn't know how to connect them.

Time Spent: 2.5 hours

# May 29 :suspect: 

![image](https://github.com/user-attachments/assets/e0bda97b-cc70-4fb1-8784-51049bbaf64b)

After skeeming through the hackpad channel, i learned how to connect the rotary encoder that i could do a matrix + connecting the leds in series so i didn't use all of the gpios, that i could use global labels in kicad so i didn't need to connect them directly. 
> WHAT, THAT'S GENIUS :interrobang:

Also included the rotary encoder and oled display. Ended up with a :goat: ed schematic 

![Og schematic OMFG1](https://github.com/user-attachments/assets/a22bb1dc-e41b-453e-a02c-d3d9dbd67aac)

Time Spent: 3 hours

# May 31 :suspect:
![image](https://github.com/user-attachments/assets/96d88486-3488-4c7d-be92-c975fbbbbed6)
> night owl :sigma_male:

With the schematic done, i placed the components to the pcb tab to resemble a macropad.

I didn't really sketch or made a certain design for the pcb, so i just went with it and kinda liked it!

Learned from Solder and did some rounded corners, might have over did it tho. 

Finished for the day by starting to trace the connections, although i didn't want to use a lot of vias, this took a lot of time and it was super late so i left it mid tracing 

![Image](https://github.com/user-attachments/assets/2b927449-3060-4b66-b522-36f937bf438b)

Time spent: 5 hours

# June 1 :rage1:

![image](https://github.com/user-attachments/assets/35dee972-6b7b-40b4-a602-95c759c46063)

Sooo... i didn't like the shape after all, so i changed to have less rounded things, finally added some ground fills, looks so professional!

![3d view](https://github.com/user-attachments/assets/5ed2fc30-af99-4733-a80f-cb3a247a2f71)

Time Spent: 2 hours

# June 2 :rage3:

![image](https://github.com/user-attachments/assets/0a008192-195e-4420-b364-93b2509be42c)

Started to add silkscreen art, mainly to personalize my pcb further, i wanted to make it mine, to show what i liked, learned that i could draw on figma and export it as svg. 

I saw a super cool [silkscreen art](https://lh4.googleusercontent.com/proxy/1_U3g3KRv54jqYMfxqYlnqbbxwsGXWIzcXYJClNF3SlAx20Lz0C3ZUfjKaGJKFvePmdQwYVAVtmIgr0zbJFWp6T9adAC0VlgzglczDJyZidVwr7j) that i wanted to recreate since making Solder and discovered a nice little tool called [Ditherlicious](https://29a.ch/ditherlicious/), it let's you apply the same dither effect on images. 
> BTW this is NOT recommended, Kicad makes individual objects for each point, so avoid using multiple ones with the same effect

![Pcb with silkscreen](https://github.com/user-attachments/assets/9d508339-8553-4876-821f-0642abf6f152)

So of course i wanted to be happy and added this:
![image](https://github.com/user-attachments/assets/8c828172-e16d-4547-ad3a-bb708b5b6df3)

Time Spent: 4 hours

# June 5 :rage4:
I <sub>AGAIN</sub> changed the pcb outline, i wanted to fit the silkscreen art without having to worry about where to place it, so i just made the outline be a rectangle with rounded courners 

Pcb with new silkscreen art
![PCB SILKSCREEN FINAL DESIGN](https://github.com/user-attachments/assets/05aa8678-a5a9-4117-aa13-a69748bfeb05)

And also, found out you can actually add the rotary encoder to the matrix
![Correct schematic](https://github.com/user-attachments/assets/a807da63-1705-4cbb-9d20-446fa3f2e140)

Time Spent: 3.5 hours

# June 6 :rage4:
> I have a fusion version that goes from June 6, i imported the Orpheuspad on june 4 but since i didn't have anything else from that day i just went from june 6

![Fusion](https://github.com/user-attachments/assets/78b0a2bd-1338-4fe5-9008-2e61401904ab)

I started the design on Fusion by first doing the basic layout of the keys and making a basic case

![Basic 3d case](https://github.com/user-attachments/assets/b4673ae3-7d66-4b11-baa8-bd13695b6cc5)

But i didn't want to leave it at that, so, based on how Orpheuspad designed the heatset inserts and being slightly inclined, i decided i wanted to integrate that to my design.
> AND THAT WAS A PAIN IN THE BUTT! :hurtrealbad:

Time Spent: 3 hours

# June 7 :goberserk:
![fusion june 7](https://github.com/user-attachments/assets/4c1309b6-c5e5-4e6c-ab7b-d6803e7a451a)

By measuring the dimensions in kicad and looking at the examples of the key switch on the guide, i made the sketches in fusion and on a notebook to have both in digital and physical.

I needed to add the holes for the rotary encode and the oled so this are the sketches i made, to get the measurements just right.

I learned so much actually, it felt so amazing when i extruded a sketch and the cut or join action was right, so satisfying!

![Sketches](https://github.com/user-attachments/assets/fed6300a-4270-464c-a323-b988f5b21928)
> This sketches were made from june 7 to june 8
 
Time Spent: 4 hours

# June 8 Part 1 :goberserk:
![Fusion June 8 hours](https://github.com/user-attachments/assets/7a9c79b1-26ae-4eb3-8763-5d25c1976ea0)
> this is a late night session from june 7, night owl v2

So from the late night session i started to work on putting the holes for the oled and rotary encoder, added the mounting holes for the screws, also using the ones from the pcb.

![Fusion June 7](https://github.com/user-attachments/assets/69242558-b25e-41e1-ab46-3a624f509a07)

Time Spent: 2 hours

# June 8 Part 2 :finnadie:
![Fusion June 8 hours v2](https://github.com/user-attachments/assets/56f4920a-e1d0-4689-8a2b-4f5b7f36f9bf)

Wanted to make it fit perfectly, didn't want thin walls so the heatset inserts have enough to go around melting the 3d print

![Bad holes](https://github.com/user-attachments/assets/21e72f65-1234-438a-a1b5-c842c6cfb061)
> This was an awful experience, it was fun

So after a full afternoon of making the holes both for the screws and heatset inserts, i added the covers for the heatset insert holes, so they are not visible and they fit!
![They fit](https://github.com/user-attachments/assets/c7f42bb4-65ea-494f-a2fb-d61724fb60b6)

Time Spent: 5 hours 
# June 9 :feelsgood:
I've not been mentioning the bottom cover, the reason is it was an easier process, almost an immediate process 
![image](https://github.com/user-attachments/assets/3d0d3554-f821-4950-a786-c3c25a8bd064)
> The usb-c hole is in the wrong orientation lol, but i changed it later

I was finally finishing the top cover design, added some text, and made it so it looks not so plain
![Fusion June 9](https://github.com/user-attachments/assets/f7665dd8-fd60-4366-a9df-8afb29f49776)

That's also the case for the bottom cover, and if you see close enough, at the side of the usb c port, there's a support designed for the pcb due to only having 3 mounting holes, which would make it unstable, so that's the reason it's there.

![image](https://github.com/user-attachments/assets/9a4f422f-d834-4a1d-b368-cdb593ce103f)

And to finish it, the inclination that also function as the support for the macorpad!

![image](https://github.com/user-attachments/assets/38249e31-00b2-4378-94c6-d3c6c4819245)

I've added some text and as you see theres the holes for the screws and honestly, i'm really proud of this, i learned so much and this has only sparked a motivation in me to make more projects, thank you! 

Time Spent: 4 hours
# June 10 :godmode:

So this is the final design

![image](https://github.com/user-attachments/assets/a4ce9ea2-8c13-4922-a5bb-21f67e7e5db2)

I wanted to go with black on the top and inclined part because if it gets dirty it doesn't show as much, and the blue in the middle so it resembles Tron!

# June 12 :godmode:
Added some supports? Idk but i added this to make the assembly easier
![image](https://github.com/user-attachments/assets/1e51a3ce-09b3-4dbf-a8b3-09f24f095769)
![image](https://github.com/user-attachments/assets/21fdae0d-1658-4a25-b7a1-c9a0f014e53d)
![image](https://github.com/user-attachments/assets/ca84453f-f89d-4297-93c9-3ad4920f1dee)

Time Spent: 0.5 hours
![Video of the assembling](https://github.com/user-attachments/assets/44710b4c-f038-4628-ad3c-8864bbcb4045)
