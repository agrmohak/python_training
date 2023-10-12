import pyodbc as db
import utils
from books import *
from author import *
from reviews import *
from users import *

command_registry = {
    "add_authors" :{'func':add_author, 'args':['name', 'bio']},
    "remove_authors" :{'func':remove_author, 'args':['author_id']},
    "get_author_by_id" :{'func':get_author_by_id, 'args':['author_id']},
    "get_all_authors" :{'func':get_all_authors, 'args':[]},
    "add_books" :{'func':add_book, 'args':['isbn','title','author_id']},
    "remove_books" :{'func':remove_book, 'args':['book_id']},
    "get_all_books" :{'func':get_all_books, 'args':[]},
    "get_book_by_authorid" :{'func':get_books_by_authorid, 'args':['author_id']},
    "get_book_reviews" :{'func':get_book_review, 'args':['book_id']},
    "add_book_review" :{'func':add_book_review, 'args':['book_id','user_id','user_pass','rating','user_text']},
    "add_new_user" :{'func':add_new_user, 'args':['name','email','password']},
    "get_all_user" :{'func':get_all_users,'args':[]},
    "get_user_review" :{'func':get_user_review,'args':['user_id']}
}

def main():
    with utils.db_connect() as connection:
        cursor = connection.cursor()
        while True:
            user_input = input("db> ")
            task = user_input.split(' ')
            command, input_args = task[0].strip(), task[1:]
            final_args = input_args
            try:
                if command.lower() in ["quit", "exit", "bye"]:
                    break
                task_helper = command_registry[command.lower()]

                if len(input_args) < len(task_helper['args']):
                    for arg in task_helper['args'][len(input_args):]:
                        final_args.append(input(f'{arg}?'))
                result = task_helper['func'](cursor,*final_args)
                if not result:
                    utils.print_data(result)
                
            except Exception as e:
                print(e)
                print("Command not recognized.")


if __name__ == '__main__':
    main()
