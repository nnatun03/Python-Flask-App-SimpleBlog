
import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail


def save_picture(form_picture):
    """
    This function takes an image file from a form, generates a random filename for it,
    resizes it to 125x125 pixels, and saves it to the 'static/profile_pics' directory.

    Args:
        form_picture (FileStorage): An image file from a form.

    Returns:
        str: The new filename of the picture.
    """
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


def send_reset_email(user):
    """
    This function generates a password reset token for a user, creates a password reset email
    with the token embedded in a URL, and sends the email to the user's registered email address.

    Args:
        user (User): The user who requested a password reset.
    """
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com',
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)