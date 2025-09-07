import os
import subprocess

# thnk this is ready for tests


def run_python_file(working_directory, file_path, args=[]):
    try:
        abs_working_directory = os.path.abspath(working_directory)
        joined_path = os.path.join(abs_working_directory, file_path)
        file_to_execute = os.path.abspath(joined_path)
        if not file_to_execute.startswith(abs_working_directory):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(file_to_execute):
            return f'Error: File "{file_path}" not found.'
        if not file_to_execute.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        command = ["python3", file_to_execute] + args
        try:
            cp = subprocess.run(
                command,
                check=True,
                cwd=abs_working_directory,
                timeout=30,
                capture_output=True,
                text=True,
            )
        except subprocess.TimeoutExpired:
            return f'Error: Execution of "{file_path}" timed out.'
        if not cp.stdout.strip() and not cp.stderr.strip():
            return f"No output produced."
        returncode_text = ""
        if cp.returncode != 0:
            returncode_text = f'Process exited with code X" {cp.returncode}\n'
        return f"STDOUT:\n{cp.stdout.strip()}\nSTDERR:\n{cp.stderr.strip()}\n{returncode_text}"
    except Exception as e:
        return f"Error: executing Python file: {e}"
