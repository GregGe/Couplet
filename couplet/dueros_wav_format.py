import os
import sys

import pydub
from pydub import AudioSegment

reload(sys)
sys.setdefaultencoding('utf8')

# pydub.AudioSegment.converter = 'D:\\soft\\ffmpeg-20180919-49c67e7-win64-static\\bin\\ffmpeg.exe'
file_prefix = u"couplet"

target_file_pofix = "wav"
# 2 byte (16 bit) samples
target_sample_width = 2
# 16 kHz frame rate
target_frame_rate = 16000
# stereo
target_channels = 1


def main():
    # print("path:")
    # base_dir = input("please enter your dir:")
    convert_in_dir('audio')
    print("job finish")


def convert_in_dir(base_dir):
    if os.path.isfile(base_dir):
        print(u'starting:')
        convert(base_dir, None)
    else:
        file_list = os.listdir(base_dir)
        for i in range(len(file_list)):
            f = file_list[i]
            if f.endswith(".wav") or f.endswith(".mp3"):
                print(u"format %d : %s" % (i, f))
                convert(base_dir, f)


def convert(dir, file_name):
    file = (dir if (file_name is None) else dir + "/" + file_name)
    namef, name_sufix = os.path.splitext(file_name)
    save_dir = '%s/%s' % (dir, u"dueros")
    if os.path.exists(save_dir):
        print(save_dir + " existed path")
    else:
        os.mkdir(save_dir)

    sound = AudioSegment.from_file(file)
    new_sound = sound.set_frame_rate(target_frame_rate).set_channels(target_channels).set_sample_width(
        target_sample_width)
    save_name = '%s/%s.%s' % (save_dir, file_prefix + namef, target_file_pofix)
    new_sound.export(save_name, format="wav")
    print(u'complete')


if __name__ == '__main__':
    main()
