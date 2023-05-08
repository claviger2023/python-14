def sanitize_file(source, output):
    with open(source, "r") as fs:
        output_content = ''
        for k in fs.read():
            line = ''
            for i in k:
                if not i.isnumeric():
                    line = line + i
            output_content = output_content + line
        with open(output, "w") as fo:
            fo.write(output_content)
