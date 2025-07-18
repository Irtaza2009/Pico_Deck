---
title: "Pico Deck"
author: "@Irtaza"
description: "A small flash drive, but with buttons (for shortcuts) and LEDs instead of storage!! With a custom RP2040 devboard!"
created_at: "2025-07-11"
---

## July 11th: Completed Schematic + PCB design!

Started out by researching some **RP2040 devboard guides**. Like this [one](https://www.circuitstate.com/projects/mitayi-pico-rp2040-r0-5-open-source-microcontroller-development-board-schematic-pcb-and-assembly/)!

I decided to give **EasyEDA Pro** for the first time for this project! Usually, I use **KiCAD**!

Then I looked at different schematics and completed the RP2040 devboard part of my schematic! Instead of a USB-C or microUSB female port, I instead used a **USB-A port** with the RP2040, because that fulfils my purpose! All of the components I used are SMD! For the flash, I used **128Mbit W25Q128JWPIQ**. And the 3.3V voltage regulator I used was the **AMS1117-3.3**! 

After the devboard was completed, I added **4 tactile switches**. They will serve as the _keys_! And for the lights, at first I was going for normal LEDs, but then realised I could use something like the **WS2812B** for _cool animations_ or _effects_, so I went with those! WS2812B operate at 3.7-5.3V, so I powered them directly from the USB_VBUS instead of the RP2040. I added _8 WS2812B_, and they can _all be controlled by a single RP2040 GPIO pin!_ Their main advantage is that they can be chained, and then the Neopixel library can be used for easy programming!

After that, I went to the PCB tab, updated all the components, and placed them in a nice layout. I tried to place all the components close that I had read online had to be placed close to a part. I placed all the resistors, capacitors, and every component except for the WS2812B and buttons on the bottom layer, and the buttons and the WS2812B on the top layer! Then I made a nicely styled outline for the board! Now the only thing left is **routing** (_auto-routing isn't working, I might have to rearrange some components_)!
<details>
<summary>
<b>Schematic:</b>
</summary>
<p>
<img width="1270" height="845" alt="SCH_PicoDeck" src="https://github.com/user-attachments/assets/0c2830c6-63a5-40bb-8342-2a6d0d806cb0" />
</p>
</details>

<details>
<summary>
<b>PCB:</b>
</summary>
<p>
<img width="577" height="261" alt="PicoDeck_PCB_Top_Layer" src="https://github.com/user-attachments/assets/6bec8981-3f14-45aa-afb7-95b1a9682bc0" align="center" /><img width="577" height="265" alt="PicoDeck_PCB_Bottom_Layer" src="https://github.com/user-attachments/assets/ff957ce5-2337-4ae7-b291-a8ef9c178cd4" align="center"/>
</p>
</details>

**Total time spent: 7 hours**

## July 12th: Finished Schematic + PCB design and Firmware!

I started off by moving around some components and then autorouting again. It did not work. I had to move around components, change the board outline, and manually route some components myself. After 8 tries, auto-routing finally managed to route everything except for 2 pads, which I manually routed. All of this auto routing took a lot of time (>5-10minutes every time), so I also started working on the firmware side-by-side!

I used CircuitPython for the firmware because I have used it for past projects like [Hackamon](https://github.com/Irtaza2009/Hackamon).

I had 4 buttons, and using the adafruit_hid library, I mapped the buttons to copy, paste, undo, and redo! Then I used the neopixel library to make some animations using the WS2812Bs!! At boot, the LEDs will light up a red-to-green gradient left to right, and then turn green! And upon any button press, they will play a blue wipe animation, and then return to green!

Once the basic firmware was done, I went back to my PCB and made a new, improved outline and made sure it was symmetrical! Finally, I used [this checklist](https://libsharedobject.so/howsmypcb.html) to make sure my PCB was alright, and it was not :(. I was using vias on the USB data lines, and also, the data lines were not of equal length. So I removed all the routes, did the USB data line manually, and then auto-routed again! This time, it left 6 pins un-routed, which I had to move components, traces, etc., to fix. But finally, I got 0 errors on the DRC! I added ground planes on both layers for good measure, and finally, my PCB design was finished! 

Then I posted the Schematic and PCB design on [r/PrintedCircuitBoard](https://www.reddit.com/r/PrintedCircuitBoard/) for a review!

<details>
<summary>
<b>Schematic:</b>
</summary>
<p>
<img width="1270" height="845" alt="SCH_PicoDeck_1_1-P1_2025-07-13 (2)" src="https://github.com/user-attachments/assets/c82fc493-f542-48d3-96d9-278cfa199211" />
</p>
</details>

<details>
<summary>
<b>PCB:</b>
</summary>
<p>
<img width="714" height="335" alt="PCB Top Layer" src="https://github.com/user-attachments/assets/773044ff-69c9-4aab-93c3-642981f49cec" align="center"/>
<img width="714" height="335" alt="PCB Bottom Layer" src="https://github.com/user-attachments/assets/c9127008-7c07-4917-80c3-e31240565601" align="center"/>
</p>
</details>

**Total time spent: 6 hours**

## July 13th: Review + Schematic and PCB Changes 

I received some valuable feedback from my Reddit post, which made me change the voltage regulator from the AMS1117-3.3 to the AP2112K-3.3. I also fixed several pins on the schematic and added more vias to the ground planes. I attempted to switch to a four-layer design but found the routing to be challenging, so I decided to revert to two layers. I believe the PCB can be finalised now!

**Total time spent: 2 hours**

## July 17th: 3D Case

I finally remembered to charge my Apple Pencil and reinstall Shapr3D, so I started working on the case. First, I imported the 3D model of the PCB from EasyEDA. Then, I sketched an outline around it, offset it, and extruded the shape. After that, I created the sides and the top plate. 

Next, I added two holes on the bottom side for the boot and reset buttons, along with four holes on the top side for the other buttons. I also included a large rectangle for the debugging headers and a line for the LEDs. To enhance stability, I added spacers to both the bottom and top pieces. Finally, I filleted the edges to give the design a more professional look!

I exported the models as .3mf, because .step is only for the PRO version!

<img width="1000" height="1000" alt="3D Case Top" src="https://github.com/user-attachments/assets/b275727e-d42c-4a0a-9928-67f35f761e7c" />
<img width="1000" height="1000" alt="3D Case Bottom" src="https://github.com/user-attachments/assets/619b6c87-6cf4-4fbf-9642-200cebef4399" />

**Total time spent: 2.5 hours**
