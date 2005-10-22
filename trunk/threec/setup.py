from setuptools import setup, find_packages

setup(
    name="threec",
    version="1.0",
    #description="An open source automatic coding competition system",
    #author="Gottlieb & Renaud",
    #author_email="rrenaud@gmail.com",
    #url="",
    setup_requires = ["TestGears"],
    install_requires = ["TurboGears == 0.5.0"],
    scripts = ["threec-start.py"],
    packages=find_packages(),
    package_data = {'' : ["*.kid", "*.js", "*.html"]},
    )
    
