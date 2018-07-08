with open('movie_lines.txt') as in_f:
    with open('out_file.txt', 'w') as out_f:
        for i in [i.strip() for i in in_f if i != '\n']:
            out_f.write(' '.join(i.split()[8:]) + '\n')
