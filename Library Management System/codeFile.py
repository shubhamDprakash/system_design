from abc import ABC, abstractmethod
from enum import Enum
from typing import List

class BookStatus(Enum):
    AVAILABLE, RESERVED, ISSUED, LOST = 1, 2, 3, 4

class BookCategory(Enum):
    ROMANTIC, DRAMA, SCIENCE_FICTION, SELF_HELP = 1, 2, 3, 4

class Constants():
    def __init__(self) -> None:
        self.max_checkout_limit = 5
        self.max_retention_days = 10

class Address():
    def __init__(self, address_line, city, pin_code, state, country) -> None:
        self.address_line = address_line
        self.city = city
        self.pin_code = pin_code
        self.state = state
        self.country = country

class Library:
    def __init__(self, name: str, location: Address, book_count) -> None:
        self.name = name
        self.location = location
        self.book_count = book_count

class Book:
    def __init__(self, uniqueId, title, author, subject, authors: list, category: BookCategory) -> None:
        self.uniqueId = uniqueId
        self.title = title
        self.authors = authors
        self.subject = subject
        self.book_category: BookCategory = category

class BookItem(Book):
    def __init__(self, uniqueId, title, author, subject, authors: list, category: BookCategory, bar_code, rackId: Rack, pub_date, status: BookStatus) -> None:
        super().__init__(uniqueId, title, author, subject, authors, category)
        self.bar_code = bar_code
        self.rackId: Rack = rackId
        self.pub_date = pub_date
        self.status: BookStatus = status

class Rack():
    def __init__(self, rId, positionId) -> None:
        self.rId = rId
        self.positionId = positionId

class Person():
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

class Author(Person):
    def __init__(self, first_name, last_name, books: List[Book]) -> None:
        super().__init__(first_name, last_name)
        self.books: List[Book] = books
        
class SystemUser(Person):
    def __init__(self, first_name, last_name, email, phone_number, account: Account) -> None:
        super().__init__(first_name, last_name)
        self.email = email
        self.phone_number = phone_number
        self.account: Account = account

class Student(SystemUser):
    def __init__(self, first_name, last_name, email, phone_number, account: Account, member_card: MemberCard, total_books_taken, search: Search, book_issue_service: BookIssueService) -> None:
        super().__init__(first_name, last_name, email, phone_number, account)
        self.member_card: MemberCard = member_card
        self.total_books_taken = total_books_taken
        self.search: Search = search
        self.book_issue_service: BookIssueService = book_issue_service

class MemberCard():
    def __init__(self, bar_code: str) -> None:
        self.bar_code: str = bar_code

class Librarian(SystemUser):
    def __init__(self, first_name, last_name, email, phone_number, account: Account, search: Search, book_issue_service: BookIssueService) -> None:
        super().__init__(first_name, last_name, email, phone_number, account)
        self.search: Search = search
        self.book_issue_service: BookIssueService = book_issue_service

        def add_item(self, book_item: BookItem):
            pass

        def delete_item(self, bar_code):
            pass

        def update_item(self, book_item: BookItem):
            pass

class Account():
    def __init__(self, user_name, password, account_id) -> None:
        self.user_name = user_name
        self.password = password
        self.account_id = account_id

class Search():
    def get_book_by_title(self, title) -> List[BookItem]:
        pass
    def get_book_by_author(self, author) -> List[BookItem]:
        pass
    def get_book_by_subject(self, subject) -> List[BookItem]:
        pass
    def get_book_by_category(self, category) -> List[BookItem]:
        pass
    def get_book_by_publication_date(self, pub_date) -> List[BookItem]:
        pass

class BookIssueService():
    def __init__(self, fine_service: FineService) -> None:
        self.fine_service: FineService = fine_service

    def get_book_reservation_detail(self, book_item: BookItem) -> BookReservationDetail:
        pass
    def update_reservation_detail(self, reservation_detail: BookReservationDetail):
        pass
    def reserve_book(self, book_item: BookItem, user: SystemUser) -> BookReservationDetail:
        pass
    def issue_book(self, book_item: BookItem, user: SystemUser) -> BookIssueDetail:
        pass
    def return_book(self, book_item: BookItem, user: SystemUser):
        pass

class BookLending():
    def __init__(self, book_item: BookItem, date, user: SystemUser) -> None:
        self.book_item: BookItem = book_item
        self.date = date
        self.user: SystemUser = user

class BookReservationDetail(BookLending):
    def __init__(self, book_item: BookItem, date, user: SystemUser, reservation_status: ReservationStatus) -> None:
        super().__init__(book_item, date, user)
        self.reservation_status: ReservationStatus = reservation_status

class BookIssueDetail(BookLending):
    def __init__(self, book_item: BookItem, date, user: SystemUser, due_date) -> None:
        super().__init__(book_item, date, user)
        self.due_date = due_date

class ReservationStatus():
    def __init__(self, is_reserved: bool) -> None:
        self.is_reserved: bool = is_reserved

class FineService():
    def calculate_fine(self, user: SystemUser, book_item: BookItem, days):
        pass


