import os


def get_files_info(working_directory, directory="."):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        joined_path = os.path.join(abs_working_directory, directory)
        target_directory = os.path.abspath(joined_path)
        if not target_directory.startswith(abs_working_directory):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_directory):
            return f'Error: "{directory}" is not a directory'
        files_info = []
        try:
            with os.scandir(target_directory) as it:
                for entry in it:
                    info_str = f"- {entry.name}: file_size={entry.stat().st_size} bytes, is_dir={entry.is_dir()}\n"
                    files_info.append(info_str)
        except FileNotFoundError:
            return f'Error: Directory "{directory}" does not exist'
        except PermissionError:
            return f"Error:Permission denied for directory {target_directory}."
    except Exception as e:
        return f"Error:An error occurred: {e}"
    return "".join(files_info)
