# Bug Type: Expression modification

def levenshtein(source, target):
    if not source:
        return len(target)
    if not target:
        return len(source)

    if source[0] == target[0]:
        return levenshtein(source[1:], target[1:])
    else:
        return 1 + min(
            levenshtein(source, target[1:]),
            levenshtein(source[1:], target[1:]),
            levenshtein(source[1:], target)
        )
