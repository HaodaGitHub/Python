import tushare as ts
import matplotlib.pyplot as plt
from datetime import datetime

data = ts.get_hist_data('600848')
# ��ʱ�����н�������
data = data.sort_index()
#print(data.index)

#ǰ5����¼
#data = data.head(50)

xs = [datetime.strptime(d, '%Y-%m-%d').toordinal() for d in data.index ]
#print(xs)

plt.plot_date( xs , data['open'] , 'b-')
plt.gcf().autofmt_xdate()  # �Զ���ת���ڱ��
plt.show()
