import os

def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        lines = []
        for item in os.listdir(target_dir):
            joined_path = os.path.join(target_dir, item)
            is_dir = os.path.isdir(joined_path)
            file_size = os.path.getsize(joined_path)
            line = f'- {item}: file_size={file_size} bytes, is_dir={is_dir}'
            lines.append(line)
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e}"