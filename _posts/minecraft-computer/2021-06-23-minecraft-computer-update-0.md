---
layout: post
title: Minecraft Computer | Update 0
description: The core concept of my minecraft computer
tags: minecraft-computer
published: false
---
# Intro
I am working on making a working computer in vanilla minecraft that can be easily reprogramed.
This post is just about the concept of it.
I also want to make a compiler for it so you can easily write and run code for it.

# Memory
This computer will be fed operations from what I am going to call program memory which can only be read from.
It will have have another seperate memory, which I am going to call memory, which the computer can read and write to.
Both the memory and program memory will have a memory cursor. 
The program memory's cursor will move forward and read each cycle.
The memory's cursor will be controled by the program's operations and will not move each cycle.
Also, I am going to call the byte that the memory or program memory's cursor is on the current byte in memory or program memory.

# Operations
To start simple, the operations are going to be fed as 3 bit codes.
The codes will go as follows

> 000: Set Bit  
> 001: Invert Bit  
> 010: Equal  
> 011: Jump  
> 100: Move memory cursor forward  
> 101: Move memory cursor backward  

Both set and invert bit operate on the byte the memory's cursor is on.
Equal will check if the current byte in memory is equal to the next byte in program memory. If true, it will run the next command. If false, it will skip past that command
Jump will move the program memory by some amount

After I get a proof of concept version of thiss working I will add more operations, but that will come in a futre update.
