import tushare as ts
import matplotlib.pyplot as plt

data = ts.get_hist_data('600848')
# ��ʱ����н�������
data = data.sort_index()
print(data)


print(data.index)
#ǰ50����¼
#data = data.head(50)

data['open'].plot()

plt.gcf().autofmt_xdate()  # �Զ���ת���ڱ��
plt.show()
