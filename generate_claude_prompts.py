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
    user_prompt_file = open(user_prompt_filename, "a")
    tf_files = [tf_filename for tf_filename in os.listdir(path_to_code_files) \
                if (isfile(join(path_to_code_files, tf_filename)) and \
                (tf_filename.endswith(".tf") or tf_filename.endswith("tfvars")))]

    with open(user_prompt_filename, "a") as user_prompt_file:
        user_prompt_file.write("Now generate XML output for this terraform code. Make sure to close all the XML tags you open:\n")
        user_prompt_file.write(f"{divider_string}\n")

        for tf_filename in tf_files:
            # Open each tf file
            with open(join(path_to_code_files, tf_filename), "r") as tf_file:
            # Write title of tf file in prompt file
            # Write tf file contents in prompt file
            # Close the tf file
                user_prompt_file.write(f"Title: {tf_filename}\n")
                user_prompt_file.writelines(tf_file.readlines())
                

        user_prompt_file.write(f"{divider_string}\n")
        user_prompt_file.write("Only output the XML content, do no output any English.")
    
    


def create_system_prompt():
    """
    Creates prompt with Terraform files to XML examples
    """
    pass


create_user_prompt_for_image()