from __future__ import absolute_import

import pytest

from .app import setup, teardown

from app import create_app
from app.models import db, Framework


@pytest.fixture(autouse=True, scope='session')
def db_migration(request):
    setup()
    request.addfinalizer(teardown)


@pytest.fixture(scope='session')
def app(request):
    return create_app('test')


def _update_framework(request, app, status, framework_slug):
    with app.app_context():
        framework = Framework.query.filter(
            Framework.slug == framework_slug
        ).first()
        original_framework_status = framework.status
        framework.status = status

        db.session.add(framework)
        db.session.commit()

    def teardown():
        with app.app_context():
            framework = Framework.query.filter(
                Framework.slug == framework_slug
            ).first()
            framework.status = original_framework_status

            db.session.add(framework)
            db.session.commit()

    request.addfinalizer(teardown)


@pytest.fixture(params=[('live', 'digital-outcomes-and-specialists')])
def live_framework(request, app):
    _update_framework(request, app, request.param[0], request.param[1])


@pytest.fixture(params=[('expired', 'digital-outcomes-and-specialists')])
def expired_framework(request, app):
    _update_framework(request, app, request.param[0], request.param[1])


@pytest.fixture()
def update_framework(request, app):
    def inner_update_framework(status='live', framework_slug='digital-outcomes-and-specialists'):
        with app.app_context():
            framework = Framework.query.filter(
                Framework.slug == framework_slug
            ).first()
            original_framework_status = framework.status
            framework.status = status

            db.session.add(framework)
            db.session.commit()

        def teardown():
            with app.app_context():
                framework = Framework.query.filter(
                    Framework.slug == framework_slug
                ).first()
                framework.status = original_framework_status

                db.session.add(framework)
                db.session.commit()

        request.addfinalizer(teardown)

    return inner_update_framework

