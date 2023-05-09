import os, sys, shutil
from pathlib import Path

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

def moving_files(foldername2, img_folder, doc_folder, audio_folder, video_folder):
    folder = Path(foldername2)

    for el in folder.glob("**/*"):
        ext = el.suffix.lower()
        new_file_name2 = normalize(el.name) + ext
        if ext == '.jpeg' or ext == '.jpg' or ext == '.png' or ext == '.svg':
                shutil.move(el, img_folder + '/' + new_file_name2)
                if not (ext in all_formats):
                    all_formats.append(ext)
                all_files["images"].append(new_file_name2 + ext)
        elif ext == '.doc' or ext == '.docx' or ext == '.txt' or ext == '.pdf' or ext == '.xlsx' or ext == '.pptx':
                shutil.move(el, doc_folder + '/' + new_file_name2)
                if not (ext in all_formats):
                    all_formats.append(ext)
                all_files["documents"].append(new_file_name2 + ext)
        elif ext == '.mp3' or ext == '.ogg' or ext == '.wav' or ext == '.amr' :
                shutil.move(el, audio_folder + '/' + new_file_name2)
                if not (ext in all_formats):
                    all_formats.append(ext)
                all_files["audio"].append(new_file_name2 + ext)
        elif ext == '.avi' or ext == '.mp4' or ext == '.mov' or ext == '.mkv':
                shutil.move(el, video_folder + '/' + new_file_name2)
                if not (ext in all_formats):
                    all_formats.append(ext)
                all_files["video"].append(new_file_name2 + ext)
        elif ext == '.zip' or ext == '.gz' or ext == '.tar':
            continue
        else:
            if not (ext in unknown_formats):
                    unknown_formats.append(ext)

def unzip_files(foldername2, archives_folder):
    folder = Path(foldername2)

    for el in folder.glob("**/*"):
        ext = el.suffix.lower()
        if ext == '.zip' or ext == '.gz' or ext == '.tar':
            shutil.unpack_archive(el, archives_folder + '/' + el.name.rstrip(ext))
            if not (ext in all_formats):
                all_formats.append(ext)
                all_files["archives"].append(el.name+ext)

def delete_empty_folders(foldername): # this unfortunately is work not 100% correct
    for root, d_names, f_names in os.walk(foldername):
        if not os.listdir(root) and root.find('archives') == -1:
            shutil.rmtree(root)

def create_folders(foldername, img_folder, doc_folder, audio_folder, video_folder, archives_folder):
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

def sort_files(foldername):
    img_folder = foldername + '/images'
    doc_folder = foldername + '/documents'
    audio_folder = foldername + '/audio'
    video_folder = foldername + '/video'
    archives_folder = foldername + '/archives'

    create_folders(foldername, img_folder, doc_folder, audio_folder, video_folder, archives_folder)
    moving_files(foldername, img_folder, doc_folder, audio_folder, video_folder)
    unzip_files(foldername, archives_folder)
    delete_empty_folders(foldername)

def main():
    if len(sys.argv) != 2:
        print("Please add 2 arguments!")
        quit()
    sort_files(sys.argv[1])
    print(all_files)
    print(all_formats)
    print(unknown_formats)

if __name__ == '__main__':
    main()

