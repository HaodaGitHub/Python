import numpy as np
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
#�������
clf.fit(X, Y)

print( "* Ԥ�������(�����ĸ������ǩ) =>" , clf.predict([[-0.8, -1]]))
print( "* Ԥ�����(���ڷ����ǩ�ĸ���) =>", clf.predict_proba([[-0.8, -1]]))

# �ѿ�ѧ���㷨����ת��Ϊ����������
def as_num(x):
    y='{:.10f}'.format(x) # 10f��ʾ����10λС�����float��
    return(y)


#print( as_num(  -5.05653266e-08 ) )
#print( as_num( -1.67999998e+01 ) )