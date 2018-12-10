# encoding : utf-8
import pandas as pd
# df.to_excel(excel_writer, sheet_name='Sheet1', na_rep='',
#             float_format=None, columns=None, header=True,
#             index=True, index_label=None, startrow=0, startcol=0,
#             engine=None, merge_cells=True, encoding=None,
#             inf_rep='inf', verbose=True, freeze_panes=None)
# excel_writer :文件路径
# sheet_name：工作表
# np_rep:默认缺省值
# float_format 默认无格式浮点数的字符串
# columns 可选要写如入的列
# header 布尔值或字符串列表，默认为True写出列名。如果给出了字符串列表，则假定它是列名的别名
# index default True写行名（索引）
# index_label
# startrow 左上角的单元格行转储数据框
# startcol  左上角的单元格列，用于转储数据框
# engine
# merge_cells
# encoding
# inf_rep
# verbose
# freeze_panes
columns = ["ID",
               "公共图节点数", "大图和新图的节点数最大", "大图和新图的节点数最小值",
               "公共图边数", "大图和新图的边数最大值", "大图和新图的边数最小值",
               ]
result=[[1,2.1,2.5,5.6,2.3,0.5,4.6]]
df = pd.DataFrame(result, columns=columns)
print(df.shape[0])
df.to_excel("F:\python_code\s.xls",startrow=df.shape[0]-1)
result2=[[0,1,5,4,8,5,6]]
df = pd.DataFrame(result+result2, columns=columns)
df.to_excel("F:\python_code\s.xls",startrow=df.shape[0]+1 ,header=None)