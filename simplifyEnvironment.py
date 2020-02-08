#conda env export > environment.yml makes an environment with all the specific dependencies
#this is not cross platform and requires manually changing the environment.yml to what you care about
#this seeks to simply the process by removing all specific versions and praying conda can figure it out

f = open("environment.yml", 'r')
n = open("newenvironment.yml", 'w')
for line in f:
    base = line.split("=")[0]
    if base[-1] != '\n':
        base += '\n'
    n.write(base)
