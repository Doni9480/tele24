import json


class WriteRead:
    @staticmethod
    def read_write_text_file(file: str = 'data.txt', mod: str = 'r', encoding: str = 'utf-8',
                             data_for_write=None):
        with open(f"{file}", f"{mod}", encoding=f"{encoding}") as file:
            if mod == 'r':
                return file.read()
            elif mod == 'w':
                file.write(str(data_for_write))
                return 'Успех!'
            else:
                return 'Не правелные типы данных!'

    # @staticmethod
    def read_write_json_file(self, file: str = 'data.json', mod: str = 'r', encoding: str = 'utf-8',
                             data_for_write: dict = None, indent: int = 4, ensure_ascii: bool = False):

        with open(f"{file}", mod, encoding=encoding) as file:
            if mod == 'r':
                self.json_dict = json.load(file)
                return self.json_dict
            elif mod == 'w' and data_for_write:
                json.dump(data_for_write, file, indent=indent, ensure_ascii=ensure_ascii)
                return 'Успех!'
            else:
                return 'Не правелные типы данных!'

    def check_user_id(self,user_id):
        rez = WriteRead().read_write_json_file()
        for k,v in rez.items():
            if v == user_id:
                return False
            else:
                return rez

def main():
    rez = WriteRead().read_write_json_file()
    if rez:
        rez = WriteRead().read_write_json_file(mod='w', data_for_write={**rez,'c': 43, 'f': 66})


    print(rez)


if __name__ == '__main__':
    main()
