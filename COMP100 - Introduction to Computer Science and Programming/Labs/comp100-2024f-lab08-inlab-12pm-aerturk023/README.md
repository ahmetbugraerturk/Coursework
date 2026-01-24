[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/n5o9Bytf)
# COMP100 2024F Lab 08 InLab 12 PM:

## Deadline: Friday, 06 December 2024, 13:40 PM

###  Cracking the Case: Tracking City Clues

You are a smart digital detective exploring the database at *DataVault*. As you dig into it, you find lots of folders and hidden files, all organized in a tricky way. Your mission is to carefully look through this pile of information, checking every file for important clues. Some files contain encrypted messages urging you to investigate particular cities, with dates specified, such as: "Attention! Check **** PARIS (25/11/2023) ****."

Your task is to find these special files and write down the cities and dates you find. When you discover them, use  *special shell command* to write the code into a file called "CityClues.txt". **Please do not copy and paste manually.**

People say there might be about 10 city clues hidden in DataVault's database. Your reputation as a great digital detective depends on finding **at least 5** of these important cities to crack the case.

After you find at least 5 keys, you need to paste your all commands to main.sh.

**Important Notes**:
- You are given DataVault folder which has many subfolders and subfiles, you need to explore this folder using ```cd``` and ```ls``` commands.
- If you find a .txt file that has a city clue, append the clue to CityClues.txt, which is in the same directory with DataVault folder. You can use ```cat``` command and ```>>``` operator. 
- Paste your commands to main.sh. You can view the last n command by typing ```history n```. For example, if you want to check your last 50 commands, you need to type ```history 50```.