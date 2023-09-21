# https://colab.research.google.com/drive/1DEBPsccVLF_aUnmD0FwPeHFrtdC0QIUP?usp=sharing

import openai
import urllib.parse
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = "EMPTY"  # Key is ignored and does not matter
openai.api_base = "http://zanino.millennium.berkeley.edu:8000/v1"
# Alternate mirrors
# openai.api_base = "http://34.132.127.197:8000/v1"


#  Edit your own paths in `.env` file
data_path = os.environ.get("DATA_PATH")
src_path = os.environ.get("SRC_PATH")
output_path = os.environ.get("OUTPUT_PATH")


# Report issues
def raise_issue(e, model, prompt):
    issue_title = urllib.parse.quote("[bug] Hosted Gorilla: <Issue>")
    issue_body = urllib.parse.quote(f"Exception: {e}\nFailed model: {model}, for prompt: {prompt}")
    issue_url = f"https://github.com/ShishirPatil/gorilla/issues/new?assignees=&labels=hosted-gorilla&projects=&template=hosted-gorilla-.md&title={issue_title}&body={issue_body}"
    print(f"An exception has occurred: {e} \nPlease raise an issue here: {issue_url}")


# Query Gorilla server
def get_gorilla_response(prompt="I would like to translate from English to French.", model="gorilla-7b-hf-v1"):
    try:
        completion = openai.ChatCompletion.create(model=model, messages=[{"role": "user", "content": prompt}])
        return completion.choices[0].message.content
    except Exception as e:
        raise_issue(e, model, prompt)


# Defined func for writing result into local file `module1.py` in a formated way, and return the code for next task's usgae
def inference(prompt, mode="a"):
    output = get_gorilla_response(prompt, model="gorilla-7b-hf-v1")
    code = output.split("<<<code>>>:")[1]
    exepln = output.split("<<<code>>>:")[0]

    print(code)

    new = os.path.join(src_path, "module1.py")
    with open(new, mode) as f:
        f.write("\n" + f'"""\n{exepln}\n"""')
        f.write("\n" + code)

    f.close()
    return code


# TASK 1

# img_path = os.path.join(parent_directory, "data", "pic.png")
# prompt = f"I want to detect objects in an image {img_path}."
prompt = f'I want to write an essay discussing about the topic "Education should be free" with 300 words. Do not use the model bigscience/bloom-7b1. Save the essay in a new file in the path {output_path}.'
code = inference(prompt, "w")

print("\n#######\tStage 1 finished\t#######\n")


# TASK 2

# getting result from last output
rs = code.splitlines()[-1].split("(")[-1].split(")")[0]
prompt2 = f"I would like to translate the text to Swedish. The text is stored in a variable called {rs}."

code2 = inference(prompt2)
