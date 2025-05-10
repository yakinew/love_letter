"""
This script orchestrates the generation and sending of a love letter.

It imports functions from the google_api and send_email modules to generate
a love letter using a language model and then send it via email.
"""

import google_api
import send_email


def main():
    """
    Main function to generate and send a love letter.

    This function calls google_api.get_love_letter() to generate the letter text,
    prints the letter to the console, and then uses send_email.send_love_letter()
    to send the letter.  It also includes error handling.
    """
    love_letter = google_api.get_love_letter()
    print(love_letter)

    send_email.send_love_letter(love_letter)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:  # pylint: disable=W0718
        print(f'error : {e}')
