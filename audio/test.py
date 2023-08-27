import json

def get_json_data():
    file = open("audio/lofi-girl.json")
    complete_json_data = json.load(file)

    if complete_json_data is None:
        complete_json_data = {}
        return complete_json_data
    elif complete_json_data is not None:
        # you still need to get the last element of the list
        return complete_json_data
    
def get_index():
    complete_json_data = get_json_data()
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

def test_json_data():
    complete_json_data = get_json_data()
    index = get_index()

    for i in range(5):
        json_data = {
            "title": f"title{index}",
            "song": f"song{index}",
            "artist": f"artist{index}",
            "i_url": f"i_url{index}",
            "x_url": f"x_url{index}",
        }
        complete_json_data[index] = (json_data)
        write_json(complete_json_data)
        index += 1

def main():
    test_json_data()
    print(json.dumps(get_json_data(), indent=4))

if __name__ == "__main__":
    main()

