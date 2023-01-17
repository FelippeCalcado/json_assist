class Check:
    @classmethod
    def file_exist(cls, file):
        try:
            with open(file) as f:
                pass
            return True
        except:
            return False

    @classmethod
    def check_key_in_dictionary(cls):
        pass