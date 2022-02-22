import pytesseract
import cv2
import os


def read_image(path_image: str, txt_name: str):
    '''
    Function read text from imagine.
    '''
    img = cv2.imread(path_image)
    text = pytesseract.image_to_string(img, lang='ukr')
    with open(txt_name, 'w', encoding='utf-8') as file:
        file.write(text)


def read(path_to_folder:str):
    '''
    Function that defines path to the file.
    Call function which read text from imagine.
    '''
    folder, smth, files = list(os.walk(path_to_folder))[0]
    os.mkdir(path_to_folder + '_2' )
    for i in range(len(files)):
        path_image = path_to_folder + '/' + files[i]
        txt_name = path_to_folder + '_2' + '/file' + str(i + 1) + '.txt'
        read_image(path_image, txt_name)

if __name__ == '__main__':
    path_to_folder = input()
    read(path_to_folder)