from os import getcwd
from pathlib import Path

project_folder_path = Path(getcwd()).parent

template_folder_path = project_folder_path / "templates"
app_folder_path = project_folder_path / "bar"
