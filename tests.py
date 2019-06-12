import os
import sys
import io
import traceback
from unittest import mock
import contextlib

import ticket_viewer
import display_ticket_list
import display_ticket
import zendesk_interface
import io_process


def main():
    unit_tests()
    integration_test()
    print("Testing complete.")


def unit_tests():
    io_process_tests()
    display_ticket_list_tests()
    display_ticket_tests()
    zendesk_interface_tests()


def io_process_tests():
    #throw commands at the get_command function, make sure it doesn't
    #accept bad ones or not accept good ones
    def test_get_command():
        print(  "Testing get_command; may hang on input "
                "(entering 'z' or 'c' should resolve)")
        with mock.patch('builtins.input',side_effect = ["f","b","c","d","e"]):
            leftover_input = []
            command = io_process.get_command(["z","c"])
            #flush output
            while True:
                try:
                    leftover_input=leftover_input+[input()]
                except StopIteration:
                    break
            if command != "c":
                print(  "Issue with get_command: command is {} "
                        "(should be 'c')".format(str(command)))
            if(leftover_input != ["d","e"]):
                print(  "Issue with get_command; remaining input is {} (should"
                    " be [\"d\",\"e\"])".format(str(leftover_input)))
        print("Done testing get_command.\n")

    #throw inputs at the get_number function, make sure it doesn't
    #accept too-low or too-high or non-number, and make sure it
    #accepts good number
    def test_get_number():
        print(  "Testing get_number; may hang on input "
                "(entering '1' should resolve)")
        with mock.patch(
                'builtins.input',side_effect = [0,-20,"b",200,41,40,2,7]):
            leftover_input = []
            sys.stdout = open(os.devnull, 'w')
            number = io_process.get_number("",40)
            sys.stdout = sys.__stdout__
            #flush output
            while True:
                try:
                    leftover_input = leftover_input+[input()]
                except StopIteration:
                    break
            if(number != 40):
                print(  "Issue with get_number; successful input is {}"
                        " (should be 40)".format(str(number)))
            if(leftover_input != [2,7]):
                print(  "Issue with get_number; remaining input is "
                        "{} (should be [2,7])".format(str(leftover_input)))
        print("Done testing get_number.\n")
        return

    #check that the authentication obtained is as it's written in the file
    #(and that it doesn't crash)
    def test_get_authentication():
        login = ("","","")
        try:
            login = io_process.get_authentication()
        except Exception:
            print(  "Get authentication failed;"
                    " {}".format(traceback.format_exc()))
        if (login != ("https://internship-sample.zendesk.com",
                    "swannmar@gmail.com/token",
                    "x3hlrjtVYH7oT6zTGjhv4fIV2z2r0sSrnEjLK2vx")):
            print("Issue with get authentication: read {}".format(str(login)))
        print("Get authentication test completed.")

    test_get_command()
    test_get_number()
    test_get_authentication()


def display_ticket_list_tests(): 
    def test_display_ticket_list():
        #test universal output structure
        successful_output = (
            "\nID:        Type:    Priority: Status: Created:   "
            "Updated:   Due:       Subject/Tags:\nPage 1/1\n\n"
            "'n' for next page, 'p' for previous page, "
            "'j' to jump to a page,'v' to view a ticket, "
            "'r' to refresh list of tickets, 'q' to quit.\n")
        actual_output = io.StringIO()
        try:
            with contextlib.redirect_stdout(actual_output):
                display_ticket_list.display_ticket_list(1,[])
            if (actual_output.getvalue() != successful_output):
                print(  "Issue with display_ticket_list; output was\n{}."
                        "instead of\n{}.".format(
                            actual_output.getvalue(),successful_output))
        except Exception:
            print(  "Display ticket list with artifical input failed; "
                    "{}".format(traceback.format_exc()))
        print("Display ticket_list test completed.")

    #test output of artificial tickets, and make sure only <=25 are displayed
    def test_print_ticket_list(ticket_list,page,output):
        successful_output = (output)
        actual_output = io.StringIO()
        try:
            with contextlib.redirect_stdout(actual_output):
                display_ticket_list.print_ticket_list(ticket_list,page)
            if (actual_output.getvalue() != successful_output):
                print(  "Issue with print_ticket_list; output was\n{}."
                        "instead of\n{}.".format(
                            actual_output.getvalue(),
                            successful_output))
        except Exception:
            print(  "Print ticket list failed; "
                    "{}".format(traceback.format_exc()))
        print("Print ticket list test completed.")

    blank_ticket = {}
    blank_ticket_output = (
        "Missing    Missing  Missing   Missing Missing    "
        "Missing    Missing    Missing  Missing\n")

    sample_ticket = {"id":4,"type":"problem","priority":"urgent",
                    "status":"open","created_at":"2019-14-88",
                    "updated_at":"1000-01-21","due_at":"9999-99-99",
                    "subject":"this is a test subject","tags":["a","b","c"]}

    sample_ticket_output = (
        "4          problem  urgent    open    2019-14-88 "
        "1000-01-21 9999-99-99 \"this is a test subject\"  ['a', 'b', 'c']\n")

    test_display_ticket_list()
    test_print_ticket_list(
        (   [sample_ticket]*5+[blank_ticket]*10
            +[sample_ticket]*10+[blank_ticket]*10),
        1,
        sample_ticket_output*5+blank_ticket_output*10+sample_ticket_output*10)

    test_print_ticket_list(
        (   [sample_ticket]*5+[blank_ticket]*10
            +[sample_ticket]*10+[blank_ticket]*10),
        2,
        blank_ticket_output*10)


def display_ticket_tests(): 
    def test_display_ticket(output,ticket):
        successful_output = (output)
        actual_output = io.StringIO()
        try:
            with contextlib.redirect_stdout(actual_output):
                display_ticket.display_ticket(ticket)
            if (actual_output.getvalue() != successful_output):
                print(
                    "Issue with display_ticket; output was\n{}."
                    "instead of\n{}.".format(   actual_output.getvalue(),
                                                successful_output))
        except Exception:
            print(  "Display ticket failed; "
                    "{}".format(traceback.format_exc()))
        print("Display ticket test completed.")

    test_display_ticket("\nid  : 7\nid2 : 8\n",{"id":7,"id2":8})
    test_display_ticket("\n",{})
    test_display_ticket(
        ("\ntest                      : 89\n"
        "really_long_variable_name : yes\n")
        ,{"test":89,"really_long_variable_name":"yes"})


def zendesk_interface_tests(): 
    def test_get_json():
        try:
            zendesk_interface.get_json(
                "https://internship-sample.zendesk.com/api/v2/tickets.json",
                "swannmar@gmail.com/token",
                "x3hlrjtVYH7oT6zTGjhv4fIV2z2r0sSrnEjLK2vx")
        except SystemExit:  
            print("Get json received non-200 status code on get tickets.json")
        except Exception:
            print(  "Get json failed on tickets.json request; "
                    "{}".format(traceback.format_exc()))
        try:
            zendesk_interface.get_json(
                "https://internship-sample.zendesk.com/api/v2/tickets/1.json",
                "swannmar@gmail.com/token",
                "x3hlrjtVYH7oT6zTGjhv4fIV2z2r0sSrnEjLK2vx")
        except SystemExit:
            print(  "Get json received non-200 status code on get "
                    "tickets/1.json.")
        except Exception:
            print(  "Get json failed on tickets/1.json request; "
                    "{}".format(traceback.format_exc()))
        print("Get json test completed.")

    def test_handle_response_code():
        try:
            zendesk_interface.handle_response_code(200)
        except Exception:
            print(  "Handle response code quit on status 200; "
                    "{}".format(traceback.format_exc()))
        for error_code in [1,301,400,401,403,404,500,503,504]:
            try:
                zendesk_interface.handle_response_code(error_code)
                print(  "Handle response code failed to quit on status"
                        " {}".format(error_code))
            except SystemExit:
                continue
            except Exception:
                print(  "Handle response code quit abnormally on status {};"
                        " {}".format(error_code,traceback.format_exc()))
        print("Handle response code test completed.")

    def test_get_ticket_list():
        try:
            zendesk_interface.get_ticket_list(
                "https://internship-sample.zendesk.com",
                "swannmar@gmail.com/token",
                "x3hlrjtVYH7oT6zTGjhv4fIV2z2r0sSrnEjLK2vx")
        except SystemExit:
            print("Get ticket list received a non-200 status code.")
        except Exception:
            print("Get ticket list failed; {}".format(traceback.format_exc()))
        print("Get ticket list test completed.")

    def test_get_ticket():
        try:
            zendesk_interface.get_ticket(
                "https://internship-sample.zendesk.com",
                "swannmar@gmail.com/token",
                "x3hlrjtVYH7oT6zTGjhv4fIV2z2r0sSrnEjLK2vx",1)
        except SystemExit:
            print("Get ticket received a non-200 status code.")
        except Exception:
            print("Get ticket failed; {}".format(traceback.format_exc()))
        print("Get ticket test completed.")

    test_get_json()
    test_handle_response_code()
    test_get_ticket_list()
    test_get_ticket()


def integration_test():
    print("Running integration test; may hang on input")
    with mock.patch('builtins.input',side_effect = [
            "n","n","n","n","n",
            "p","p","p","p","p","n","n","n","p","p","p","x",
            "j",3,"j",1,"j",7000,1,"v",1,"","v",7000,60,"r","q","j",7
            ]):
        sys.stdout = open(os.devnull, 'w')
        try:
            ticket_viewer.main()
        except Exception:
            sys.stdout = sys.__stdout__
            print("Integration test failed: {}".format(traceback.format_exc()))
            #flush output
            leftover_input=[]
            while True:
                try:
                    leftover_input = leftover_input+[input()]
                except StopIteration:
                    break
            if(leftover_input != ["j",7]):
                print(  "Issue with integration test; remaining input is"
                        "{} (should be [\"j\",7])".format(str(leftover_input)))
        except SystemExit:
            sys.stdout = sys.__stdout__
            #flush output
            leftover_input = []
            while True:
                try:
                    leftover_input = leftover_input+[input()]
                except StopIteration:
                    break
            if(leftover_input != ["j",7]):
                print(  "Issue with integration test; remaining input is"
                        "{} (should be [\"j\",7])".format(str(leftover_input)))
    print("Done running integration test.\n")


if __name__ == "__main__":
    main()