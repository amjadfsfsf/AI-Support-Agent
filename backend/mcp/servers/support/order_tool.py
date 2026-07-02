orders = {

    1001: "Processing",

    1002: "Delivered",

    1003: "Cancelled"
}


def get_order(order_id: int):

    return orders.get(order_id, "Order not found.")