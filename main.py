from PIL import Image
import os


def convert(filename, extension, new_format):
    img = Image.open(f'./test/{filename}{extension}').convert('RGB')
    img.save(f'./dest/{filename}.{new_format}', new_format)


def main():
    directory = input('Enter a Directory\n> ')

    print('Contents: ')

    num = 0
    for file in os.listdir(directory):
        num += 1
        filename, extension = os.path.splitext(file)

        if extension == '.PNG':
            print(' {0}.\t{1}{2}'.format(num, filename, extension))

            convert(filename, extension, 'JPEG')

if __name__ == '__main__':
    main()

    print('Convertion Done')
