from customer.models import *
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def common_category():
    category = Categories.objects.all()
    return {'category': category}

def send_order_confirmation_email(to_email, firstname, lastname, order_id, product):
    subject = 'Order Confirmation'
    from_email = 'yourshop@example.com'
    to = [to_email]

    context = {
        'firstname': firstname,
        'lastname': lastname,
        'order_id': order_id,
        'product': product
    }

    text_content = f'Dear {firstname} {lastname},\n\nYour order has been successfully placed. Your order ID is {order_id}.\n\nHere are the details of your order:\n\n'
    for product in product:
        text_content += f'Product: {product["product_name"]}, Quantity: {product["quantity"]}, Amount: {product["amount"]}\n'
   
    text_content += '\nThank you for shopping with us!'

    html_content = render_to_string('customer/email.html', context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()