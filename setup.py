from setuptools import setup, find_packages


setup(
    # name of package
    name="jenkins-manager",
    # packages (directories) to be included
    packages=find_packages(),
    # script entry point
    entry_points={
        "console_scripts": [
            "jenkins-manager = jenkins-manager.jenkins_manager:main",
        ],
    },
    # package dependencies
    install_requires=[
        "aiohttp==3.9.3",
        "aiosignal==1.3.1",
        "attrs==23.2.0",
        "certifi==2024.2.2",
        "charset-normalizer==3.3.2",
        "frozenlist==1.4.1",
        "idna==3.6",
        "multidict==6.0.5",
        "requests==2.31.0",
        "urllib3==2.2.0",
        "yarl==1.9.4",
    ],
    version="0.1.0",
    author="ASivashs",
    author_email="anton.sivashko@gmail.com",
    description="Jenkins manager task.",
    license="MIT"
)
