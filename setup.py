from setuptools import setup, find_packages


setup(
    # name of package
    name="jenkins_manager",
    # packages (directories) to be included
    packages=find_packages(),
    # script entry point
    entry_points={
        "console_scripts": [
            "jenkins-manager = jenkins_manager.jenkins_manager:cli",
        ],
    },
    # package dependencies
    install_requires=[
        "click==8.1.7",
        "certifi==2024.2.2",
        "charset-normalizer==3.3.2",
        "distro==1.9.0",
        "idna==3.6",
        "multi_key_dict==2.0.3",
        "pbr==6.0.0",
        "python-jenkins==1.8.2",
        "requests==2.31.0",
        "six==1.16.0",
        "urllib3==2.2.0",
    ],
    version="0.1.0",
    author="ASivashs",
    author_email="anton.sivashko@gmail.com",
    description="Jenkins manager task.",
    license="MIT",
)
