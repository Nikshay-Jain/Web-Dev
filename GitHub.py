import subprocess

command = "git status"
try:
    output = subprocess.check_output(command, shell=True, text=True, stderr=subprocess.STDOUT)
    file_lines = output.strip().split('\n')

    for i in range(len(file_lines)-7):
        status = file_lines[i+6][1:2]

        if status == 'd':
            file_path = file_lines[i+6][13:]
            subprocess.run(f'git rm "{file_path}"')
            subprocess.run(f'git commit -m "Removed {file_path}"')
            print(f"Deleted and committed: {file_path}")
        
        elif status == 'm':
            file_path = file_lines[i+6][13:]
            subprocess.run(f'git add "{file_path}"')
            subprocess.run(f'git commit -m "Updated {file_path}"')
            print(f"Modified and committed: {file_path}")

        else:
            file_path = file_lines[i+6][1:]
            if(file_path=="is up to date with 'origin/main'." or file_path=="Untracked files:" or file_path=='  (use "git add <file>..." to include in what will be committed)'):
                continue
            else:
                subprocess.run(f'git add "{file_path}"')
                subprocess.run(f'git commit -m "Added {file_path}"')
                print(f"Added and committed: {file_path}")
        
    subprocess.run('git push -u origin main')
    print("Repository Updated Successfully.")

except subprocess.CalledProcessError as e:
    print("Command execution failed.")
    print("Error:", e)