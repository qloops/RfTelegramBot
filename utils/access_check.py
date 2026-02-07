import database
import constants


def access_check(
        user: database.models.User,
        role: constants.UserAccessRoles
) -> bool:
    """
    Checks if the user has access based on their role.

    `(3)GOD > (2)ADMINISTRATOR > (1)USER`

    Args:
        user: The user to check access for.
        role: The required access role.

    Returns:
        bool: True if the user has enough access, False otherwise.
    """
    # I don't know what the fuck is going on here, 
    # then I'll figure it out.
    return user.access_level >= role
