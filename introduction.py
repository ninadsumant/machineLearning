from sklearn.datasets import load_iris
iris_dataset = load_iris()
print("Keys of iris_dataset:\n", iris_dataset.keys())
print(iris_dataset['DESCR'][:193] + "\n...")
print("Target names:", iris_dataset['target_names'])
print("Feature names:\n", iris_dataset['feature_names'])
print("Type of data:", type(iris_dataset['data']))
print("Shape of data:", iris_dataset['data'].shape)
print("First five rows of data:\n", iris_dataset['data'][:5])
