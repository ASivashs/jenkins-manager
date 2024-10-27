### About 

This script provide functions for manage Jenkins application. You can install Jenkins with dependencies and delete Jenkins with one command.

### Install 

To install this script run: 

```
pip3 install .
```

To check working run: 

```
jenkins-manager --help
```

### Usage

In this script you can specify next parameters:

1) install – Install LTS version of Jenkins with dependencies.
2) uninstall – Uninstall Jenkins with files. 

Using script:

Jenkins install
```
jenkins-manager install --mode [lts, weekly] [OPTIONAL]
```

Jenkins uninstall
```
jenkins-manager uninstall
```

Get help
```
jenkins-manager --help
```
