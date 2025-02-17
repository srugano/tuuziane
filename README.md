ABOUT TUUZIANE
=========================


## Contributing

### System Requirements

- python 3.12
- [direnv](https://direnv.net/) - not mandatory but strongly recommended
- [uv](https://github.com/uvproject/uv)

## Configure development environment

**WARNING**
> Tuuziane implements **security first** policy. It means that configuration default values are "almost" production compliant.
>
> Es. `DEBUG=False` or `SECURE_SSL_REDIRECT=True`.
>
> Be sure to run `./manage.py env --check` and  `./manage.py env -g all` to check and display your configuration



### 1. Clone repo and install requirements
    git clone https://github.com/srugano/tuuziane
    uv create 3.12
    uv install
    uv activate in-project
    pre-commit install

### 2. configure your environment

Uses `./manage.py env` to configure your environment

    ./manage.py env > .evnvrc

Customize your env for development:

    export DEBUG=True
    export SESSION_COOKIE_NAME="hcr_test_session"
    export SESSION_COOKIE_DOMAIN=""
    export SESSION_COOKIE_SECURE=False
    export SECURE_HSTS_SECONDS=0
    export SECURE_HSTS_PRELOAD=False
    export CSRF_COOKIE_SECURE=False
    export SECURE_SSL_REDIRECT=False
    export CELERY_TASK_ALWAYS_EAGER=True


and check required (and optional) variables to put

    ./manage.py env --check


### 3. Run upgrade to run migrations and initial setup

    ./manage.py upgrade

### 4. (Optional) Create some sample data

    ./manage.py demo

> If `DEBUG=True` . Note that:

>   - If the username is ADMIN_EMAIL you will be superuser
>   - If username starts with `admin` will be created a superuser
>   - If username starts with `user`  will be created a standard user (no staff, no admin)
