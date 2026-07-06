workflows = ['atacseq', 'chipseq', 'nanoseq', 'rangeland', 'rnaseq', 'sarek']

for workflow in workflows:
    for run in range(1, 4):
        with open(f'traces/hu-{workflow}-{run}.csv', 'r') as orig_file:
            lines = orig_file.readlines()

        with open(f'traces/temp/hu-{workflow}-{run}.csv', 'w') as new_file:
            new_file.write(lines[0].strip() + '\tcpu_model\n')
            for line in lines[1:]:
                orig_line = line.strip()
                new_line = f'{orig_line}\tIntel Xeon Silver 4314\n'
                new_file.write(new_line)
