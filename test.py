import os
import subprocess

files_directory = "test"
files = os.listdir(files_directory)

def wc_test(file_path):
    result = subprocess.check_output(['python', os.path.join('program_files','wc.py'), file_path], universal_newlines=True)
    return (result.strip())

def run_tests():
    global files_directory
    input_files = [file for file in files if file.endswith(".in") and "wc" in file]
    output_files = [file for file in files if file.endswith(".out") and "wc" in file]

    for i in range(0, len(input_files)):
        file_path = os.path.join(files_directory, input_files[i])
        output = wc_test(file_path)
        out_file = os.path.join(files_directory, output_files[i])
        with open(out_file) as f:
            expected_output = f.read()
        assert expected_output.strip() == output.strip()
        print("Success!")
        # print(f"{i}\n{expected_output}")
        # print(f"{i}\n{output}")

if __name__ == "__main__":
    run_tests()