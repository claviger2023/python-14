def save_applicant_data(source, output):
    output_content = ''
    for i in range(len(source)):
        ab_info= source[i].get('name')+','+str(source[i].get('specialty'))+','+str(source[i].get('math'))+','+str(source[i].get('lang'))+','+str(source[i].get('eng'))
        ab_info = ab_info + '\n'
        output_content = output_content + ab_info
    with open(output, "w") as fo:
        fo.write(output_content)

source = [
    {
        "name": "Kovalchuk Oleksiy",
        "specialty": 301,
        "math": 175,
        "lang": 180,
        "eng": 155,
    },
    {
        "name": "Ivanchuk Boryslav",
        "specialty": 101,
        "math": 135,
        "lang": 150,
        "eng": 165,
    },
    {
        "name": "Karpenko Dmitro",
        "specialty": 201,
        "math": 155,
        "lang": 175,
        "eng": 185,
    },
]

output = 'hw6-8.txt'

save_applicant_data(source, output)