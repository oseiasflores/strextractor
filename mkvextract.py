import pathlib
import os 

video_list = [{'filename': str(video).replace('.mkv', ''),
               'path': f'{video}'} for video in pathlib.Path('./').glob('*.mkv')]
print(video_list)

def srtextract(video):
    return_code = os.system(f'mkvextract tracks {video["path"]} 2:{video["filename"]}.srt')
    os.system(f'mkdir {video["filename"]}_files')
    os.system(f'mv {video["path"]} {video["filename"]}.srt {video["filename"]}_files')

for video in video_list:
    srtextract(video)