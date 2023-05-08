import os, sys, shutil

CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯЄІЇҐ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g", 
                "A", "B", "V", "G", "D", "E", "E", "J", "Z", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "U", "F", "H",
                "TS", "CH", "SH", "SCH", "", "Y", "", "E", "YU", "YA", "JE", "I", "JI", "G")

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

def normalize(name):
    new_name = name.translate(TRANS)            # translit to kyrilic
    final_name = ''
    for i in range(len(new_name)):              # change other symbols in the filename
        if not (new_name[i] in TRANSLATION):
            final_name += '_'
        else:
            final_name += new_name[i]
    return final_name

all_files = {
    "images" : [],
    "documents" : [],
    "audio": [],
    "video": [],
    "archives": []
}
all_formats = []
unknown_formats = []

def sort_files(foldername):
    # receiving list of folders and files
    entries = os.listdir(foldername)
    subfolders = []

    # checking and creating new folders
    img_folder = foldername + '/images'
    doc_folder = foldername + '/documents'
    audio_folder = foldername + '/audio'
    video_folder = foldername + '/video'
    archives_folder = foldername + '/archives'
    if not os.path.exists(img_folder):
        os.makedirs(img_folder)
    if not os.path.exists(doc_folder):
        os.makedirs(doc_folder)
    if not os.path.exists(audio_folder):
        os.makedirs(audio_folder)
    if not os.path.exists(video_folder):
        os.makedirs(video_folder)
    if not os.path.exists(archives_folder):
        os.makedirs(archives_folder)

    # sorting files regarding the format

 #   for root, d_names, f_names in os.walk(foldername):
 #       for folder in root:
 #           if folder != 'images' and folder != 'documents' and folder != 'audio' and folder != 'video' and folder != 'archives':
 #               if (os.path.isdir(foldername)) and (not os.listdir(folder)):
 #                   shutil.rmtree(folder)    
 #       print (root, d_names, f_names)

    for file in entries:
        filepath = foldername + '/' + file

        if os.path.isfile(filepath):
            # preparting file name and format for checking the file extention (format)
            format = os.path.splitext(filepath)[-1].lower()
            file_name = file.replace(format, '')
            new_file_name = normalize(file_name) + format
            
            # sorting file and moving to the certain folder, adding the file format and name into our lists
            if format.endswith(".jpeg") or format.endswith(".jpg") or format.endswith(".png") or format.endswith(".svg"):
                shutil.move(filepath, img_folder + '/' + new_file_name)
                if not (format in all_formats):
                    all_formats.append(format)
                all_files["images"].append(new_file_name)

            elif format.endswith(".doc") or format.endswith(".docx") or format.endswith(".txt") or format.endswith(".pdf") or format.endswith(".xlsx") or format.endswith(".pptx"):
                shutil.move(filepath, doc_folder + '/' + new_file_name)
                if not (format in all_formats):
                    all_formats.append(format)
                all_files["documents"].append(new_file_name)

            elif format.endswith(".mp3") or format.endswith(".ogg") or format.endswith(".wav") or format.endswith(".amr"):
                shutil.move(filepath, audio_folder + '/' + new_file_name)
                if not (format in all_formats):
                    all_formats.append(format)
                all_files["audio"].append(new_file_name)

            elif format.endswith(".avi") or format.endswith(".mp4") or format.endswith(".mov") or format.endswith(".mkv"):
                shutil.move(filepath, video_folder + '/' + new_file_name)
                if not (format in all_formats):
                    all_formats.append(format)
                all_files["video"].append(new_file_name)

            elif format.endswith(".zip") or format.endswith(".gz") or format.endswith(".tar"):
                #shutil.move(filepath, archives_folder + '/' + new_file_name)
                shutil.unpack_archive(filepath, archives_folder + '/' + file_name)
                if not (format in all_formats):
                    all_formats.append(format)
                all_files["archives"].append(new_file_name)

            else:
                if not (format in unknown_formats):
                    unknown_formats.append(format)

        # recurring ? how to do that?
        else:
            if file == 'images' or file == 'documents' or file == 'audio' or file == 'video' or file == 'archives':
                continue
    
    # deleting empty folders
    entries2 = os.listdir(foldername)
    for file in entries2:
        filepath2 = foldername + '/' + file
        if (os.path.isdir(filepath2)) and (not os.listdir(filepath2)):
            shutil.rmtree(filepath2)

def main():
    sort_files(sys.argv[1])
    print(all_files)
    print(all_formats)
    print(unknown_formats)

if __name__ == '__main__':
    main()

