DEB_DISTRO = (
        "ubuntu", "debian",
    )
RPM_DISTRO = (
        "CentOS", "Red Hat", "Arch Linux", "OpenSUSE", 
        "Amazon Linux", "Azure Linux",
    )

LTS_JENKINS_KEY = "https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key"
LTS_JENKINS_BINARY = "https://pkg.jenkins.io/debian-stable binary/"
JENKINS_KEYRINGS_PATH = "/usr/share/keyrings/jenkins-keyring.asc"
JENKINS_GPG = "/etc/apt/sources.list.d/jenkins.list"
