import tushare as ts
import matplotlib.pyplot as plt
from datetime import datetime

data = ts.get_hist_data('600848')
print(data.index)
data = data.head(5)
xs = [datetime.strptime(d, '%Y-%m-%d').date() for d in data.index ]
print(xs)

plt.plot( xs , data['open'])
plt.gcf().autofmt_xdate()  # �Զ���ת���ڱ��
plt.show()
