import os
import tomli


def get_file_content(working_directory, file_path):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        joined_path = os.path.join(abs_working_directory, file_path)
        target_file_path = os.path.abspath(joined_path)
        if not target_file_path.startswith(abs_working_directory):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        config_path = os.path.join(os.path.dirname(__file__), "config.toml")
        with open(config_path, "rb") as c:
            config = tomli.load(c)
        file_content_length_limit = config["file_content_length_limit"]
        with open(target_file_path, "r") as f:
            data = f.read(file_content_length_limit+1)
            file_content = data[:file_content_length_limit] 
            if len(data) > file_content_length_limit:
                file_content += f'[...File {target_file_path} truncated at {file_content_length_limit} characters]'
    except Exception as e:
        return f"Error:An error occurred: {e}"
    return file_content
