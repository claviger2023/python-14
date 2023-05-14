def to_indexed(source_file, output_file):
    with open(source_file, 'r') as fh:
        content = fh.readlines()
        new_lines = []
        for i in range(len(content)):
            line = str(i) + ': ' + content[i]
            new_lines.append(line)
    with open(output_file, "w") as fh:
        fh.writelines(new_lines)