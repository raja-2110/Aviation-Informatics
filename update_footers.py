import os, glob

old_footer = '''                                <div class="footer-contact">
                                    <h2>Our Address</h2>
                                    <p><i class="fa fa-map-marker-alt"></i>172, cessna street, piper layout, Coimbatore</p>
                                    <p><i class="fa fa-phone-alt"></i>+91 9876504321</p>
                                    <p><i class="fa fa-envelope"></i>aviationinformatics@gmail.com</p>'''

new_footer = '''                                <div class="footer-contact">
                                    <h2>Aviation Support Hub</h2>
                                    <p><i class="fa fa-headset"></i>24/7 Digital Assistance</p>
                                    <p><i class="fa fa-envelope"></i>support@aviationinformatics.com</p>
                                    <p><i class="fa fa-globe"></i>Serving the Global Aviation Community</p>'''

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if "Our Address" in content and "cessna street" in content:
        # replace more robustly
        start_idx = content.find('<div class="footer-contact">')
        if start_idx != -1:
            end_idx = content.find('</div>', start_idx)
            # Find the specific block
            address_block_start = content.find('<h2>Our Address</h2>', start_idx)
            if address_block_start != -1 and address_block_start < end_idx:
                # Let's just do a simple replace of the known exact string, or a regex replacement
                # Since spacing might be off, let's use exact string first
                pass

    if old_footer in content:
        content = content.replace(old_footer, new_footer)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f'Successfully updated footer in {f}')
    else:
        print(f'Pattern not found exactly in {f}, might need manual check.')
