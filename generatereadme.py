import os

header = ''
body = ''
excluded_dirs = ['.git']
excluded_files = ['.gitignore', 'input']

with open('.header.md', 'r') as header_file:
    header = header_file.readlines()

for root, dirs, files in os.walk('.', topdown=True):
    dirs[:] = sorted([d for d in dirs if d not in excluded_dirs])
    files[:] = [f for f in files if f not in excluded_files]
    if len(dirs) == 0:
        body = body + '# {}\n'.format(root[2:])
        for file in sorted(files):
            body = body + '## {}\n'.format(file)
            with open(os.path.join(root, file), 'r') as soln_file:
                body = body + '```py\n'
                body = body + ''.join(soln_file.readlines())
                body = body + '```\n'

with open('README.md', 'w') as new_readme_file:
    new_readme_file.writelines(header)
    new_readme_file.writelines(body)
