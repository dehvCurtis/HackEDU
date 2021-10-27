# Non-Compliant Code
import html

def encode_for_html(error_message):    
    return error_message

# Compliant Code
import html

def encode_for_html(error_message):    
    error_enc = html.escape(error_message)
    return error_enc