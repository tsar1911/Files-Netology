def merge_files(filenames, output_file):
    file_data = []

    for filename in filenames:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            file_data.append((filename, len(lines), lines))

    file_data.sort(key=lambda x: x[1])

    with open(output_file, 'w', encoding='utf-8') as output:
        for filename, num_lines, lines in file_data:
            output.write(f"{filename}\n")
            output.write(f"{num_lines}\n")
            output.writelines(lines)


filenames = ['1.txt', '2.txt', '3.txt']
output_file = 'merged_output.txt'

merge_files(filenames, output_file)