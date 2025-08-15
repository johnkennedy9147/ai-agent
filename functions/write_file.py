import os


def write_file(working_directory, file_path, content):
    if not content:
        return "Error: Content cannot be empty"
    try:
        abs_working_directory = os.path.abspath(working_directory)
        joined_path = os.path.join(abs_working_directory, file_path)
        target_file_path = os.path.abspath(joined_path)
        if not target_file_path.startswith(abs_working_directory):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(target_file_path):
            os.makedirs(os.path.dirname(target_file_path), exist_ok=True)
        with open(target_file_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f"Error:An error occurred: {e}"
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
