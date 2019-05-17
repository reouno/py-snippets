from typing import Text

def get_user_confirmation(confirmation_msg: Text, refused_msg: Text) -> bool:
    '''require YES/NO answer on console
    '''
    while True:
        choice = input('{} [y/N]: '.format(confirmation_msg))
        if choice.upper() in ['Y','YES']:
            return True
        elif choice.upper() in ['N','NO']:
            print(refused_msg)
            return False


if __name__ == '__main__':
    confirmation = 'Delete this file?'
    refused = 'Cannot delete the file. Delete it or specify another file path and try again.'
    print(get_user_confirmation(confirmation, refused))
