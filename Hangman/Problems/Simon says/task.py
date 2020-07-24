def what_to_do(instructions):
    if str(instructions).startswith('Simon says') or str(instructions).endswith('Simon says'):
        return 'I ' + instructions.replace('Simon says', '').strip()
    return "I won't do it!"
