import subprocess

# run the ipconfig command and capture the output
output = subprocess.check_output(['ipconfig']).decode('utf-8')

# print the output
print(output)