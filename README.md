# Planning

## Pages required:

1. HOME (default/index)
2. LOGIN (user/login)
3. SIGNUP (user/signup)
4. USER PROFILE (user/profile)

## Requirements for **v0.1**:

#### HOME

1. When user opens the website for the first time, it should go directly to the *HOME* page.	=> @DONE
2. HOME page should have a link (top-right) which points it to *LOGIN* page.	=> @DONE
3. If user is logged in, then instead of link for signin, user_email should be displayed. (use session object)
4. If the logged in user clicks on his email on top-right corner, he should be redirected to *USER PROFILE* page.

#### LOGIN

1. User should not be able to jump directly to this page using URL. Previous page must be *HOME* page.
2. If user enters email_id, password and then clicks on Submit button. Then he/she should be redirected to *HOME* page.	=> @DONE
3. For new user, there should be an option for signup.	=> @DONE
4. If user clicks on signup link, he should be redirected to *SIGNUP* page.	=> @DONE
5. User should have an option of  `forgot password`.
6. If user clicks on `forgot password`, then an email should be sent with the new `random` password.

#### SIGNUP

1. User should not be able to jump directly to this page using URL. Previous page must be *LOGIN* page.
2. User should not be able to enter an already existing email.	=> @DONE
3. Email verification should be completed first before user is able to login.
4. User should have an option of  `forgot password`.

#### USER PROFILE

1. User should be able to reset the password.
2. User should be able to view/edit/archive his previous posts.
3. User should have an option of writing new post. (Add TextEditor)
4. User should be able to update his personal info like pen name, Mobile number, profile pic etc.