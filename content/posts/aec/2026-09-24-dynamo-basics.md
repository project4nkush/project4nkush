---

title: Visual Programming with Dynamo

date: 2026-09-24

category: aec

tags: [dynamo]

excerpt: Understanding visual programming, dynamo and its user interface

---

## Why learn Dynamo?
I recently joined a MNC and was briefed about the projects that the BIM team is currently working on. On of it was a tunnel modelling project, where the team had to model the tunnel wall and the services (Civil, MEP) in Revit. The task was relatively easy, the services were in a group of families that the team simply had to copy and align with the tunnel wall axes. I quickly learned that the task is incredibly repetitive in nature, so I decided to take a look into copying elements in array along a path, but soon realised Revit simply doesn't have that option. The logic is sound, but the tool is missing, so I took a look at Dynamo and thus began the journey of satisfying my endless curiosity.



## Visual Programming

### Back Story

I wanted to help my team somehow, so, after exploring the YouTube tutorials like [this](https://www.youtube.com/watch?v=i7QRdJ9Qwhs), and asking Claude and Gemini to understand scripting using Dynamo for this specific problem, I learned that it was entirely possible, but I would have to start from the basics. Why not? I love programming so, this could be a great opportunity to learn automation and help my team simultaneously. This is when I came across an great resource called [The Dynamo Primer](https://primer.dynamobim.org/index.html), which is an introductory guide to "Visual Programming" using Dynamo.

This was the first time I learned about the term, "Visual Programming." After reading through the first chapter and understanding the example of origami crane, I realised the power of visual programming and the potential practical applications it holds for people who are not too deep into coding, but lean more towards, design.



## What is Visual Programming?

Visual Programming, as I understand it, is a method of programming, in which a set of instructions are placed in a logical format, called algorithm, in order to achieve a desired goal. While text based programming (like Python, C++ etc) require writing the code for the computer to understand and execute, visual programming languages, like Dynamo, Grasshopper, Scratch, relies on visual logic arrangement using nodes, blocks and flowcharts. Visual programming basically bridges the gap between "visualizing" the logic and coding. Just like textual code have code block, visual programs have nodes, for the most common use cases.

This concept opened up a whole different perspective of learning programming for me. Eager to discover more and hopefully create something useful.



## Dynamo

Dynamo is an open-source software, that is used to visually script behaviour and design logic, for processing data or generate and interact with geometry. For me, dynamo is a tool to fast track the modelling process in my BIM workflow. Download it [here](https://dynamobim.org/download/)



### Dynamo User Interface

Downloading and installing dynamo is the easy part, and I thought, like blender, it would have a complex UI that will take a long time to understand, but I was wrong. The UI is as simplistic as it can get. The standard - Menus, Toolbar; then a node library, workspace and execution bar. That's it. The Menus, Toolbar, Workspace and Execution bar were easy to understand so I skimmed through them. What I found interesting was the Library.



### Library

Dynamo library is a neatly arranged list of Nodes (default as well as ones loaded from Revit), that is firstly, organized in a hierarchy with Libraries -> Categories -> Sub-Categories (where needed), based on whether the nodes CREATE, execute an ACTION or is used to QUERY data.

I particularly find the part that a node can be categorized whether it creates a geometry, performs an action or extracts data. It simplifies the process significantly. Whenever a flow of logic is to be determined, I simply would have to contemplate on these three. This also opened up my mind a little.



## Final thoughts for the day

Learning Dynamo is a step I took of my own accord in order to help out my team members. I only realised how interesting this topic actually is after I made my first circle using nodes. I have wanted to learn programming and now I can do it while helping others. Thanks Dynamo team.

