This program requires python 3 to run. No other installation is required.

To run the program, execute 'python ticket_viewer.py' via command prompt, or equivalent.

The program automatically presents the list of all tickets upon loading, together with use instructions. Use instructions are included in this file as well, and are as follows:
-From the list of tickets, entering 'n' or 'p' moves through pages, which will present the new page before reiterating the list of commands.
-Similarly, 'j' presents a prompt for a number, which lets the user jump to a desired page without having to cycle through them one at a time.
-Entering 'v' presents a prompt for an ID number, which will then display the corresponding ticket in full detail. After this, pressing enter again will return to the list of tickets, at the page the user was previously on.
-Entering 'r' will refresh the list of tickets, i.e. request a new one, in case it has been updated since the last request. The list of tickets will not refresh otherwise, so as to prevent unnecessary downloads and the time/data/power spent in doing so.
-Entering 'q' will exit the program.

The login details are read from authentication.txt (so as to make it comparatively easy to swap to different ones if needed) and are stored in token form (so as to avoid disclosing passwords); the first line is the username, the second is the password, and the third is their website at zendesk.


________________________________________________________________________________


The program is split into 5 components: one which handles displaying the list of tickets, one which handles displaying an individual ticket, one which handles making requests to the zendesk API, one which handles the input/output, and lastly one which handles overall code structure.

The list of tickets is displayed in table format, with the following fields: id, type, priority, status, created_at, updated_at, due_at, subject, tags. The individual ticket display shows all of its initialised fields and their values, with the colons separating them aligned for readability and aesthetic.

It is assumed that the maximum ticket ID is 1,000,000,000. Ticket IDs higher than this should only cause trivial display issues at best, i.e. slightly-misaligned columns.

The tests were constructed by writing one test for each function, after removing trivial one-line functions (such as zendesk_interface.get_ticket, which is essentially equivalent to zendesk_interface.get_json). API-related functions just involve running the function and ensuring it does not crash; this is just because trying to evaluate the output/return-value is questionable, given that it's connecting to a completely separate thing. Functions with meaningful output or return values have those compared to what they are supposed to be, as basic unit tests; this includes abnormal input/output or input/return pairs, such as displaying an empty ticket. Functions that require input (this includes an integration test on ticket_viewer.main) have stdin mocked, and their possible values tested (valid inputs, invalid inputs, and abnormal inputs all). 






