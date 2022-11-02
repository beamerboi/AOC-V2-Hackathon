## **JWT Endpoints**
| Create a JWT|`auth/jwt/create/` | POST Request |

| Refresh Token|`auth/jwt/refresh/`| POST Request |

| Verify Token |`auth/jwt/verify/`| POST Request |
## **Base Endpoints**

| Create User |`auth/users/`| POST Request |

| Activate User |`auth/activation/`| POST Request |

| User Resend Activation E-mail |`auth/users/resend_activation/`| POST Request |

| Reset Password |`auth/users/reset_password/`| POST Request |

| Reset Password Confirmation |`auth/users/reset_password_confirm/`| POST Request |

## **Required fields**

Create the JWT: `email` and `password`

Refresh Token:  `refresh`

Verify Token: `access`

Create User: `email`, `first_name`, `last_name`, `domain`, `phone`, `password` and `re_password`

Activate User: `uid`(can be found in the url sent through email as 
follows `activate/{uid}/{token}`) and `token` (sent through email)

User Resend Activation E-mail:  `email`

Reset Password:  `email`

Reset Password Confirmation: `uid `(can be found in the url sent through email as follows `activate/{uid}/{token}`), `token` (sent through email), `new_password`, and `re_new_password`

Password: should be `alphanumeric` with a `symbol` and **it should be different** from the `first_name`

## **Max Length**

`first_name`: 256 characters long

`last_name`: 256 characters long

`phone`: 8 characters long
