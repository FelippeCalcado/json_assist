from jsn_basics import JsnActions
from jsn_check import Check
from jsn_msg import Messages


class Jsn:
    def __init__(self, file_name):
        self.file_name = file_name

    def save_file(self, dictionary):
        if Check.file_exist(self.file_name):
            print(Messages.file_exists(self.file_name))
            print(Messages.overwrite_file())
            resp = input('y/n: ')
            if resp == 'y' or resp == 'Y':
                json_obj = JsnActions.dic_to_json(dictionary)
                JsnActions(self.file_name).save_file(json_obj)
                print(Messages.file_saved())
            elif resp == 'n' or resp == 'N':
                print(Messages.action_canceled())
        else:
            print(Messages.file_do_not_exists(self.file_name))
            json_obj = JsnActions.dic_to_json(dictionary)
            JsnActions(self.file_name).save_file(json_obj)
            print(Messages.file_saved())

    def read_file(self):
        if Check.file_exist(self.file_name):
            print(Messages.file_exists(self.file_name))
            dic = JsnActions(self.file_name).open_file()
            return dic

    def add_key_to_file(self, new_key, value):
        if Check.file_exist(self.file_name):
            print(Messages.file_exists(self.file_name))
            file = JsnActions(self.file_name)
            dic = JsnActions(self.file_name).open_file()
            if Check.check_key_in_dictionary(new_key, dic):
                print(Messages.overwrite_key())
                respk = input('y/n: ')
                if respk == 'y' or respk == 'Y':
                    file.add_key(dic, new_key, value)
                    json_obj = JsnActions.dic_to_json(dic)
                    JsnActions(self.file_name).save_file(json_obj)
                    #respk = 0
                else:
                    pass
            else:
                file.add_key(dic, new_key, value)
                json_obj = JsnActions.dic_to_json(dic)
                JsnActions(self.file_name).save_file(json_obj)
        else:
            print(Messages.file_not_found())
            print(Messages.action_canceled())




if __name__ == '__main__':
    '''dic1 = {'c': 1, 'd': 2}'''
    file_01 = Jsn('dic_for_test_01')
    '''file_01.save_file(dic1)
    dic2 = {'a': -1}
    file_02 = Jsn('dic_for_test_01').read_file()
    print('file2 =', file_02)'''

    file_01.add_key_to_file('a', 5)
    file_02 = Jsn('dic_for_test_01').read_file()
    print('file2 =', file_02)

    file_01.add_key_to_file('a', -1)
    file_02 = Jsn('dic_for_test_01').read_file()
    print('file2 =', file_02)


