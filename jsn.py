from jsn_basics import JsnActions
from jsn_check import Check
from jsn_msg import Messages


class Jsn:
    def __init__(self, file_name):
        self.file_name = file_name

    def save_file(self, dictionary):
        if Check.file_exist(self.file_name):
            print(Messages.file_exists(self.file_name))
            print(Messages.overwrite())
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



if __name__ == '__main__':
    dic1 = {'c': 1, 'd': 2}
    file_01 = Jsn('dic_for_test_01')
    file_01.save_file(dic1)

    #file_02 = Jsn('dic_for_test_02')
    #file_02.save_file(dic1)

