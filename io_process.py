def get_command(legal_commands):
    command = ""
    while(command not in legal_commands):
        command = input()
    return command


#in this function, the continues serve as "bad input; go back to start of loop"
def get_number(prompt,max_=float('inf')):
    while(True):
        output = input(prompt)
        try:
            output = int(output)
            if (output < 1):
                print(str(output)+" is not a valid number (must be above 0).")
                continue
            elif (output > max_):
                print(str(output)+" is not a valid number (too big).")
                continue
        except ValueError:
            print(str(output)+" is not a number.")
            continue
        return output


#Get authentication details and base url from file
def get_authentication():
    authentication = open("authentication.txt","r")
    #trim newlines
    user = authentication.readline()[:-1]
    pwd = authentication.readline()[:-1]
    #can append '.json' for all tickets, '/{id}.json' for individual ticket
    url = authentication.readline()

    return (url,user,pwd)