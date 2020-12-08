
import openpyxl


class HandExcel:
    def __init__(self, filename, sheetname):
        self.filename = filename
        self.sheetname = sheetname

    def open_excel(self):
        """打开excel表单"""
        # 设置为实例属性
        self.wb = openpyxl.load_workbook(self.filename)

        self.sh = self.wb[self.sheetname]

    def read_excel(self):
        """读取excel表格数据"""
        self.open_excel()

        '''
        1. 因为此处要用到 sh.rows
        2. 所以把 wb 和 sh 设置为实例属性，方便调用
        '''
        res = list(self.sh.rows)
        # 获取第一行的title

        # title = []
        # for i in res[0]:
        #     title.append(i.value)

        title = [i.value for i in res[0]] # 列表推导式，简化上面的for循环代码

        case_data = []  # 存放用例数据
        # 获取除第一行以外的所有行数据
        for i in res[1:]:
            # data = []
            # for j in i:
            #     data.append(j.value)
            data = [j.value for j in i]
            res = dict(zip(title, data))
            case_data.append(res)
        return case_data

    def write_excel(self, row, col, value):
        """excel写入数据"""
        self.open_excel()
        self.sh.cell(row=row, column=col, value=value)
        self.wb.save(self.filename)

if __name__ == '__main__':

    excel = HandExcel(r"D:\py31\git_code\py31_project\test_api4 _V3\data\case_data.xlsx", "login")

    res = excel.read_excel()
    print(res)
#
#     excel.write_excel(7, 2, "小白")
