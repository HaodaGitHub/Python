import tushare as ts
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd

data = ts.get_hist_data('600848')
print(data.index)
#ǰ5����¼
data = data.head(5)

data['open'].plot()

plt.gcf().autofmt_xdate()  # �Զ���ת���ڱ��
plt.show()



