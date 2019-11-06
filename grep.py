def grep(text, files, flags=''):
    matching = []
    for filename in files:
        with open(filename) as f:
            for i, line in enumerate(iter(f.readline, ''), start=1):
                # prepare line for comparison
                line = line.rstrip('\r\n')
                # iter file line by line
                options = []
                queued = None
                if '-x' in flags:
                    # only match entire line
                    if text == line or ('-i' in flags and text.lower() == line.lower()) and '-v' not in flags:
                        queued = line
                elif text in line or ('-i' in flags and text.lower() in line.lower()):
                    # regular match
                    if '-v' not in flags:
                        queued = line
                elif '-v' in flags:
                    # not matching but reverse search
                    queued = line

                if queued is not None:
                    if '-l' in flags:
                        # only filename needed
                        matching.append(filename)
                        break
                    if len(files) > 1:
                        # print filename only if several files are passed
                        options.append(f'{filename}:')
                    if '-n' in flags:
                        # print line number
                        options.append(f'{i}:')

                    matching.append(f'{"".join(options)}{line}')
    if len(matching) > 0 or '-l' in flags:
        matching.append('')
    return '{}'.format('\n'.join(matching))