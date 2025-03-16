from enum import Enum


class Commands(Enum):
    FIND_CONTACT = "find-contact"
    ADD_CONTACT = "add-contact"
    REMOVE_CONTACT = "remove-contact"
    UPDATE_NAME = "update-name"

    ADD_PHONE = "add-phone"
    UPDATE_PHONE = "update-phone"
    REMOVE_PHONE = "remove-phone"

    ADD_ADDRESS = "address"
    CLEAR_ADDRESS = "clear-address"

    ADD_EMAIL = "email"
    CLEAR_EMAIL = "clear-email"

    ADD_BIRTHDAY = "birthday"
    CLEAR_BIRTHDAY = "clear-birthday"

    BIRTHDAYS = "birthdays"

    ADD_NOTE = "add-note"
    UPDATE_NOTE = "update-note"
    REMOVE_NOTE = "remove-note"
    ADD_TAGS = "add-tags"
    REMOVE_TAGS = "remove-tags"
    FIND_NOTES = "find-notes"
    FIND_TAGS = "find-tags"

#  birthday Name 12.13.2222
#  email Name sdfsfd@asdd.cpm
#
#
# add-note Title Text
# update-note Title
#
#
# add-tags Title askldl as;ldk asda;lsd asda sdasd
#


# @sure_remove
# def remove_contact():
