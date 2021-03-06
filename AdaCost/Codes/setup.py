from setuptools import setup, find_packages

setup(
    # Application details
    name="adacost",
    version="0.1.0",
    author="Joel Varghese",
    author_email="joelprince25@gmail.com",
    description="AdaCost - A variation of AdaBoost for classification problems with misclassification costs",
    include_package_data=True,

    # Dependencies
    packages=find_packages(),
    install_requires=[
            "pandas",
            "numpy",
            "scikit-learn"
    ]
)
