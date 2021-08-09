def df_to_dict(df, col_keys="param", col_values="value"):
    d = dict(zip(df[col_keys], df[col_values]))
    return d


def convert_video(ffmpeg_path, input_fpfn, start, stop,
                  video_codec, video_param,
                  audio_codec, audio_param,
                  output_fp, output_fn, extension):
    import subprocess
    import os

    if not os.path.exists(ffmpeg_path):
        return "FAIL: ffmpeg_path does not exist"
    if not os.path.exists(input_fpfn):
        return "FAIL: input file does not exist"

    command = [ffmpeg_path,
               "-y", # overwrite output without asking
               "-i",
               input_fpfn]

    if start != "" and stop != "":
        command = command + ["-ss", # start time hh:mm:ss
                             start,
                             "-to", # stop time hh:mm:ss (not duration!)
                             stop]

    command = command + ["-c:v",
                         video_codec]

    if video_param != "":
        command = command + video_param.split(" ")

    command = command + ["-c:a",
                         audio_codec]
    if audio_param != "":
        command = command + audio_param.split(" ")

    command = command + [os.path.join(output_fp, output_fn) + "." + extension]

    print(subprocess.list2cmdline(command))
    subprocess.run(command)

    return "success"