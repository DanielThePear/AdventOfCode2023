import os
import json
import requests

def main() -> None:
    
    os.chdir(os.path.dirname(os.path.abspath(__file__)))    
    
    with open("config.json", "r") as f: config = json.load(f)
    with open("Template.py", "r") as f: template = f.read()
    
    os.chdir(os.path.abspath(config["aocParentDir"]))

    day = int(input("Which day? "))

    try: os.mkdir(f"Day{day}")
    except FileExistsError:
        print(f"Day {day} already exists")
        return
    
    os.chdir(os.path.abspath(f"Day{day}"))

    r = requests.get(
        f"https://adventofcode.com/{config['aocYear']}/day/{day}/input",
        cookies = {"session": config["aocSessionCookie"]}
    )
    
    with open("input.txt", "w", encoding="utf-8") as file: file.write(r.text)
    with open("Problem1.py", "w", encoding="utf-8") as file: file.write(template)
    with open("Problem2.py", "w", encoding="utf-8") as file: pass # make empty file
    with open("TestInput.txt", "w", encoding="utf-8") as file: pass # empty file, to insert testing input for problem 1
    
    print(f"Generated files for Advent of Code Day {day}")
    

if __name__ == "__main__": main()