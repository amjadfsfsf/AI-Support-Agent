tickets = []


def create_ticket(name: str, email: str, issue: str):

    ticket = {

        "id": len(tickets) + 1,

        "name": name,

        "email": email,

        "issue": issue,

        "status": "Open"
    }

    tickets.append(ticket)

    return ticket


def get_ticket(ticket_id: int):

    for ticket in tickets:

        if ticket["id"] == ticket_id:

            return ticket

    return "Ticket not found."