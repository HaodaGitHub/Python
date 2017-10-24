from sklearn.datasets import load_iris
from sklearn import tree
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

#2 ѵ����ɺ󣬵��� iris ���ݼ�ѵ����������
from sklearn.externals.six import StringIO
with open("iris.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)

#3 dot -Tpdf iris.dot -o iris.pdf

#���֮��ģ�Ϳ��������������ࣺ
predict = clf.predict(iris.data[:1, :])
print( 'predict=',predict )

#ÿ������ĸ����ܱ�Ԥ�⣬��ĳ��Ҷ���У��÷���������ռ�ȡ�
predict_proba = clf.predict_proba(iris.data[:1, :])
print( 'predict_proba=',predict_proba )
