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
