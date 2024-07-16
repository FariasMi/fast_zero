from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='lana',
        password='senha_segura@193',
        email='lana@mi.com.br',
    )

    session.add(user)
    session.commit()
    result = session.scalar(select(User).where(User.email == 'lana@mi.com.br'))

    assert result.username == 'lana'
