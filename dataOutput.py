from openpyxl import workbook  # 写入Excel表所用
from openpyxl import load_workbook  # 读取Excel表所用

class DataOutput(object):

    def __init__(self):
        self.datas=[]
        self.wb = workbook.Workbook()  # 创建Excel对象
        self.ws = self.wb.active  # 获取当前正在操作的表对象
        self.ws.append(['类别', '问题编号', '问题链接', '问题','问题详情','回答总数', '回答编号', '回答', '回答时间','点赞数','踩数', '最佳答案'])
     
    def collect_data(slef,data):
        if data is None:
            return 
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html','w')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        for data in self.datas:
            for name in data.keys():
                fout.write("<td>%s</td>"%data[name],encode('utf-8'))
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()

    def output_excel(self,datas,path):
        for i in datas:
            self.ws.append(i)
        self.wb.save(path)


