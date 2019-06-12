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


The program is split into 4 components: one which handles displaying the list of tickets, one which handles displaying an individual ticket, one which handles making requests to the zendesk API, and one which handles the input/output and overall code structure.

The list of tickets is displayed in table format, with the following fields: id, type, priority, status, created_at, updated_at, due_at, subject, tags. The individual ticket display shows all of its initialised fields.

It is assumed that the maximum ticket ID is 1,000,000,000. Ticket IDs higher than this should only cause trivial display issues at best, i.e. slightly-misaligned columns.

The current design has no meaningful advantage, and is only the way it is as a result of time constraints, so the following changes are acknowledged as improvements:
-moving more of the API-related functions (such as appending the proper strings to the base url) to zendesk_interface
-maybe extracting out the input/output and putting that in its own module separate to the ticket_viewer module (which presently handles both input/output as well as overall program logic/structure).

The tests were constructed by writing one test for each function, after removing the trivial functions (such as get_ticket, which is basically just a call to get_json (see previous comment about moving API functions to zendesk_interface!)). API-related functions just involve running the function and ensuring it does not crash. Functions with meaningful output or return values have those compared to what they are supposed to be, as basic unit tests; this includes abnormal input/output or input/return pairs, such as displaying an empty ticket. Functions that require input (this includes an integration test on ticket_viewer.main) have stdin mocked, and their possible values tested (valid inputs, invalid inputs, and abnormal inputs all). 






