import google_api
import send_email


def main():
    love_letter = google_api.get_love_letter()
    print(love_letter)

    send_email.send_love_letter(love_letter)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'error : {e}')
