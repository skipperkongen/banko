def render_ascii(rows):
    lines = []
    for row in rows:
        line = ' '.join([
            '  ' if cell is None else
            f' {cell}' if cell<10 else
            f'{cell}'
            for cell in row
        ])
        lines.append(line)
    return '\n'.join(lines)
