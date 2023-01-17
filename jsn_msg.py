class Messages:
    def __init__(self):
        pass

    @classmethod
    def key_exists_file(cls, key):
        print(f'The key "{key}" already exists in the json file.')

    @classmethod
    def key_exists_dict(cls, key):
        print(f'The key "{key}" already exists in the dictionary.')

    @classmethod
    def file_exists(cls, file_name):
        return f'The file "{file_name}" already exists.'

    @classmethod
    def file_do_not_exists(cls, file_name):
        return f'The file "{file_name}" do not exists.'

    @classmethod
    def overwrite_file(cls):
        return f'Do you want to overwrite the file?'

    @classmethod
    def overwrite_key(cls):
        return f'Do you want to overwrite the key?'

    @classmethod
    def file_saved(cls):
        return f'File saved.'

    @classmethod
    def action_canceled(cls):
        return f'Action canceled.'

    @classmethod
    def file_not_found(cls):
        return f'File not Found.'


if __name__ == '__main__':
    Messages.key_exists_dict(1)
    Messages.key_exists_file(2)
    Messages.file_exists(3)
