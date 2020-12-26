# Projects
All projects ever made by students of OIC.

# CIE Assembler
![view](https://github.com/CompSci-OIC/Projects/blob/master/CIE_Assembler/images/view.gif?raw=true)

*This software was entirely designed and developed by A-Levels students not as an assignment but just for experience. We will be happy to receive any suggestions about how to make things better :)

There was no way to run a made up assembly code from CIE Computer Science A-Levels so we decided to make a virtual machine that could interpret this specific assembly language. It can show how RAM and relevant registers are changing in real time.

Developers:
* Adi Bozzhanov
* Laveen Chandnani
* Martin Lee
* Tanthun Assawapitiyaporn

Project leader:
* Nicholas Mulvey

## Requirements
The latest verision of tkinter has to be installed. Software was developed and tested on python 3.7

## Installation and running
Clone the repository and enter the CIE_Assembler directory.

run ```python src/main.py``` or ```python3 src/main.py```

Now have fun playing around with the CIE Assembler virtual machine!

## Specification
Here is the specification image:

![spec](https://github.com/CompSci-OIC/Projects/blob/master/CIE_Assembler/images/spec.png?raw=true)

We have implemented all of the listed commands.

We have also implemented the ability for user to define specific bytes at the beginning of the program.

The syntax is as follows:

```<DB>``` followed by ```\n``` character

then ```\n``` separated ```<byte address>:<byte value>```

```\n``` character and a terminator ```</DB>```

it should look like that:
```
<DB>
16:72
17:69
...
</DB>
```
