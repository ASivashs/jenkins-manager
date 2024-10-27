DEB_DISTRO = (
        "ubuntu", "debian", "linuxmint", "raspbian",
    )
RHL_DISTRO = (
        "rhel", "centos", "fedora", "amzn", "oracle"
    )
SUSE_DISTRO = (
        "sles", "opensuse", "suse",
)
ARCH_DISTRO = (
        "arch", "altlinux",
)

LTS_JENKINS_DEB_KEY = "https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key"
LTS_JENKINS_DEB_BINARY = "https://pkg.jenkins.io/debian-stable binary/"
LTS_JENKINS_DEB_KEYRINGS_PATH = "/usr/share/keyrings/jenkins-keyring.asc"
JENKINS_GPG = "/etc/apt/sources.list.d/jenkins.list"

LTS_JENKINS_RPM_KEY = "https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key"
LTS_JENKINS_RPM_REPO = "https://pkg.jenkins.io/redhat-stable/jenkins.repo"
LTS_JENKINS_RPM_KEYRINGS_PATH = "/etc/yum.repos.d/jenkins.repo"

diriterdir = ("admin", "user", "guest")
