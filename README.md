# What is ToolKit-Car?
***This is a hardware project from the StarDance challenge by Hack club.(https://stardance.hackclub.com/projects/52883)***

I've always loved to build things, from desks to computers, to everything in between. One thing that you will always need when building something are tools. Tools can often get lost or misplaced, even in a small workspace! I have experienced this one too many times, so I decided to build something to fix that! 
Toolkit car is able to track anyone within a room using a USB webcam and an raspberry pi 4 model b. The raspberry pi takes the data from the camera, and using a YOLO python script will send commands to 4 motors and allow it to move!

## Why did you make ToolKit-Car?

I have a very cluttered workspace, and constantly have to move stuff around just so I can have what I need for the many different projects I'm working on. This however results in me losing so much stuff, especially my tools, I once forgot where I put my soldering iron and could not find it for 3 days. ToolKit-Car was built to help at least fix that aspect of my life by being able to hold my tools for me, and bring them to me just to make sure I don't spend 30 minutes looking for a tape measure and not being able to find and then going all over the house to find it, and then walking back to my room in defeat just to see it lying on my bed(its personal). I thought to myself one day that I really needed a project like this, and I decided to build it.

## Current Progress!
- [x] All CAD and Design
- [ ] Assembly
- [ ] 3-D printing
- [ ] StarDance funding
- [X] Firmware
      
***View project here for more frequent updates:https://stardance.hackclub.com/projects/52883***

## How to print it?
*Please only download the most recent version of the .step files (currently V3)*
| CAD files | Do I print it? |
| -------- | ------- |
| Concept.step| *No* |
| Casing and wheel part studio.step | *No* |
| raspberry pi casing printing assembly.step | *No* |
| Rail part studio.step| *No* |
| Wheel printing assembly.step| *No*|
| Raspberry pi 4 Model B.step| *No*|
| L298N Driver.step| *No*|
| **raspberry pi casing printing.step** | **Yes** |
| **Wheel printing.step**| **Yes** |
 |**Rail printing assembly.step**| **Yes** |

| CAD files | What type of filament do I use? |
| -------- | ------- |
| raspberry pi casing printingV2.step | **PET-G*** |
| Rail printing assembly.step| **PET-G*** |
| Wheel printing.step| TPU |

_*PET-G can be replaced with other filaments. **PET-G is recommended**._


### Printing/Slicing Steps!
1. Download the .step files listed above.
2. Import the files into a slicer
3. Auto orient the files to the plate and ensure none are touching
4. Under supports select **organic tree supports**
5. Select slice and send to printer 
6. Glue the build plate using whatever glue is available.
7. Print each of the assemblies separately, or together.

_*Creality: https://wiki.creality.com/en/software/update-released/Support/support-settings_

_*Bambu:  https://wiki.bambulab.com/en/software/bambu-studio/support_
 
_*Cura: https://ultimaker.com/learn/tree-supports-what-are-they-and-how-do-they-work/_
   
_*Prusa: https://help.prusa3d.com/article/tree-supports_1515_
   
**The printing is now done!**

## Assembly
- [ ] Assembly steps finished!
- [ ] Assembly in README finished!
      
***(Will update when assembly IRL is finished)***

## Firmware!
*As of 9/29/2026, the firmware draft has been completed but not yet tested or adjusted for the actual ToolKit Car*
1. Download the latest firmware files
2. Upload the firmware files to a USB thumb drive/SD card or equivalent
3. Flash the firmware to the raspberry pi

- [ ] Firmware finalized!

***(Will update when firmware coding is finished)***

## Concept and Design
The images below show the concepts of **ToolKit Car**. This can help with **Assembly** later on!

*These concepts are the original ones, there are more updated versions of the concepts. **They are only concepts it does not matter if you have the latest one***

<img width="1959" height="583" alt="Screenshot_20260830_202002" src="https://github.com/user-attachments/assets/2de86980-265b-4238-a2cc-437a3d7fb238" />
Above is the main concept design of **ToolKit Car**. This is what you can see assembled in **Concept.step** *(open the file for more angles of the concept)*. This is what an assembled **ToolKit Car** should resemble! 
<img width="2376" height="1374" alt="Screenshot_20260830_175007" src="https://github.com/user-attachments/assets/eed695c9-d571-4851-aa00-76e55c848dd0" />
Above is the bottom angle of the main concept design. 
<img width="1959" height="583" alt="Screenshot_20260830_202002" src="https://github.com/user-attachments/assets/42ac3c0f-d1d1-4718-9432-80e61b2bdee1" />
Above is, again, the main concept design of **ToolKit Car**. This one has more descriptors if you are ever confused on how **ToolKit Car** works!

# Credits:
## CAD
**These files are not mine!!!!! Please check out the original creators, they do a lot of great work!!!**
https://grabcad.com/library/raspberry-pi-4-with-powerpack-box-1 For raspberry pi 
https://grabcad.com/library/l298n-stepper-driver-1 For l298N



