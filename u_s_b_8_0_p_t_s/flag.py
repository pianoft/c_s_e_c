import subprocess


def run(commands):
    subprocess.run([commands], shell=True)
    return
    
run('rm -rfv *.txt')
a, b = 4, 1
for i in range(0, 7):
    #  icat - Output the contents of a file based on its inode number.
    run('icat drive.img 36-128-'+str(a) + ' > ' + str(b)+'.txt')
    a, b = a+1, b+1

ans = ''
for i in range(1, 8):
    fr = open(str(i)+'.txt', 'r').readline()
    ans += fr
print(ans)
