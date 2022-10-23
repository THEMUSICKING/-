pass


'''Excel的操作'''
import xlrd

lsx = xlrd.open_workbook('12.xls')

sheet = lsx.sheet_by_index(0)

print(sheet.nrows)              # 打印行数
print(sheet.ncols)              # 打印列数

for _ in range(sheet.nrows):
    print(sheet.row_values(_))      # 打印行值


'''Json的操作'''
import json
dit = '[{"name": "jim","sex":"男"},{"name":"cj","sex": "女"}]'
json_lst = json.loads(dit)                          # 使用json.loads来将str, bytes or bytearray类型转化为json格式
print(json.dumps(json_lst,ensure_ascii=False))      # 使用json.dumps将json类型转化为字符串类型


'''XML文件的操作 '''
try:
    import xml.etree.cElementTree as ET         # 使用c语言模式
except:
    import xml.etree.ElementTree as ET          # 使用python的模式

tree = ET.parse('../11.xml')
root = tree.getroot()                           # 获取根
print(root.tag)
print(root.text)
print(root.attrib)
for child in root:                              # 获取根的子节点
    print(child.tag)
    print(child.attrib)
    print(child.text)


'''Yaml文件操作'''
import yaml
'''
对象：   键: 值

数组：     -值1
          -值2

数组的行内表示：
animal: [cat, dog]

复合结构：
        lagua:
          -RUby
          -dd
          -jj
        
        animal:
          YAML: dq
          aw: qw
'''
# yaml_str = "animal: cat"
yaml_str = open('../1.yaml','r',encoding='utf-8').read()
yaml_ob = yaml.load(yaml_str,Loader=yaml.FullLoader)            # yaml.load 加载yaml文件内容，Loader=yaml.FullLoader全导入
print(yaml_ob)
print(type(yaml_ob))