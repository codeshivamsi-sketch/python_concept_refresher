import subprocess

result = subprocess.run(["ls", "-la"], capture_output=True, text=True) # text=True coverts output to string (from byte)
print(result.stdout)
print(result.returncode) # output of the command, 0 - success, anything else - error


result2 = subprocess.run(["echo", "hello"], capture_output=True, text=True)
print(result2.stdout)


# Check for errors, this fails silently
result3 = subprocess.run(["ls", "fakefolder"], capture_output=True, text=True) 
print(result.stderr)
print(result3.returncode) # return 1, not 0.


# Check=True ensure on error command wont fail silently instead will throw error 
result4 = subprocess.run(["ls", "fakefolder"], capture_output=True, text=True, check=True)
print(result.stdout)