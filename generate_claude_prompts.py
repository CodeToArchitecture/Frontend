import os
from os.path import isfile, join

path_to_code_files = "./example"

user_prompt_filename = "user_prompt.txt"
system_prompt_filename = "system_prompt.txt"
divider_string = "##################"


def create_user_prompt_for_image() -> None:
    """
    Creates prompt with code context to generate images
    Format:
    "Now generate XML output for this terraform code. Make sure to close all the XML tags you open:

    {{ terraform_code }}

    Only output the XML content, do no output any English."
    """
    tf_files = _get_code_filenames()

    with open(user_prompt_filename, "a") as user_prompt_file:
        user_prompt_file.write("Now generate XML output for this terraform code. Make sure to close all the XML tags you open:\n")
        user_prompt_file.write(f"{divider_string}\n")

        _write_code_files_to_prompt_file(prompt_file=user_prompt_file, code_filenames=tf_files)

        user_prompt_file.write(f"{divider_string}\n")
        user_prompt_file.write("Only output the XML content, do no output any English.")


def create_system_prompt_for_chat():
    """
    Creates prompt with Terraform files to XML examples

This is the code base:

{code base files}
    """
    tf_files = _get_code_filenames()

    with open(system_prompt_filename, "a") as prompt_file:
        prompt_file.write("You are an assistant. Help the user understand with below code context.\n")
        prompt_file.write("These are the code files:\n")
        prompt_file.write(f"{divider_string}\n")

        _write_code_files_to_prompt_file(prompt_file=prompt_file, code_filenames=tf_files)

        prompt_file.write(f"{divider_string}\n")


def _get_code_filenames():
    return [tf_filename for tf_filename in os.listdir(path_to_code_files) \
                if (isfile(join(path_to_code_files, tf_filename)) and \
                (tf_filename.endswith(".tf") or tf_filename.endswith("tfvars")))]

def _write_code_files_to_prompt_file(prompt_file, code_filenames: str):
    for tf_filename in code_filenames:
        # Open each tf file
        with open(join(path_to_code_files, tf_filename), "r") as tf_file:
        # Write title of tf file in prompt file
            prompt_file.write(f"Title: {tf_filename}\n")
        # Write tf file contents in prompt file
            prompt_file.writelines(tf_file.readlines())
