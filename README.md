# Duck-Decoder

## Introduction

A while ago I went to recieve some classes to annother country lucky for me, I already had my duck! Often in my trip
I found myself near unlocked computers which I could dump lssas or backdoor depending the case, for this I started doing a whole bunch of different payloads and scripts to pwn all of these computers!

Sadly for me, since I wasnt using my own computer at the time (for security) I erased the whole account on the system except for my backed up source files.. or so I thought! I had mistakenly backed up only the *inject.bin* files and all of my thousands of lines of source code were gone now! I thought, if I just keep the .bins classified I could still reuse them to pwn computers until, a Win 8 computer comes up aviable to hack and none of my scripts work!

This project was the result of having to figure out what was inside all of those *inject.bin* files that I had saved over time for on-the-fly payload changing. This script solved my problem of often losing or accidentaly deleting the source code files of all my hacks.

## How to use it

The project was made using python 2.7.3, to run it you can do:
```
 python DuckDecoder.py <display | decode> /path/to/inject.bin
```

Run it without arguments to display the help menu. The program currently has two modes, to explain them better lets say I encode this payload:
```
 DELAY 500
 STRING Hello!!
 BACKSPACE
 ENTER
 STRING This is a test!!
```
The display mode is intended to show you what would the code look like once it was typed by the duck, deleting when backspace and not showing delays. Runing __DuckDecoder.py display /path/to/inject.bin__ will output this:
```
 Hello!
 This is a test!!
```

The decode mode is intended to output the text in Duck-ready format for revision or reuse in other scripts. Runing __DuckDecoder.py decode /path/to/inject.bin__ will output this:

```
 DELAY 500

 STRING Hello!!
 BACKSPACE 
 ENTER 
 STRING This is a test!!
```

## Want support for a different keyboard?

The program finds the position of the duck hex code and translates it by finding its mirror position in another
list with the letters. To submint a keyboard mapping, make two lists pressing the keys in this order:

![keyboard_mapping] (https://raw.githubusercontent.com/JPaulMora/Duck-Decoder/master/mapping.png) { width: 400px; }

The lists should look like this, one for shift and one for plain characters:

```
 Letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"etc..]
 CapLetters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"etc..]
```

