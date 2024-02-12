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
        "distro==1.9.0",
    ],
    version="0.1.0",
    author="ASivashs",
    author_email="anton.sivashko@gmail.com",
    description="Jenkins manager task.",
    license="MIT"
)
