class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = ''

        width = 0
        for word in words:
            width += len(word)
            if width > maxWidth:
                lines = lines[:-1] + '\n'
                width = len(word)
            
            lines += f'{word} '
            
            width += 1
        
        lines = lines.split('\n')
        no_of_lines = len(lines)

        print(f'Total Lines : {no_of_lines}')

        for i,line in enumerate(lines):
            line = line.strip()
            no_of_spaces_present = len(line.split())-1
            extra_spaces = maxWidth - len(line) + no_of_spaces_present

            if no_of_spaces_present==0:
                lines[i] = line + ' '*extra_spaces
                continue
            elif i == no_of_lines-1:
                lines[i] = line + ' '*(extra_spaces-no_of_spaces_present)
                break
            
            spaces_per_word = ' '*max(extra_spaces//no_of_spaces_present,1)
            print('Spaces per word:',len(spaces_per_word))
            line = spaces_per_word.join(line.split())
            print(f'LINE: {line}')

            left_spaces = maxWidth - len(line)
            print(f'LINE: {line} | {left_spaces}')

            if left_spaces:
                print(f'LINE 1: {line}')
                line = line.replace(spaces_per_word,spaces_per_word+' ',left_spaces)
                print(f'LINE 2: {line}')
            
            lines[i] = line
                
        return lines