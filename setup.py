from setuptools import setup, find_packages

setup(
    name="social_media_etl",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "praw==7.7.1",
        "python-dotenv==1.0.0",
        "boto3==1.28.44",
        "numpy==1.24.3",
        "pandas==2.0.3",
        "kafka-python==2.0.2",
        "pyspark==3.5.0",
        "textblob==0.17.1",
        "nltk==3.8.1"
    ]
) 