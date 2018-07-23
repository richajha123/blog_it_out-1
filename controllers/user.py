from passlib.hash import pbkdf2_sha256 as pwd_context

def login():
    response.title = T("Log In | BIO")

    form = SQLFORM.factory(
        Field('Email', type='string', requires=[IS_NOT_EMPTY(),IS_EMAIL()]),
        Field('Password', type='password', requires=IS_NOT_EMPTY()),
        Field('Terms_and_conditions', type='boolean', requires=IS_NOT_EMPTY())
    ).process()

    if form.accepted:
        rows = db().select(db.person.ALL)
        email_id = form.vars.Email
        password = form.vars.Password

        user_found = False
        for row in rows:
            if row.email == email_id:
                if pwd_context.verify(password, row.password):
                    session.flash = T("Welcome to Blog It Out")
                    user_found = True
                    redirect(URL('signup'))

        if not user_found:
            response.flash = T("Incorrect username or password!")

    elif form.errors:
        response.flash = T("Error in form!")

    return locals()


def signup():
    response.title = T("Sign up | BIO")

    form = SQLFORM.factory(
        Field('Email', type='string', requires=[IS_NOT_EMPTY(),IS_EMAIL()]),
        Field('Password', type='password', requires=IS_NOT_EMPTY()),
        Field('Password_again', type='password', requires=IS_NOT_EMPTY()),
        Field('Terms_and_conditions', type='boolean', requires=IS_NOT_EMPTY())
    ).process()

    if form.accepted:
        rows = db().select(db.person.ALL)
        email_id = form.vars.Email
        password = form.vars.Password
        password_again = form.vars.Password_again

        if password == password_again:
            crypted_password = pwd_context.hash(password)

            user_found = False
            for row in rows:
                if row.email == email_id:
                    response.flash = T("Email already exists!")
                    user_found = True

            if not user_found:
                form.vars.id = db.person.insert(**dict(email=email_id, password=crypted_password))
                session.flash = T("Welcome to Blog It Out")
                redirect(URL('login'))

        else:
            response.flash = T("Passwords don't match!")

    elif form.errors:
        response.flash = T("Error in form!")

    return locals()