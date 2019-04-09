import os, sys, subprocess

file = open('README.md', 'r')
dest = open('README.md.tmp', 'w')

def get_usage() -> str:
    result = subprocess.run([sys.executable, 'main.py', '-h'], stdout=subprocess.PIPE)
    return str(result.stdout, 'utf-8').replace('\\n', '\n')

def read_question(folder) -> str:
    question_file = open(os.path.join(folder, 'readme.md'), 'r')
    result = '##' + question_file.read()
    question_file.close()
    return result

next_header = False
for line in file:
    if next_header and not line.startswith('## '):
        continue
    
    next_header = False
    if line.startswith('## Usage'):
        print('Collecting usage...')
        next_header = True

        dest.write(line)
        dest.write('\n```text\n')
        dest.write(get_usage())
        dest.write('```\n\n')
        continue
    
    if line.startswith('## Questions'):
        print('Collecting questions...')
        next_header = True

        dest.write(line)
        dest.write('\n')
        folders = list(filter(lambda s: s.startswith('problem_') and os.path.isdir(s), os.listdir('./')))
        folders.sort()
        for folder in folders:
            dest.write(read_question(folder))
            dest.write('\n')
        continue
    
    dest.write(line)


file.close()
dest.close()

print('Renaming README.md.tmp to README.md')
os.remove('README.md')
os.rename('README.md.tmp', 'README.md')

print('Done')
