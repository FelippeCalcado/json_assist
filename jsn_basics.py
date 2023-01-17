import json


class JsnActions:
    def __init__(self, file_name):
        self.file_name = file_name

    @classmethod
    def dic_to_json(self, dictionary):
        json_file = json.dumps(dictionary,
                   indent=4,
                   sort_keys=True)
        return json_file

    def open_file(self):
        with open(self.file_name, 'r') as file:
            dictionary = json.load(file)
        return dictionary

    def save_file(self, json_file):
        with open(self.file_name, 'w') as file:
            file.write(json_file)


if __name__ == '__main__':
    dic1 = {'a': 1, 'b': 2}
    jf = JsnActions.dic_to_json(dic1)
    print(type(dic1))
    print(type(jf))
    jsn_ass = JsnActions('dic_for_test_01')
    jsn_ass.save_file(jf)
    dic1B = jsn_ass.open_file()
    print(dic1B)
    print(dic1)

