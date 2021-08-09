import pandas as pd
from func import *

dfg = pd.read_excel("config.xlsx", sheet_name="general")
d = df_to_dict(dfg)

dff = pd.read_excel("config.xlsx", sheet_name="files", na_values="")
dff = dff.fillna('')


for index, row in dff.iterrows():
    print("Processing: " + row['destination_file'])

    s = convert_video(ffmpeg_path=d['ffmpeg_path'],
                      input_fpfn=row['source_file'],
                      start=row['start'],
                      stop=row['stop'],
                      video_codec=row['vcodec'],
                      video_param=row['vparam'],
                      audio_codec=row['acodec'],
                      audio_param=row['aparam'],
                      output_fp=row['destination_folder'],
                      output_fn=row['destination_file'],
                      extension=row['container'])
    print(s)

