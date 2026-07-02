from database import conn
cursor = conn.cursor()


def create_ticket(name: str, email: str, issue: str):

    cursor.execute(
        """
        INSERT INTO tickets(name,email,issue,status)
        VALUES(?,?,?,?)
        """,
        (
            name,
            email,
            issue,
            "Open"
        )
    )

    conn.commit()

    ticket_id = cursor.lastrowid

    return f"""
    ✅ Support ticket created successfully.

    Ticket ID: {ticket_id}

    Status: Open

    We'll contact you as soon as possible.
    """


def get_ticket(ticket_id: int):

    cursor.execute(
        """
        SELECT *
        FROM tickets
        WHERE id=?
        """,
        (ticket_id,)
    )

    ticket = cursor.fetchone()

    if ticket is None:

        return {
            "error": "Ticket not found"
        }

    return {

        "id": ticket[0],

        "name": ticket[1],

        "email": ticket[2],

        "issue": ticket[3],

        "status": ticket[4]
    }


def close_ticket(ticket_id: int):

    cursor.execute(
        """
        UPDATE tickets
        SET status=?
        WHERE id=?
        """,
        (
            "Closed",
            ticket_id
        )
    )

    conn.commit()

    return {
        "message": "Ticket closed."
    }


def reopen_ticket(ticket_id: int):

    cursor.execute(
        """
        UPDATE tickets
        SET status=?
        WHERE id=?
        """,
        (
            "Open",
            ticket_id
        )
    )

    conn.commit()

    return {
        "message": "Ticket reopened."
    }


def list_tickets():

    cursor.execute(
        """
        SELECT *
        FROM tickets
        """
    )

    rows = cursor.fetchall()

    tickets = []

    for row in rows:

        tickets.append({

            "id": row[0],

            "name": row[1],

            "email": row[2],

            "issue": row[3],

            "status": row[4]
        })

    return tickets