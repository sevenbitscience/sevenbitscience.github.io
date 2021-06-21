---
layout: post
title: Trash Dash!
tags: python coding
---
# Intro
 Trash Dash is a game that I helped make about water pollution (kinda).
 I am being kinda brief about playing it and and stuff bc I already made a website for the game with more info on playing it and stuff [here is a link to it](https://trashdash.sevenbitscience.com).
 Anyways this is going to be a more behind the scenes and how it got made view of the project.

# Starting off in unity
 So I was initaly going to make the game using unity bc like "it wouldn't be that hard" and "I could get it done quickly" and even though i have used unity in the past, im not that good at it.
 Anyway so I started working in unity and I got it so the player could move and trash would fall down the river and it was going good.
 The next part was the ui and that is where i decided to just give up on unity bc
 I just didn't know how to do UI stuff in unity and I didn't realy want to figure it out and there were other things i didn't know how to do but I think mostly it was
 because i saw [this](https://www.youtube.com/watch?v=7tXsC8YlCq8) video about someone learning pygame for a game jam and I remembered that I have used pygame before
 and even made a terrible game with pygame before so i scraped all the unity stuff and started over. Another reason i switched because i use python so much more and i felt like
 i had more control with pygame. I also felt like there was just so much built in to unity that it was just hard to figure out how to start with ui and stuff.

# Rewrite the game
 So I re wrote the entire game with pygame, and although i hadn't gotten very far in the project, unity handles a lot for you and pygame doesn't.
 Pygame mostly just makes the window for the game and handles getting keyboard and mouse input. You have to handle everything else.
 Another downside of pygame is that it has to be run from a .py file, so you needed python to run the game.
 This was going to be a problem because i don't want people to have to install python and pygame when they download the game.
 It would also be a problem because the game was going to be distributed at my school and we can't install python or run command prompt (to install python) on the school computers.
 However, someone has made a python module to convert a python file to an executable, called [pyinstaller](https://www.pyinstaller.org/), and i thought that would work.

# Executable issues
 Anyways, I had gotten most of the game done and it was mostly playable so i decided to try to get it to run on another computer.
 I converted the code with to an exe with pyinstaller and added it as a pre-release on github and tried to download and run it.
 Here is where I realized the big issue with this method, when I tried to run the exe my antivirus immediately deleted it.
 What i think happened is that although did not contain a virus or anything harmful the antivirus wanted to be cautions and just deleted it.

# Rewriting the Rewrite
 Since the game would be hard to distribute as an exe i decided to, once again, rewrite the game.
 This time, I was going to use [skulpt](http://skulpt.org/) and [pygame4skulpt](https://github.com/Petlja/pygame4skulpt), pygame module for skulpt as skulpt uses modules written in javascript.
 Skulpt is a tool that allows you to run python code from a static website, meaning I could put the game on github pages and anyone could play it without downloading anything.
 However, because pygame4skulpt is like an unofficial port of pygame, and it is for a webpage, there is some functionality that was lacking, meaning i had to mostly rewrite the game again.
 So after a few more days, i had finally completed the game for the website.
 I then made a google site with info on playing the game ([link to that](https://trashdash.sevenbitscience.com)) and now i'd say that it is basically done.

[//]: # <iframe src="https://www.sevenbitscience.com/web-trash-dash" title="Trash Dash" height="645" width="1280"></iframe>
