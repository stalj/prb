required_permissions = {"read", "write", "execute"}
user_permissions = {"read", "write"}

has_permissions = user_permissions.issubset(required_permissions)  
print(has_permissions) 