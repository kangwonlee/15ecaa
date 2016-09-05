# -*- coding: utf8 -*-
# 위 주석은 이 .py 파일 안에 한글이 사용되었다는 점을 표시하는 것임
import os


def skip_this_path(path, png_path):
    skip_these = ('.git', '.idea', png_path)
    result = False
    for skip_this in skip_these:
        if skip_this in path:
            result = True
    return result


def mkdir(path):
    if os.path.exists(path):
        result = 'path %r already exists' % path
    elif not path:
        result = 'unable to create %r' % path
    elif not os.path.exists(path):
        split_path = os.path.split(path)
        if not os.path.exists(split_path[0]):
            return_value = mkdir(split_path[0])
            result = 'recursive %s' % return_value
        else:
            os.mkdir(path)
            result = 'created dir %s' % path
    else:
        result = "don't know what to do with %r" % path
    return result


def main():
    png_path = 'png'

    for dir_path, dir_names, file_names in os.walk(os.pardir):
        if not skip_this_path(dir_path, png_path):
            for file_name in file_names:
                add_utf8(dir_path, file_name)


def encoding_indicated(txt):
    def in_txt(encoding):
        return encoding in txt

    return any(map(in_txt, ('utf8', 'utf-8', 'cp949')))


def add_utf8(dir_path, file_name):
    if '.py' == os.path.splitext(file_name)[-1]:
        full_path = os.path.join(dir_path, file_name)
        with open(full_path, 'rt') as f:
            txt = f.read()
        if not encoding_indicated(txt):
            encoding_string = '# -*- coding: utf8 -*-\n'
            encoding_indicated_string = encoding_string + txt

            with open(full_path, 'wt') as f:
                f.write(encoding_indicated_string)


def move_png(dir_path, file_name, png_path):
    if '.png' == os.path.splitext(file_name)[-1]:
        png_full_path = os.path.join(dir_path, png_path)
        print(mkdir(png_full_path))
        source = os.path.join(dir_path, file_name)
        destination = os.path.join(dir_path, png_path, file_name)
        os.rename(source, destination)


if __name__ == '__main__':
    main()
