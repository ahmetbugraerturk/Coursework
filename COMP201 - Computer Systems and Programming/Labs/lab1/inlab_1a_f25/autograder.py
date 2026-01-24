#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import subprocess
import stat

def run_command(command):
    try:
        proc = subprocess.Popen(
            ["/bin/bash", "-c", command],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True
        )
        stdout, stderr = proc.communicate()
        return stdout.strip(), stderr.strip()
    except Exception as e: return "", str(e)

def setup_question_dir(dir_name):
    if os.path.exists(dir_name): shutil.rmtree(dir_name)
    os.makedirs(dir_name)
    os.chdir(dir_name)

def cleanup_question_dir(original_dir, dir_name):
    os.chdir(original_dir)
    if os.path.exists(dir_name): shutil.rmtree(dir_name)

# --- Graders for Lab A ---

def grade_question_1(command):
    run_command(command)
    return os.path.isfile("report_part1.txt") and os.path.isfile("report_part2.txt")

def grade_question_2(command):
    run_command(command)
    return os.path.isdir("submission/code/src")

def grade_question_3(command):
    with open("main_log.txt", "w") as f: f.write("log data")
    os.makedirs("logs")
    run_command(command)
    return not os.path.exists("main_log.txt") and os.path.isfile("logs/archive_log.txt")

def grade_question_4(command):
    with open("script_A.sh", "w") as f: f.write("#!/bin/bash")
    run_command(command)
    if not os.path.exists("script_A.sh"): return False
    expected_mode = stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP # 750
    actual_mode = os.stat("script_A.sh").st_mode
    return (actual_mode & 0o777) == expected_mode

def grade_question_5(command):
    os.makedirs("cache/subdir")
    with open("cache/a.bak", "w") as f: f.write("data")
    with open("cache/subdir/b.bak", "w") as f: f.write("data")
    with open("cache/c.txt", "w") as f: f.write("data")
    with open("d.bak", "w") as f: f.write("data")
    run_command(command)
    return not os.path.exists("cache/a.bak") and not os.path.exists("cache/subdir/b.bak") and os.path.exists("cache/c.txt") and os.path.exists("d.bak")

def grade_question_6(command):
    with open("user.conf", "w") as f: f.write("c1")
    with open(".settings.conf", "w") as f: f.write("c2")
    with open("data.txt", "w") as f: f.write("d")
    stdout, _ = run_command(command)
    return stdout.strip() == "2"

def grade_question_7(command):
    with open("status.log", "w") as f: f.write("Initial log entry\n")
    run_command(command)
    if not os.path.exists("status.log"): return False
    with open("status.log", "r") as f: content = f.read().strip()
    return content == "Initial log entry\nSystem Ready"

def main():
    original_dir = os.getcwd()
    answers_file = "answers_A.txt"
    graders = [
        grade_question_1, grade_question_2, grade_question_3, grade_question_4,
        grade_question_5, grade_question_6, grade_question_7
    ]
    if not os.path.exists(answers_file):
        print("Error: '{}' file not found.".format(answers_file)); return
    with open(answers_file, "r") as f:
        student_answers = [line.strip() for line in f.readlines()[1:]]
    while len(student_answers) < len(graders): student_answers.append("")
    print("--- Starting Evaluation for Lab A ---")
    score = 0
    for i, (grader_func, answer) in enumerate(zip(graders, student_answers), 1):
        if not answer:
            print("Question {}: Incorrect (No answer provided)".format(i)); continue
        question_dir = "q{}_test_env".format(i)
        try:
            setup_question_dir(question_dir)
            if grader_func(answer): print("Question {}: Correct".format(i)); score += 1
            else: print("Question {}: Incorrect".format(i))
        except Exception as e: print("An error occurred while grading question {}: {}".format(i, e))
        finally: cleanup_question_dir(original_dir, question_dir)
    print("\n--- Evaluation Finished ---")
    print("Final Score: {}/{}".format(score, len(graders)))

if __name__ == "__main__": main()