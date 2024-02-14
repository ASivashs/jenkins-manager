import jenkins


def create_user(
        admin_password: str, 
        username: str="user", 
        user_password: str="user"
    ):
    server = jenkins.Jenkins(
        'http://127.0.0.1:8080', 
        username='admin', 
        password=admin_password
    )
    server.create_user(
        username, 
        user_password, 
        "User Resu",
    )


def create_guest(    
        admin_password: str, 
        username: str="Guest", 
        user_password: str="guest"
    ):
    server = jenkins.Jenkins(
        'http://127.0.0.1:8080', 
        username='admin', 
        password=admin_password
    )
    server.create_guest(
        username, 
        user_password, 
        "Guest Tseug",
    )
