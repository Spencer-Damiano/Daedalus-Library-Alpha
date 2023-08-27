from pytube import Playlist, YouTube
import json
import os

"""
This uses pytube to get all videos from Lofi Girl's Library playlist and downloads the audio only. 
It also catalogues the videos in a json file that contains the title, author, and url of the video.

copyright ref: https://lofigirl.com/use-the-music/
"""

def format_json(yt):

    title = yt.title
    artist = title.split("-")[0]
    song = title.split("-")[1]
    x_url = yt.watch_url
    i_url = f"audio/files/{yt.title}"

    json_data = {
        "title": title,
        "song": song,
        "artist": artist,
        "i_url": i_url,
        "x_url": x_url,
    }

    test_title = title
    test_reconstructed_title = f"{artist}-{song}"

    if test_title == test_reconstructed_title:
        return json_data
    else:
        # print(f"Error: ({test_title}) != ({test_reconstructed_title})")
        #non_formattable += 1
        pass

def write_json(json_data):
    json_str = json.dumps(json_data, indent=4)
    json_file = open("audio/lofi-girl.json", "r+")
    json_file.write(json_str)
    json_file.close()

def download_audio(yt):
    # extract only audio
    video = yt.streams.filter(only_audio=True, file_extension="mp4" ).first()

    # replace destination with the path where you want to save the downloaded file
    destination = "audio/files"
    
    # download the file
    out_file = video.download(output_path=destination)
    
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp4'
    if not os.path.exists(new_file):
        os.rename(out_file, new_file)
    
    # result of success
    print(yt.title + " has been successfully downloaded.")

def set_json_data():
    file = open("audio/lofi-girl.json")
    complete_json_data = json.load(file)

    if complete_json_data is None:
        complete_json_data = {}
        return complete_json_data
    elif complete_json_data is not None:
        # you still need to get the last element of the list
        return complete_json_data

def get_index(complete_json_data):
    complete_json_data = complete_json_data
    index = 0

    for i in range(len(complete_json_data)):
        index += 1

    if index == 0:
        return index
    elif index > 0:
        index += 1
        return index

def write_json(json_data):
    json_str = json.dumps(json_data, indent=4)
    json_file = open("audio/lofi-girl.json", "r+")
    json_file.write(json_str)
    json_file.close()

def main():

    # Lofi Girls Library Playlist URL 
    playlist_var = Playlist("https://www.youtube.com/playlist?list=PLofht4PTcKYnaH8w5olJCI-wUVxuoMHqM")

    # This is for testing purposes VVV
    # non_formattable = 0

    complete_json_data = set_json_data()
    index = get_index(complete_json_data)
    print(index)

    playlist_len = len(playlist_var)


    for i in range(index, playlist_len): 
        yt = YouTube(playlist_var[i])

        if "-" in yt.title:
            json_data = format_json(yt)
            complete_json_data[index] = json_data
            write_json(complete_json_data)
            index += 1 

            download_audio(yt)
        elif "–" in yt.title:
            yt.title = yt.title.replace("–", "-")

            json_data = format_json(yt)
            complete_json_data[index] = json_data
            write_json(complete_json_data)
            index += 1
            
            download_audio(yt)
        else:
            # This is for testing purposes (used because of bug in pytube library, doesn't always read the titles of some videos)
            # print(f"Error: ({yt.title}) does not contain a '-' or '–' character.")
            # non_formattable += 1 
            pass

    # write_json(complete_json_data)
    # print(json.dump s(complete_json_data, indent=4))
    print("Done!")



if __name__ == "__main__":
    main()