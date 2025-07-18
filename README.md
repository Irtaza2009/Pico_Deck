# Pico Deck + USB Rubber Ducky 

### **A flash-drive-sized USB macropad and rubber ducky!**  

A small **flash-drive** but with *__buttonnnnsssss for shortcuts__* instead of storage!! And with a _custom **rp2040** devboard!_
And _**LEDDDsss!**_
And it can _run different scripts_ on the computer it's plugged into, like a **USB rubber ducky**!

I created this to learn how to make a devboard, how hard it is, and what modifications can be applied to it!

## Preview

| Description           | Image                                                                                                                                  |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| PCB Top Layer         | ![](https://github.com/user-attachments/assets/773044ff-69c9-4aab-93c3-642981f49cec)                                                  |
| PCB Bottom Layer      | ![](https://github.com/user-attachments/assets/c9127008-7c07-4917-80c3-e31240565601)                                                  |
| PCB 3D Render Front   | ![](https://github.com/user-attachments/assets/d3730a47-ca12-4814-8c4c-6fdc7cbfad7d)                                                  |
| PCB 3D Render Back    | ![](https://github.com/user-attachments/assets/08fb3b45-b659-489f-8471-1a0725f66eb9)
| Schematic             | ![](https://github.com/user-attachments/assets/c16c6657-8c1c-4736-9c36-b4b51a29d4b7)                                                  |
| 3D Case Top           | ![](https://github.com/user-attachments/assets/b275727e-d42c-4a0a-9928-67f35f761e7c)                                                  |
| 3D Case Bottom        | ![](https://github.com/user-attachments/assets/619b6c87-6cf4-4fbf-9642-200cebef4399)                                                  |

## BOM

| Component Description              | Quantity | LCSC Part #     | Price (USD) | LCSC Link                                                                                                                        |
|-----------------------------------|----------|-----------------|-------------|----------------------------------------------------------------------------------------------------------------------------------|
| Tactile Switch SKRPACE010         | 1        | C139797         | 0.60        | [Link](https://lcsc.com/product-detail/Tactile-Switches_ALPSALPINE-SKRPACE010_C139797.html?s_z=n_C139797)                        |
| 100nF Ceramic Capacitor           | 20       | C14663          | 0.24        | [Link](https://lcsc.com/product-detail/Multilayer-Ceramic-Capacitors-MLCC-SMD-SMT_YAGEO-CC0603KRX7R9BB104_C14663.html)           |
| 10uF Ceramic Capacitor            | 2        | C19702          | 0.30        | [Link](https://lcsc.com/product-detail/Multilayer-Ceramic-Capacitors-MLCC-SMD-SMT_Samsung-Electro-Mechanics-CL10A106KP8NNNC_C19702.html) |
| 14pF Ceramic Capacitor            | 2        | C5360816        | 0.30        | [Link](https://lcsc.com/product-detail/Multilayer-Ceramic-Capacitors-MLCC-SMD-SMT_CCTC-TCC0603COG140J500CT_C5360816.html)        |
| WS2812B RGB LED (2020)            | 8        | C965555         | 4.00        | [Link](https://lcsc.com/product-detail/RGB-LEDs-Built-in-IC_Worldsemi-WS2812B-2020_C965555.html)                                 |
| 27Ω Resistor                      | 2        | C137753         | 0.12        | [Link](https://lcsc.com/product-detail/Chip-Resistor-Surface-Mount_YAGEO-RC0603FR-0727RL_C137753.html)                          |
| 10kΩ Resistor                     | 2        | C98220          | 0.11        | [Link](https://lcsc.com/product-detail/Chip-Resistor-Surface-Mount_YAGEO-RC0603FR-0710KL_C98220.html)                            |
| 1kΩ Resistor                      | 1        | C22548          | 0.11        | [Link](https://lcsc.com/product-detail/Chip-Resistor-Surface-Mount_YAGEO-RC0603FR-071KL_C22548.html)                             |
| Tactile Switch B3U-1000P          | 1        | C231329         | 2.00        | [Link](https://lcsc.com/product-detail/Tactile-Switches_OMRON-B3U-1000P_C231329.html)                                            |
| Tactile Switch TS-1002S-05026C    | 4        | C455110         | 1.00        | [Link](https://lcsc.com/product-detail/Tactile-Switches_XUNPU-TS-1002S-05026C_C455110.html)                                      |
| 4-pin Header B-2100S04P-A110      | 1        | C124378         | 0.41        | [Link](https://lcsc.com/product-detail/Pin-Headers_Ckmtw-Shenzhen-Cankemeng-B-2100S04P-A110_C124378.html)                        |
| RP2040 Microcontroller            | 1        | C2040           | 6.00        | [Link](https://lcsc.com/product-detail/Microcontrollers-MCU-MPU-SOC_Raspberry-Pi-RP2040_C2040.html)                              |
| LDO Regulator AP2112K-3.3TRG1     | 1        | C51118          | 1.00        | [Link](https://lcsc.com/product-detail/Voltage-Regulators-Linear-Low-Drop-Out-LDO-Regulators_DIODES-AP2112K-3-3TRG1_C51118.html) |
| Flash Memory W25Q128JWPIQ         | 1        | C2689660        | 5.80        | [Link](https://lcsc.com/product-detail/NOR-FLASH_Winbond-W25Q128JWPIQ_C2689660.html)                                             |
| USB-A Port AM90                   | 1        | C404965         | 0.62        | [Link](https://lcsc.com/product-detail/USB-Connectors_SHOU-HAN-AM90_C404965.html)                                                |
| 12MHz Crystal TAXM12M4RFBCCT2T    | 1        | C133337         | 0.51        | [Link](https://lcsc.com/product-detail/Crystals_Yajingxin-TAXM12M4RFBCCT2T_C133337.html)                                         |
| PCB                               | 5        | JLCPCB          | 2.00        | N/A                                         |
| PCBA                              | 5        | JLCPCB          | 130.00      | N/A                                         |
| Shipping                          | 5        | JLCPCB          | 32.00        | N/A                                         |


**PCBA is expensive:**

<img width="450" height="322" alt="image" src="https://github.com/user-attachments/assets/e9a807e3-ea0d-4074-bf27-4773b036660f" />

Subtotal (excluding PCBA): US$25

Estimated cost (PCBA, including parts and PCB): US$150 (with a coupon!)

