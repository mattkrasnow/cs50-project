def write_to_file(filename, content):
    with open(filename, 'w') as f:
       f.write(content)

def run_file(filename):
    import subprocess
    subprocess.run(['python', filename])

if __name__ == "__main__":
    user_code = input("Enter your Python code: ")
    practice_filename = 'practice.py'
   
    # Write the input to practice.py
    write_to_file(practice_filename, user_code)
   
    # Now run practice.py
    run_file(practice_filename)