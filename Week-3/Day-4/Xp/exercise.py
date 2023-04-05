# Exercise 1

import os
import random

directory = os.path.dirname(__file__) + "/words_list.txt"

random.seed(314)

def get_words_from_file(dir):
    with open(dir, "r") as words:
        words_list = words.readlines()
    return words_list

def get_random_sentence(length):
    sentence_list = random.choices(get_words_from_file(directory), k=length)
    return "".join(sentence_list).lower().replace("\n", " ")

def main():
    print("Hi, welcome to the Random Sentence Generator 2000!")
    print("Choose how many words between 2 and 20 that you would like to have and I'll make you a sentence that makes no sense.")
    try:
        length = int(input("Amount of words: "))
    except:
        raise ValueError("You disappointed me! I asked for a number!")
    if (length < 2) or (length > 20):
        raise ValueError("I told you to put a number between 2 and 20... Why couldn't you follow this simple order?")
    print(get_random_sentence(length))

main()

# Exercise 2

import os
import json

base_dir = os.path.dirname(__file__)

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

json_data = json.loads(sampleJson)

print(json_data["company"]["employee"]["payable"]["salary"])

json_data["company"]["employee"]["birth_date"] = "1/1/2000"

json_file_dir = base_dir + "/json_file.json"

with open(json_file_dir, "w") as f:
    json.dump(json_data, f, indent=2)