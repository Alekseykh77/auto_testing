import subprocess
import string

command = "cat /home/alexey/PycharmProjects/auto_testing/hw1/hello.txt "

result = subprocess.run(command, shell=True, encoding="utf-8", stdout=subprocess.PIPE)
result_out = result.stdout
print(result_out)
result_of_words = result_out.translate((str.maketrans("", "", string.punctuation)))
print(result_of_words)
if __name__ == '__main__':
    if "Hello" in result_of_words and result.returncode == 0:
        print("True")
    else:
        print("False")
