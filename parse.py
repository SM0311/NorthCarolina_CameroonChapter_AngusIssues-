import os
import subprocess

def find_python_files(directory):
    """Recursively find all Python files in the given directory."""
    python_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                full_path = os.path.join(root, file)
                print(f"Found Python file: {full_path}")  # Debug line
                python_files.append(full_path)
    return python_files

def run_pyreverse(directory, output_format='png', project_name='Project'):
    """Run pyreverse on all Python files found in the directory."""
    python_files = find_python_files(directory)
    
    if not python_files:
        print("No Python files found.")
        return
    
    try:
        # Run pyreverse
        command = [
            'pyreverse',
            '-o', 'dot',  # Generate dot files
            '-p', project_name,
            '-a', '1',  # Include attributes
            '-s', '1',  # Include methods
            '-f', 'ALL',  # Include all classes and methods
        ] + python_files  # Pass the files as separate arguments

        print(f"Running command: {' '.join(command)}")  # Debug line
        subprocess.run(command, check=True)
        
        # Convert dot files to png
        for dot_file in ['classes.dot', 'packages.dot']:
            png_file = dot_file.replace('.dot', f'.{output_format}')
            if os.path.exists(dot_file):
                convert_command = [
                    'dot',
                    '-Tpng',  # Output format
                    dot_file,
                    '-o', png_file
                ]
                subprocess.run(convert_command, check=True)
    
    except subprocess.CalledProcessError as e:
        print(f"Error during subprocess execution: {e}")

# Replace with the correct absolute path to your directory
run_pyreverse('/home/aaronl/Downloads/NorthCarolina_CameroonChapter_AngusIssues')

