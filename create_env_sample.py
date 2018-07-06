import re

env = open(".env", "r")
lines = env.readlines()

env_sample = []
for line in lines:
    if("DEBUG" in line):
        line = line.replace("True", "False")

    # 'で囲われてる値だけ消す
    line = re.sub(r"\'.*\'", "\"\"", line)
    env_sample.append(line)


sample_file = open(".env.sample", "w+")
sample_file.writelines(env_sample)
