from app.models.user import User


async def current_user() -> User:
    return User(
        id=1,
        email='test@example.com',
        hashed_password='fake',
        is_active=True,
        is_superuser=False,
        is_verified=True,
    )


__all__ = ['User', 'current_user']
