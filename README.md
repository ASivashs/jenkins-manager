### About 

This script provide functions for manage Jenkins application. You can install Jenkins with dependencies and delete Jenkins with one command.

### Install 

To install this script run: 

```
pip3 setup.py .
```

To check working run: 

```
jenkins_manager --help
```

### Usage

In this script you can specify next parameters:

1) create-users --- Create users in Jenkins (default: user, guest).
2) install --- Install LTS version of Jenkins with dependencies.
3) uninstall --- Uninstall Jenkins with files.
4) verify --- Verifying security policy.

Using script:

Jenkins install
```
jenkins_manager install
```

Jenkins uninstall
```
jenkins_manager uninstall
```
