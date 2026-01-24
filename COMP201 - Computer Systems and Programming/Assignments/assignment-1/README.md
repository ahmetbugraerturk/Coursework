[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/GRD5dCwR)
# COMP201 – Assignment 1

This repository contains the starter code and some example input/output files for **COMP201 Assignment 1**.  
The example files are located in the `test1/` and `test2/` folders, and there is also a Bash (`.bash`) script to run the entire pipeline at once.

---

## 🧠 What Is a `.bash` File?

A `.bash` file is a **Bash shell script**—a text file containing commands that can be executed in a Unix-like terminal.  

**Bash** (short for *Bourne Again SHell*) is a command interpreter commonly used on Linux and macOS, and available on Windows through **WSL** (Windows Subsystem for Linux) or **Git Bash**.

### What Can a Bash Script Do?

A Bash script can:
- Compile and run programs (e.g., `gcc main.c -o main`)
- Automate multiple commands in sequence
- Manage input/output files and redirections
- Run a sequence of test cases automatically
- Chain together multiple programs or tools

### Typical Structure

The first line of a Bash script often specifies which shell should run it:
```bash
#!/usr/bin/env bash
```

This is called a **shebang** and tells the system to use the Bash interpreter to execute the script.

---

## 🚀 How to Run the Test Scripts

The Bash files in this repository are designed to execute the entire pipeline at once. They do not compare the outputs automatically, but if you want, you can implement output comparison yourself! 😊

### Prerequisites

Make sure you have:
- A Unix-like environment (Linux, macOS, or Windows with WSL/Git Bash)
- The necessary compilers/interpreters for your code (e.g., `gcc` for C programs)
- Execute permissions on the `.bash` files (see instructions below)

### Step 1: Make the Script Executable

Before running a `.bash` file, you need to give it execute permissions:

```bash
chmod +x test1/run_test.bash
chmod +x test2/run_test.bash
```

### Step 2: Run the Script 

⚠️ **Important:** Keep in mind this will overwrite the output files, so do not forget to have a backup of ground truth outputs (or rename them, e.g., `output.txt` → `expected_output.txt`)!

You can execute the script in two ways:

**Option 1: Direct execution** (after `chmod +x`)
```bash
./test1/run_test.bash
./test2/run_test.bash
```

**Option 2: Explicitly call Bash**
```bash
bash test1/run_test.bash
bash test2/run_test.bash
```

### Step 3: Check the Output

After running the script, check the output files. You can manually compare them with the expected output files provided in the test folders.

---

## 📂 Repository Structure

```
comp201_assignment_1/
├── test1/
│   ├── input files
│   ├── expected output files
│   └── run_test.bash       # Script to run test 1
├── test2/
│   ├── input files
│   ├── expected output files
│   └── run_test.bash       # Script to run test 2
└── README.md               # This file
```

---

## 💡 Tips

- Read through the `.bash` files to understand what commands are being executed
- You can modify the scripts to add output comparison or additional test cases
- If you encounter "Permission denied" errors, make sure you've run `chmod +x` on the script

---


Good luck with your assignment! 🎓
