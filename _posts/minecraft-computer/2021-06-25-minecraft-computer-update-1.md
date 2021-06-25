---
layout: post
title: Minecraft Computer | Update 1
description: Basics of how my minecraft computer will work
tags: minecraft-computer
---
# Intro
This is the first *real* update on my minecraft computer.
This update is going to be about how the computer will work in minecraft and some updates to the operations.

# How will it work
Other people have made computers in minecraft before using redstone.
I have tried making a redstone computer before but it's just not somthing I can do right now.
I just need to research more on how that would work, but I think i'll try to do that in the future.
So instead of using redstone, I opted to use commands.
I know it's not the same as redstone or as "low level", but it's still a computer.
I started using command blocks but now I am going to make it work in a datapack, so it works on any world.

# The actual computer
Here is a picture of the command block version of the computer.
![command block computer](http://www.sevenbitscience.com/assets/images/minecraft-computer-command-block-based.png)
The memory is on the right, with program memory on the bottom and memory on top.
Then the first line of command blocks next to that is to reset the computer.
The next line of command blocks reads a from program memory.
It reads using that armor stand that is on the program memory.
The big collection of command blocks runs the operation read from program memory.

# Operations
I added some commands to the computer. The updated list of commands is as follows

> 000: Set Bit  
> 001: Invert Bit  
> 010: Jump forward 
> 011: Jump backward
> 100: Move memory cursor forward  
> 101: Move memory cursor backward  
> 110: Equal

The jump commands jump the program memory cursor. 
I seperated them into forward and backward as it makes it easier to tell the computer what direction to jump.